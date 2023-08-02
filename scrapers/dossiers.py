#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    This file is part of parltrack

#    parltrack is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    parltrack is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with parltrack  If not, see <http://www.gnu.org/licenses/>.

# (C) 2019 by Stefan Marsiske, <parltrack@ctrlc.hu>

from urllib.request import ProxyHandler
from urllib.parse import urljoin, urlsplit, urlunsplit
from utils.utils import fetch, fetch_raw, unws
from lxml.etree import fromstring
from utils.mappings import SPLIT_DOSSIERS
from utils.log import log
from db import db
from config import CURRENT_TERM, USER_AGENT, PROXY
import feedparser, datetime
import html

CONFIG = {
    'threads': 8,
    'timeout': 60,
    'retries': 5,
    'error_handler': None,
}

feedparser.USER_AGENT=USER_AGENT
handlers=[ProxyHandler({'http': PROXY})]

BASE_URL = 'https://oeil.secure.europarl.europa.eu'

def get_new_dossiers(**kwargs):
    f = feedparser.parse('https://oeil.secure.europarl.europa.eu/oeil/search/result.rss?s1&all&limit=100&lang=en', handlers=handlers)
    if not f:
        return
    refs = set(db.dossier_refs())
    for item in f.entries:
        ref = item.title
        if '*' in ref: ref = ref[:ref.index('*')]
        if ref in refs: continue
        url=html.unescape(urljoin(BASE_URL, urlunsplit(('','')+urlsplit(item.link)[2:])))
        log(4,'adding dossier scraping job %s' % url)
        payload = dict(kwargs)
        payload['url'] = url
        add_job('dossier', payload=payload)

def get_all_dossiers(**kwargs):
    urltemplate = 'https://oeil.secure.europarl.europa.eu/oeil/search/result.do?page={page}&sort=d&:year={year}'
    for year in range(datetime.date.today().year, 1971, -1):
        page = 1
        tree=fetch(urltemplate.format(**locals()))
        tmp = tree.xpath('//span[@class="ep_name" and (starts-with(normalize-space(),"Results found :") or starts-with(normalize-space(),"Result found :"))]/text()')
        if not tmp:
            log(1, "no dossiers found for %d" % year)
            raise ValueError("failed to find number of dossiers for year %d" % year)
        tmp = unws(tmp[0])
        count = int(tmp[tmp.index(":")+1:])
        log(4,"year %d, count %d" % (year, count))
        items = tree.xpath('//a[@class="reference rssEntry_id rssEntry_title rssEntry_updated"]')
        cnt=0
        while len(items)>0:
           for item in items:
               url=html.unescape(urljoin(BASE_URL, urlunsplit(('','')+urlsplit(item.get('href'))[2:])))
               log(4,'adding dossier scraping job %s' % url)
               payload = dict(kwargs)
               payload['url'] = url
               add_job('dossier', payload=payload)
               cnt+=1
           page+=1 
           tree=fetch(urltemplate.format(**locals()))
           items = tree.xpath('//a[@class="reference rssEntry_id rssEntry_title rssEntry_updated"]')
        log(4,"year %d, found %d" % (year, cnt))

def get_active_dossiers(**kwargs):
    i=0
    splitdossiers = set(SPLIT_DOSSIERS)
    for doc in db.dossiers_by_activity(True):
        url = doc['meta']['source']
        ref = doc['procedure']['reference']
        if ref in splitdossiers: continue
        log(4,'adding dossier scraping job %s' % url)
        payload = dict(kwargs)
        payload['url'] = url
        add_job('dossier', payload=payload)
        i+=1
    log(3,"total %d" % i)

def scrape(all=False, **kwargs):
    if all: get_all_dossiers(**kwargs)
    else:
        get_new_dossiers(**kwargs)
        get_active_dossiers(**kwargs)

if __name__ == '__main__':
    scrape(all=True)
