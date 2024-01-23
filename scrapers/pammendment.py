#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    This file is part of parltrack.

#    parltrack is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    parltrack is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with parltrack.  If not, see <http://www.gnu.org/licenses/>.

# (C) 2024 by Stefan Marsiske, <parltrack@parltrack.eu>


import os, re, sys, unicodedata
from tempfile import mkstemp
from sh import pdftotext
from dateutil.parser import parse
from utils.utils import fetch_raw, unws, jdump
from utils.log import log
from db import db
from scrapers.amendment import getraw, isfooter, parse_block
from scrapers import amendment

pere = r'(?P<PE>PE(?:TXTNRPE)? ?[0-9]{3,4}\.?[0-9]{3}(?:v[0-9]{2}(?:[-./][0-9]{1,2})?)?)'
amdoc=r'AM\\[0-9]{4,7}(?:EN|XM|XT)?\.(?:doc|DOC|tmp|docx)'

headerre=re.compile(r'\s*(?P<date>\d{1,2}\.\d{1,2}\.\d{4})\s*(?P<Aref>A[789]-\d{4}/\d{1,4})')
def isheader(line):
   return headerre.match(line)

def unpaginate(text, url):
    lines = text.split('\n')
    ## find end of 1st page
    #eo1p = 0
    PE = None
    date = None
    aref = []
    #while not lines[eo1p].startswith('\x0c') and eo1p<len(lines):
    #    eo1p+=1
    #if eo1p == len(lines):
    #    log(1, "could not find end of 1st page in %s" % url)
    #    raise ValueError("eo1p not found: %s" % url)

    i = len(lines) - 1
    while i>=0:
        if not lines[i].startswith('\x0c'):
            i -= 1
            continue

        # we found a line starting with pagebreak
        lines[i]=lines[i][1:]
        i -= 1
        fstart = i

        header = isheader(lines[fstart+1])
        if header:
           date1 = header.group("date")
           if date:
              if date1 != date:
                 log(1, f"date found, but is not consistent: {date} != {date1}")
           else:
              date = date1
           aref1 = header.group('Aref')
           if aref1:
              aref.append(aref1)
           del lines[fstart+1]

        # skip empty lines before pagebreak
        while i>=0 and unws(lines[i])=='':
            i-=1

        # we expect i>0 and lines[i] == 'EN' (or variations)
        if i<=0:
            log(1, "could not find non-empty line above pagebreak in %s" % url)
            raise ValueError("no EN marker found: %s" % url)

        tmp = unws(lines[i])
        if tmp not in ["EN", "EN EN", "EN United in diversity EN",
                       "EN Unity in diversity EN",
                       "EN Unie dans la diversité EN",
                       "EN In Vielfalt geeint EN",
                       "ENEN United in diversity EN",
                       "XM United in diversity XM",
                       "XT United in diversity EN",
                       "XM", "XM XM", "XT", "XT XT"]:
            if tmp in ["FR",'NL','HU']:
                log(2,'Document has non-english language marker: "%s" %s' % (tmp, url))
                return [], None
            if tmp=="Or. en":
                # no footer in this page
                continue
            if tmp in ['AM_Com_NonLegCompr', 'AM_Com_NonLegReport','AM_Com_NonLegOpinion']:
                # no footer on this page (and probably neither on the previous one which should be the first)
                continue
            if isfooter(tmp):
                if PE is None: # try to figure out PE id
                    m = pere.match(tmp)
                    if m: PE = m.group(0)
                log(3, 'no EN marker found, but footer: "%s"' % tmp)
                i+=1 # neutralize the decrement after this block
            else:
                log(1, 'could not find EN marker above pagebreak: %d %d "%s"' % (i, eo1p, tmp))
                raise ValueError('no EN marker found "%s" in %s' % (tmp,url))

        if lines[i].startswith('\x0c'): # we found a ^LEN^L
            # we found an empty page.
            while fstart > i:
                del lines[fstart]
                fstart -= 1
            lines[i]="\x0c"
            continue

        i -= 1

        # find the next non-empty line above the EN marker
        while i>0 and unws(lines[i])=='':
            i-=1
        if i<=0:
            log(1, "could not find non-empty line above EN marker: %s" % url)
            raise ValueError("no next line above EN marker found: %s" % url)

        footer = isfooter(lines[i])
        if PE is None and footer.group('PE'):
           PE = footer.group('PE')
        if (not footer):
            tmp = unws(lines[i])
            if tmp=="Or. en":
                i+=1 # preserve this line - and cut of the rest
            elif tmp not in ['AM_Com_NonLegCompr', 'AM_Com_NonLegReport','AM_Com_NonLegOpinion']:
                log(1,'not a footer: "%s" line: %d in %s' % (repr(lines[i]),i,url))
                raise ValueError('not a footer: "%s" line: %d in %s' % (lines[i],i,url))

        if lines[i].startswith('\x0c'):
            # we found an empty page with only the footer
            lines[i]='\x0c'
            i+=1
        #else: # is a regular page
        #    i -= 1
        #    if unws(lines[i])!='':
        #        for j in range(-10,10):
        #            log(1, '"%s"' % (unws(lines[i+j])))
        #        log(1, 'line above footer is not an empty line: "%s"' % (unws(lines[i])))
        #        raise ValueError("no empty line above footer")

        # delete all lines between fstart and i
        while fstart >= i:
            del lines[fstart]
            fstart -= 1

    header = isheader(lines[0])
    if header:
       date1 = header.group("date")
       if date:
          if date1 != date:
             log(1, f"date found, but is not consistent: {date} != {date1}")
       else:
          date = date1
       aref1 = header.group('Aref')
       if aref:
          aref.append(aref1)
       del lines[0]
    return lines, PE, date, aref

# patch up amendments
amendment.unpaginate = unpaginate
amendment.mansplits={}
amendment.mepmaps={}

refre=re.compile(r'(.*)([0-9]{4}/[0-9]{4}[A-Z]?\((?:ACI|APP|AVC|BUD|CNS|COD|COS|DCE|DEA|DEC|IMM|INI|INL|INS|NLE|REG|RPS|RSO|RSP|SYN)\))')
amstart=re.compile(r' *(Emendamenti|Amende?ment)\s*[0-9A-Z]+( a|/PP)?$')

dossier1stline_re = re.compile(r'(.*)\s*(A[6789]-\d{4}/\d{4})$')
def parse_dossier(lines, date):
   m1 = dossier1stline_re.match(lines[0])
   if not m1:
      log(1, f"dossier block line 0 has no 'A[6789]-' postfix. {repr(lines[0])}")
      return
   dossier = {
      'type' : unws(m1.group(1)),
      'aref' : m1.group(2)
      }
   mepid=db.getMep(unws(lines[1]),date)
   if mepid:
      try: dossier['meps'].append(mepid)
      except KeyError: dossier['meps']=[mepid]

   mr = refre.search(unws(' '.join(lines[2:])))
   if not mr:
      log(1, "could not find dossier reference in rest of dossier block")
      return dossier
   ref=mr.group(2)
   d = db.dossier(ref)
   if not d:
       log(2, f"could not find dossier for ref '{ref}'")
       return dossier
   dossier['dossier']=ref
   return dossier

def scrape(url):
   lines, PE, date, aref = getraw(url)
   #print(PE, date, aref)
   #print('\n'.join(lines))
   block=None
   res=[]
   block=None
   reference=None
   committee=[]
   meps = None
   date = parse(date, dayfirst=True)

   for line in lines:
      if amstart.match(line):
          # parse block
         if block is None:
            block = [line]
            continue

         am=parse_block(block, url, reference, date, meps, PE, parse_dossier=parse_dossier)
         if am is not None:
            #print(jdump(am))
            #process(am, am['id'], db.amendment, 'ep_amendments', am['reference']+' '+am['id'], nodiff=True)
            res.append(am)
         block=[line]
         continue
      if block is not None: block.append(line)

   if block and filter(None,block):
      am = parse_block(block, url, reference, date, meps, PE, parse_dossier=parse_dossier)
      if am is not None:
         #print(jdump(am))
         #process(am, am['id'], db.amendment, 'ep_amendments', am['reference']+' '+am['id'], nodiff=True)
         res.append(am)
   log(3,"total amendments %d in %s" % (len(res),url))
   return res


if __name__ == '__main__':
    scrape	(sys.argv[1])
