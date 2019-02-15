#!/usr/bin/env python
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

buildings={ u"Altiero Spinelli": u'ASP',
            u"Willy Brandt": u'WIB',
            u"Paul-Henri Spaak": u'PHS',
            u"Atrium": u"ATR",
            u"Louise Weiss": u'LOW',
            u"Winston Churchill": u'WIC',
            u'Salvador de Madariaga': u"SDM",
            u"Bât. Altiero Spinelli": u'ASP',
            u"Bât. Willy Brandt": u'WIB',
            u"Bât. Paul-Henri Spaak": u'PHS',
            u"Bât. Atrium": u"ATR",
            u"Bât. Louise Weiss": u'LOW',
            u"Bât. Winston Churchill": u'WIC',
            u'B\xe2t. Salvador de Madariaga': u"SDM",
            }

SEIRTNUOC = {'Belgium': u'BE',
             'Bulgaria': u'BG',
             'Czech Republic': u'CZ',
             'Denmark': u'DK',
             'Germany': u'DE',
             'Estonia': u'EE',
             'Ireland': u'IE',
             'Greece': u'EL',
             'Spain': u'ES',
             'France': u'FR',
             'Italy': u'IT',
             'Cyprus': u'CY',
             'Latvia': u'LV',
             'Lithuania': u'LT',
             'Luxembourg': u'LU',
             'Hungary': u'HU',
             'Malta': u'MT',
             'Netherlands': u'NL',
             'Austria': u'AT',
             'Poland': u'PL',
             'Portugal': u'PT',
             'Romania': u'RO',
             'Slovenia': u'SI',
             'Slovakia': u'SK',
             'Finland': u'FI',
             'Sweden': u'SE',
             'United Kingdom': u'GB',
             'Croatia': u'HR',
             }

COMMITTEE_MAP={u'AFET': u"Foreign Affairs",
               u'DROI': u"Human Rights",
               u'CLIM': u'Climate Change',
               u'CRIM': u'Organised crime, corruption and money laundering',
               u'TDIP': u'Temporary committee on use of European countries by the CIA',
               u'SEDE': u"Security and Defence",
               u'DEVE': u"Development",
               u'INTA': u"International Trade",
               u'BUDG': u"Budgets",
               u'CONT': u"Budgetary Control",
               u'CODE': u"Conciliation Committee",
               u'ECON': u"Economic and Monetary Affairs",
               u'EMPL': u"Employment and Social Affairs",
               u'ENVI': u"Environment, Public Health and Food Safety",
               u'ITRE': u"Industry, Research and Energy",
               u'IMCO': u"Internal Market and Consumer Protection",
               u'TRAN': u"Transport and Tourism",
               u'REGI': u"Regional Development",
               u'AGRI': u"Agriculture and Rural Development",
               u'PECH': u"Fisheries",
               u'CULT': u"Culture and Education",
               u'JURI': u"Legal Affairs",
               u'LIBE': u"Civil Liberties, Justice and Home Affairs",
               u'AFCO': u"Constitutional Affairs",
               u'FEMM': u"Women's Rights and Gender Equality",
               u'PETI': u"Petitions",
               u'CRIS': u"Financial, Economic and Social Crisis",
               u'SURE': u"Policy Challenges Committee",
               u'RETT': u"Regional Policy, Transport and Tourism",
               u'Foreign Affairs': u'AFET',
               u"Regional Policy, Transport and Tourism": u'RETT',
               u'Foreign Affairs': u'AFET',
               u'Subcommittee on Human Rights': u'DROI',
               u'Human Rights': u'DROI',
               u'Security and Defence': u'SEDE',
               u'Development': u'DEVE',
               u'International Trade': u'INTA',
               u'Budgets': u'BUDG',
               u'Budgetary Control': u'CONT',
               u'Organised crime, corruption and money laundering' : u'CRIM',
               u'Economic and Monetary Affairs': u'ECON',
               u'Employment and Social Affairs': u'EMPL',
               u'Environment, Public Health and Food Safety': u'ENVI',
               u'Industry, Research and Energy': u'ITRE',
               u'Internal Market and Consumer Protection': u'IMCO',
               u'Transport and Tourism': u'TRAN',
               u'Regional Development': u'REGI',
               u'Agriculture and Rural Development': u'AGRI',
               u'Fisheries': u'PECH',
               u'Culture and Education': u'CULT',
               u'Legal Affairs': u'JURI',
               u'Civil Liberties, Justice and Home Affairs': u'LIBE',
               u'Constitutional Affairs': u'AFCO',
               u"Women's Rights and Gender Equality": u'FEMM',
               u"Committee on Women's Rights and Gender": u'FEMM',
               u"Women’s Rights and Gender Equality": u'FEMM',
               u'Petitions': u'PETI',
               u'Financial, Economic and Social Crisis': u'CRIS',
               u'Policy Challenges Committee': u'SURE',
               u'Committee on Foreign Affairs': u'AFET',
               u'Committee on Human Rights': u'DROI',
               u'Committee on Security and Defence': u'SEDE',
               u'Committee on Development': u'DEVE',
               u'Committee on development': u'DEVE',
               u'Special Committee on the Financial, Economic and Social Crisis': u'CRIS',
               u'Special committee on the policy challenges and budgetary resources for a sustainable': u'SURE',
               u'Special committee on the policy challenges and budgetary resources for a sustainable European Union after 2013': u'SURE',
               u'Committee on International Trade': u'INTA',
               u'Committee on Budgets': u'BUDG',
               u'Committee on Budgetary Control': u'CONT',
               u'Committee on Economic and Monetary Affairs': u'ECON',
               u'Committee on Employment and Social Affairs': u'EMPL',
               u"Commission de l'emploi et des affaires sociales": u'EMPL',
               u'Commission des libertés civiles, de la justice et des affaires intérieures': u'LIBE',
               u'Committee on Environment, Public Health and Food Safety': u'ENVI',
               u'Committee on the Environment, Public Health and Food Safety': u'ENVI',
               u'Committee on Industry, Research and Energy': u'ITRE',
               u'Committee on Internal Market and Consumer Protection': u'IMCO',
               u'Committee on the Internal Market and Consumer Protection': u'IMCO',
               u'Committee on Transport and Tourism': u'TRAN',
               u'Committee on Regional Development': u'REGI',
               u'Committee on Agriculture and Rural Development': u'AGRI',
               u'Committee on Agricultural and Rural Development': u'AGRI',
               u'Committee on Committee on Agriculture and Rural Development': u'AGRI',
               u"Commission de l'agriculture et du développement rural": u'AGRI',
               u"Commission du marché intérieur et de la protection des consommateurs": u'IMCO',
               u'Co-Committee on the Internal Market and Consumer Protection': u'IMCO',
               u'COMMITTEE ON THE INTERNAL MARKET AND CONSUMER PROTECTION': u'IMCO',
               u'Committee on Fisheries': u'PECH',
               u'Committee on Culture and Education': u'CULT',
               u'Committee on Legal Affairs': u'JURI',
               u'Committee on Civil Liberties, Justice and Home Affairs': u'LIBE',
               u'Committee on Constitutional Affairs': u'AFCO',
               u"Committee on Women's Rights and Gender Equality": u'FEMM',
               u"Committee on Women’s Rights and Gender Equality": u'FEMM',
               u'Committee on Petitions': u'PETI',
               u'Committee on Financial, Economic and Social Crisis': u'CRIS',
               u'Committee on Policy Challenges Committee': u'SURE',
               u"Committee on Constitutional Affairs"                                                                                           : u"AFCO",
               u"Committee on Foreign Affairs"                                                                                                 : u"AFET",
               u"Committee on Agriculture and Rural Development"                                                                               : u"AGRI",
               u"Committee on Budgets"                                                                                                         : u"BUDG",
               u"Temporary Committee Climate Change"                                                                                           : u"CLIM",
               u"Committee on Budgetary Control"                                                                                               : u"CONT",
               u"Temporary Committees Organised Crime, Corruption and Money Laundering"                                                        : u"CRIM",
               u"Temporary Committees Financial, Economic and Social Crisis"                                                                   : u"CRIS",
               u"Committee on Culture and Education"                                                                                           : u"CULT",
               u"Committee on Development"                                                                                                     : u"DEVE",
               u"Subcommittee on Human Rights"                                                                                                 : u"DROI",
               u"Temporary Committee on ECHELON Interception System"                                                                           : u"ECHE",
               u"Committee on Economic and Monetary Affairs"                                                                                   : u"ECON",
               u"Committee on Employment and Social Affairs"                                                                                   : u"EMPL",
               u"Committee on Environment, Public Health and Food Safety"                                                                      : u"ENVI",
               u"Committee of Inquiry into the crisis of the Equitable Life Assurance Society"                                                 : u"EQUI",
               u"Temporary Committee Crisis of the Equitable Life Assurance Society"                                                           : u"EQUI",
               u"Committee of Inquiry into BSE (bovine spongiform encephalopathy)"                                                             : u"ESB1",
               u"Temporary Committee to Monitor Action taken on BSE Recommendations"                                                           : u"ESB2",
               u"Committee on Women's Rights and Gender Equality"                                                                              : u"FEMM",
               u"Temporary Committee on Foot and Mouth Disease"                                                                                : u"FIAP",
               u"Temporary Committee Policy challenges and budgetary means of the enlarged Union 2007-2013"                                    : u"FINP",
               u"Temporary Committee on Policy Challenges and Budgetary Means of the Enlarged Union 2007-2013"                                 : u"FINP",
               u"Temporary Committee on Human Genetics and other New Technologies of Modern Medicine"                                          : u"GENE",
               u"Committee on Internal Market and Consumer Protection"                                                                         : u"IMCO",
               u"Committee on International Trade"                                                                                             : u"INTA",
               u"Committee on Industry, Research and Energy"                                                                                   : u"ITRE",
               u"Committee on Legal Affairs"                                                                                                   : u"JURI",
               u"Committee on Civil Liberties, Justice and Home Affairs"                                                                       : u"LIBE",
               u"Temporary Committee on Improving Safety at Sea"                                                                               : u"MARE",
               u"Committee on Fisheries"                                                                                                       : u"PECH",
               u"Committee on Petitions"                                                                                                       : u"PETI",
               u"Committee on Regional Development"                                                                                            : u"REGI",
               u"Subcommittee on Security and Defence"                                                                                         : u"SEDE",
               u"Temporary Committees Policy Challenges Committee"                                                                             : u"SURE",
               u"Temporary Committee Alleged use of European countries by the CIA for the transport and illegal detention of prisoners"        : u"TDIP",
               u"Temporary Committee on the alleged use of European countries by the CIA for the transport and illegal detention of prisoners" : u"TDIP",
               u"Committee on Transport and Tourism"                                                                                           : u"TRAN",
               u"Committee of Inquiry into the Community Transit Regime"                                                                       : u"TRANSIT",
               u'Special Committee on Tax Rulings and Other Measures Similar in Nature or Effect'                                              : u"TAXE",
               u'Special Committee on Tax Rulings and Other Measures Similar in Nature or Effect (TAXE 2)'                                     : u"TAX2",
               u"Special Committee on Financial Crimes, Tax Evasion and Tax Avoidance"                                                         : u"TAX3",
               u'Special Committee on Terrorism'                                                                                               : u"TERR",
}

ORGMAPS=[('Committee o', 'Committees'),
        ('Temporary committee ', 'Committees'),
        ('Temporary Committee ', 'Committees'),
        ('Subcommittee on ', 'Committees'),
        ('Special Committee ', 'Committees'),
        ('Special committee ', 'Committees'),
        ('Legal Affairs Committee', 'Committees'),
        ('Political Affairs Committee', 'Committees'),
        ('Delegation','Delegations'),
        ('Members from the European Parliament to the Joint ', 'Delegations'),
        ('Membres fron the European Parliament to the ', 'Delegations'),
        ('Conference of ', 'Staff'),
        ("Parliament's Bureau", 'Staff'),
        ('European Parliament', 'Staff'),
        ('Quaestors', 'Staff'),]

GROUP_MAP={ u"Confederal Group of the European United Left - Nordic Green Left": u'GUE/NGL',
            u"Confederal Group of the European United Left-Nordic Green Left": u'GUE/NGL',
            u'Confederal Group of the European United Left / Nordic Green Left': u'GUE/NGL',
            u'Confederal Group of the European United Left/Nordic Green Left': u'GUE/NGL',
            u'Confederal Group of the European United Left': u'GUE/NGL',
            u"European Conservatives and Reformists": u'ECR',
            u'European Conservatives and Reformists Group': u'ECR',
            u"Europe of freedom and democracy Group": u'EFD',
            u'Europe of Freedom and Direct Democracy Group': u"EFDD",
            u'Europe of Freedom and Democracy Group': u'EFD',
            u'Europe of freedom and direct democracy Group': u'EFD',
            u"Group of the Alliance of Liberals and Democrats for Europe": u'ALDE',
            u'Liberal and Democratic Reformist Group': u'LDR',
            u'Group Union for Europe': u'UFE',
            u'European Democratic Group': u'EDG',
            u'Liberal and Democratic Group': u'ALDE',
            u'Technical Group of the European Right': u'DR',
            u'Group of the European Radical Alliance': u'ERA',
            u'Socialist Group': u'SG',
            u'Rainbow Group in the European Parliament': u'RBW',
            u'Group of the European Right': u'ER',
            u'Group of Independents for a Europe of Nations': u'ER',
            u'Left Unity': u'LU',
            u'Group for the European United Left': u'GUE',
            u'Group of the European Democratic Alliance': u'EDA',
            u"Group of the Greens/European Free Alliance": u"Verts/ALE",
            u'The Greens/European Free Alliance': u"Verts/ALE",
            u"Group of the Progressive Alliance of Socialists and Democrats in the European Parliament": u"S&D",
            u'Group for a Europe of Democracies and Diversities': u'EDD',
            u'Group of the European Liberal Democrat and Reform Party': u'ELDR',
            u'Group of the European Liberal, Democrat and Reform Party': u'ELDR',
            u'Group indépendence/Démocratie': [u'ID',u'INDDEM', u'IND/DEM'],
            u'Independence/Democracy Group': [u'ID', u'INDDEM', u'IND/DEM'],
            u'Non-attached Members': [u'NA',u'NI'],
            u'Non-attached': [u'NA',u'NI'],
            u'Identity, Tradition and Sovereignty Group': u'ITS',
            u"Group of the European People's Party (Christian Democrats) and European Democrats": u'PPE-DE',
            u"Group of the European People's Party (Christian Democrats)": u'PPE',
            u"Group of the European People's Party (Christian-Democratic Group)": u"PPE",
            u'Group of the Party of European Socialists': u'PSE',
            u'Socialist Group in the European Parliament': u'PSE',
            u'Technical Group of Independent Members': u'TDI',
            u'Group indépendence/Démocratie': u'UEN',
            u'Union for a Europe of Nations Group': u'UEN',
            u'Europe of Nations Group (Coordination Group)': u'UEN',
            u'Union for Europe of the Nations Group': u'UEN',
            u'Group of the Greens / European Free Alliance': u'Verts/ALE',
            u'The Green Group in the European Parliament': u'Verts/ALE',
            u'Greens/EFA': u'Verts/ALE',
            u'Christian Democratic Group': u'CD',
            u'Christian Democratic Group': u'CD',
            u'European Conservatives': u'C',
            u'European Democrats': u'ED',
            u'European People\'s Party': u'EPP',
            u'Forza Europa': u'FE',
            u'European People\'s Party–European Democrats': u'EPP-ED',
            u'Socialist Group': u'S',
            u'Socialist Group': u'SOC',
            u'Party of European Socialists': u'PES',
            u'Progressive Alliance of Socialists and Democrats': u'S&D',
            u'Liberal Group': u'L',
            u'Liberal and Democratic Group': u'LD',
            u'Liberal and Democratic Reformist Group': u'LDR',
            u'European Liberal Democratic and Reform Party': u'ELDR',
            u'European Radical Alliance': u'ERA',
            u'Alliance of Liberals and Democrats for Europe': u'ALDE',
            u'European Democratic Union': u'UDE',
            u'European Democratic Union Group': u'UDE',
            u'European Progressive Democrats': u'EPD',
            u'European Democratic Alliance': u'EDA',
            u'Group Union for Europe': u'UFE',
            u'Union for Europe of the Nations': u'UEN',
            u'Rainbow Group': u'RBW',
            u'Rainbow Group': u'RBW',
            u'The Green Group': u'G',
            u'Communists and Allies': u'COM',
            u'Communist and Allies Group (SF, Ind. Sin.)': u'COM',
            u'European United Left': u'EUL',
            u'Left Unity': u'LU',
            u'European United Left': u'EUL',
            u'European United Left–Nordic Green Left': u'EUL/NGL',
            u'Technical Group of Independent Members - mixed group': u'TGI',
            u'Communist and Allies Group': u'COM',
            u"Rainbow Group: Federation of the Green-Alternative European Links, Agelev-Ecolo, the Danish People's Movement against Membership of the European Community and the European Free Alliance in the European Parliament": u'RBW',
            u'Group for the Technical Coordination and Defence of Indipendent Groups and Members': u'CDI',
            u'Technical Coordination and Defence of Independent Groups and Members': u'CDI',
            u'Forza Europa Group': u'FE',
            u'Christian-Democratic Group': u'CD',
            u"Christian-Democratic Group (Group of the European People's Party)": u'CD',
            u'European Conservative Group': u'C',
            u'Group of European Progressive Democrats': u'DEP',
            u'Europe of Nations and Freedom Group': u'ENF',
            }
GROUPIDS=[]
for item in GROUP_MAP.values():
    if type(item)==list:
        GROUPIDS.extend(item)
    else:
        GROUPIDS.append(item)

DELEGATIONS={
    "Armenia, Azerbaijan, Georgia": "AAG",
    "Bulgaria": "BULG",
    "Cyprus": "CYPR",
    "Czech Republic": "CZEC",
    "Afghanistan": "D-AF",
    "Delegation for relations with Afghanistan": "D-AF",
    "Delegation to the EU-Albania Stabilisation and Association Parliamentary Committee": "D-AL",
    "Delegation for relations with the Federative Republic of Brazil": "D-BR",
    "Belarus": "D-BY",
    "Delegation for relations with Belarus": "D-BY",
    "Canada": "D-CA",
    "Delegation for relations with Canada": "D-CA",
    "Delegation to the EU-Chile Joint Parliamentary Committee": "D-CL",
    "EU-Chile": "D-CL",
    "Delegation for relations with the People's Republic of China": "D-CN",
    "People's Republic of China": "D-CN",
    "EU-Croatia": "D-HR",
    "Delegation for relations with Israel": "D-IL",
    "Israel": "D-IL",
    "Delegation for relations with India": "D-IN",
    "India": "D-IN",
    "Delegation for relations with Iraq": "D-IQ",
    "Iraq": "D-IQ",
    "Delegation for relations with Iran": "D-IR",
    "Iran": "D-IR",
    "Delegation for relations with Japan": "D-JP",
    "Japan": "D-JP",
    "Delegation to the EU-Moldova Parliamentary Association Committee": "D-MD",
    "Moldova": "D-MD",
    "Delegation to the EU-Montenegro Stabilisation and Association Parliamentary Committee": "D-ME",
    "Delegation to the EU-former Yugoslav Republic of Macedonia Joint Parliamentary Committee": "D-MK",
    "EU-Former Yugoslav Republic of Macedonia": "D-MK",
    "Delegation to the EU-Mexico Joint Parliamentary Committee": "D-MX",
    "EU-Mexico": "D-MX",
    "Delegation to the EU-Serbia Stabilisation and Association Parliamentary Committee": "D-RS",
    "Delegation to the EU-Russia Parliamentary Cooperation Committee": "D-RU",
    "Russia": "D-RU",
    "Delegation to the EU-Turkey Joint Parliamentary Committee": "D-TR",
    "EU-Turkey": "D-TR",
    "Delegation to the EU-Ukraine Parliamentary Association Committee": "D-UA",
    "Ukraine": "D-UA",
    "Delegation for relations with the United States": "D-US",
    "United States": "D-US",
    "Delegation for relations with South Africa": "D-ZA",
    "South Africa": "D-ZA",
    "Delegation to the ACP-EU Joint Parliamentary Assembly": "DACP",
    "Andean Community": "DAND",
    "Delegation for relations with the countries of the Andean Community": "DAND",
    "Australia and New Zealand": "DANZ",
    "Delegation for relations with Australia and New Zealand": "DANZ",
    "Arab Peninsula": "DARP",
    "Delegation for relations with the Arab Peninsula": "DARP",
    "Delegation for relations with the countries of Southeast Asia and the Association of Southeast Asian Nations (ASEAN)": "DASE",
    "Southeast Asia, ASEAN": "DASE",
    "Central America": "DCAM",
    "Delegation for relations with the countries of Central America": "DCAM",
    "Cariforum – EU": "DCAR",
    "Delegation to the Cariforum-EU Parliamentary Committee": "DCAR",
    "Delegation to the EU-Kazakhstan, EU-Kyrgyzstan, EU-Uzbekistan and EU-Tajikistan Parliamentary Cooperation Committees and for relations with Turkmenistan and Mongolia": "DCAS",
    "Kazakhstan, Kyrgyzstan, Uzbekistan, Tajikistan, Turkmenistan and Mongolia": "DCAS",
    "Delegation for relations with Switzerland and Norway and to the EU-Iceland Joint Parliamentary Committee and the European Economic Area (EEA) Joint Parliamentary Committee": "DEEA",
    "Switzerland, Iceland and Norway and European Economic Area (EEA)": "DEEA",
    "Switzerland, Norway and the EU-Iceland and EEA JPCs": "DEEA",
    "Delegation to the Euronest Parliamentary Assembly": "DEPA",
    "Gulf States, Yemen": "DGUL",
    "Delegation for relations with the Korean Peninsula": "DKOR",
    "Korean Peninsula": "DKOR",
    "Delegation to the Euro-Latin American Parliamentary Assembly": "DLAT",
    "Delegation for relations with the Maghreb countries and the Arab Maghreb Union": "DMAG",
    "Maghreb": "DMAG",
    "Delegation for relations with the Mashreq countries": "DMAS",
    "Mashreq": "DMAS",
    "Delegation to the Parliamentary Assembly of the Union for the Mediterranean": "DMED",
    "Delegation to the UfM Parliamentary Assembly": "DMED",
    "Delegation for relations with Mercosur": "DMER",
    "Mercosur": "DMER",
    "Delegation for relations with the NATO Parliamentary Assembly": "DNAT",
    "NATO": "DNAT",
    "Delegation for relations with Palestine": "DPAL",
    "Delegation for relations with the Pan-African Parliament": "DPAP",
    "Pan-African Parliament": "DPAP",
    "Palestinian Legislative Council": "DPLC",
    "Delegation for relations with the countries of South Asia": "DSAS",
    "South Asia": "DSAS",
    "Armenia, Azerbaijan and Georgia": "DSCA",
    "Delegation to the EU-Armenia Parliamentary Partnership Committee, EU-Azerbaijan Parliamentary Cooperation Committee and the EU-Georgia Parliamentary Association Committee": "DSCA",
    "Albania, Bosnia and Herzegovina, Serbia, Montenegro, Kosovo": "DSEE",
    "Delegation for relations with Bosnia and Herzegovina, and Kosovo": "DSEE",
    "South-East Europe": "DSEE",
    "EEA": "EEA",
    "Estonia": "ESTO",
    "Hungary": "HUNG",
    "Latvia": "LATV",
    "Lithuania": "LITH",
    "Malta": "MALT",
    "Poland": "POLA",
    "Romania": "ROMA",
    "Russia": "RUSS",
    "South-East Europe": "SEE",
    "Switzerland, Iceland, Norway": "SIN",
    "Slovakia": "SLOA",
    "Slovenia": "SLOE",
    "Turkey": "TURK",
    "Ukraine, Moldova, Belarus": "UBM",
}

MEPS_ALIASES={
    u"GRÈZE, Catherine": ['GREZE', 'greze', 'Catherine Greze', 'catherine greze', u'Grčze', u'grcze'],
    u"SCOTTÀ, Giancarlo": ["SCOTTA'", "scotta'"],
    u"in 't VELD, Sophia": ["in't VELD", "in't veld", "IN'T VELD", "in'tveld", u'in `t Veld', u'in `t veld', u'in`tveld'],
    u"MORKŪNAITĖ-MIKULĖNIENĖ, Radvilė": [u"MORKŪNAITĖ Radvilė",u"morkūnaitė radvilė",u"radvilė morkūnaitė ",u"Radvilė MORKŪNAITĖ ", u"MORKŪNAITĖ", u"morkūnaitė"],
    u"MUSTIN-MAYER, Christine": ['Barthet-Mayer Christine', 'barthet-mayer christine', 'barthet-mayerchristine'],
    u"YÁÑEZ-BARNUEVO GARCÍA, Luis": [ u'Yañez-Barnuevo García', u'yañez-barnuevogarcía', u'Luis Yañez-Barnuevo García', u'luisyanez-barnuevogarcia'],
    u"ZAPPALA', Stefano": [ u'Zappalà', u'zappalà'],
    u"OBIOLS, Raimon": [u'Obiols i Germà', u'obiols i germà', u'ObiolsiGermà', u'obiolsigermà', u'Raimon Obiols i Germà', u'raimonobiolsigermà', u'OBIOLS i GERMÀ' ],
    u"CHATZIMARKAKIS, Jorgo": [u'Chatzimartakis', u'chatzimartakis'],
    u"XENOGIANNAKOPOULOU, Marilisa": [u'Xenagiannakopoulou', u'xenagiannakopoulou'],
    u"GRÄSSLE, Ingeborg": [u'Graessle', u'graessle'],
    u"VIRRANKOSKI, Kyösti": [u'Virrankoski-Itälä', u'virrankoski-itälä'],
    u"SARYUSZ-WOLSKI, Jacek": [u'Saryus-Wolski', u'saryus-wolski'],
    u"PITTELLA, Gianni": [u'Pitella', u'pitella'],
    u"EHLER, Christian": [u'Ehlert', u'ehlert', u'Jan Christian Ehler', u'janchristianehler'],
    u'COELHO, Carlos': ['Coehlo', u'coehlo', u'Coelho Carlo', u'coelho carlo', u'coelhocarlo'],
    u"Ó NEACHTAIN, Seán": [u"O'Neachtain", u"o'neachtain"],
    u"GALEOTE, Gerardo": [u'Galeote Quecedo', u'galeote quecedo',u'GaleoteQuecedo', u'galeotequecedo'],
    u'MARTIN, Hans-Peter': [u'Martin H.P.',u'martinh.p.', u'mmHans-Peter Martin', u'mmhans-petermartin' ],
    u'MARTIN, David': [u'D. Martin', u'd. martin', u'D.Martin', u'd.martin', u'Martin David W.', u'martindavidw.'],
    u'DÍAZ DE MERA GARCÍA CONSUEGRA, Agustín': [u'Díaz de Mera', u'díazdemera'],
    u'MEYER, Willy': [u'Meyer Pleite', u'meyer pleite', u'MeyerPleite', u'meyerpleite', u'Willy Meyer Pleite', u'willymeyerpleite'],
    u'ROBSAHM, Maria': [u'Carlshamre', u'carlshamre'],
    u'HAMMERSTEIN, David': [u'Hammerstein Mintz', u'hammersteinmintz'],
    u'AYUSO, Pilar': [u'Ayuso González', u'ayusogonzález'],
    u'PÖTTERING, Hans-Gert': [u'Poettering', u'poettering'],
    u'VIDAL-QUADRAS, Alejo': [u'Vidal-Quadras Roca', u'vidal-quadrasroca'],
    u'EVANS, Jill': [u'Evans Jillian', u'evansjillian'],
    u'BADIA i CUTCHET, Maria': [u'Badía i Cutchet', u'badíaicutchet', u'Badia Cutchet', u'badiacutchet'],
    u'AUCONIE, Sophie': [u'Briard Auconie', u'briardauconie', u'Sophie Briard Auconie', u'sophiebriardauconie'],
    u'BARSI-PATAKY, Etelka': [u'Barsi Pataky', u'barsipataky'],
    u'NEYNSKY, Nadezhda': [u'Mihaylova', u'mihaylova', u'Nadezhda Mihaylova', u'nadezhdamihaylova'],
    u'MOHÁCSI, Viktória': [u'Bernáthné Mohácsi', u'bernáthnémohácsi', u'bernathnemohacsi'],
    u'WOJCIECHOWSKI, Bernard': [u'Wojciechowski Bernard Piotr', u'wojciechowskibernardpiotr'],
    u'GARCÍA-MARGALLO Y MARFIL, José Manuel': [u'García-MarGállo y Marfil', u'garcía-margálloymarfil', u'García-Margallo', u'garcía-margallo'],
    u'ROGALSKI, Bogusław': [u'RoGálski', u'rogalski'],
    u'ROMEVA i RUEDA, Raül': [u'Romeva Rueda', u'romevarueda', u'Raьl Romeva i Rueda', u'raьlromevairueda'],
    u'JØRGENSEN, Dan': [u'Dan Jшrgensen', u'danjшrgensen', u'dan jшrgensen'],
    u'HÄFNER, Gerald': [u'Haefner', u'haefner', u'Gerald Haefner', u'geraldhaefner',u'gerald haefner'],
    u'EVANS, Robert': [u'Evans Robert J.E.', u'evansrobertj.e.'],
    u'LAMBSDORFF, Alexander Graf': [u'Lambsdorff Graf', u'lambsdorffgraf'],
    u'STARKEVIČIŪTĖ, Margarita': [u'Starkeviciūtė', u'starkeviciūtė'],
    u'KUŠĶIS, Aldis': [u'Kuškis', u'kuškis'],
    u'ŠŤASTNÝ, Peter': [u'Štastný', u'štastný'],
    u'FLAŠÍKOVÁ BEŇOVÁ, Monika': [u'Beňová', u'beňová'],
    u'ŢÎRLE, Radu': [u'Tîrle', u'tîrle'],
    u'HYUSMENOVA, Filiz Hakaeva': [u'Husmenova', u'husmenova'],
    u'LØKKEGAARD, Morten': [u'Morten Lokkegaard', u'mortenlokkegaard'],
    u"GOMES, Ana": [u'Ana Maria Gomes', u'ana maria gomes', u'anamariagomes'],
    u'(The Earl of) DARTMOUTH, William': [u'WilliAmendment (The Earl of) Dartmouth', u'williamendment (the earl of) dartmouth', u'williamendment(theearlof)dartmouth'],
    u'ESTARÀS FERRAGUT, Rosa': [u'Estarŕs Ferragut', u'estarŕs ferragut', u'estarŕsferragut'],
    u'GROSSETÊTE, Françoise': [u'Grossetęte', u'grossetęte'],
    u'SAVISAAR-TOOMAST, Vilja': [u'Vilja Savisaar', u'vilja savisaar', u'viljasavisaar'],
    u'HEDKVIST PETERSEN, Ewa' : [u'Hedkvist Pedersen', u'hedkvist pedersen', u'hedkvistpedersen'],
    u'JĘDRZEJEWSKA, Sidonia Elżbieta': [u'Sidonia Elżbieta Jędrzejewska', u'sidonia elżbieta jędrzejewska',u'sidoniaelżbietajędrzejewska',],
    u'TRAKATELLIS, Antonios': [u'M Trakatellis', u'm trakatellis', u'mtrakatellis'],
    u'FAVA, Claudio': [u'Giovanni Claudio Fava', u'giovanni claudio fava', u'giovanniclaudiofava'],
    u'TOMCZAK, Witold': [u'W. Tomczak', u'w. tomczak', u'w.tomczak'],
    u'PĘCZAK, Andrzej Lech': [u'A. Peczak', u'a. peczak', u'a.peczak'],
    u'SAKELLARIOU, Jannis': [u'Janis Sakellariou', u'janis sakellariou', u'janissakellariou'],
    u'GOROSTIAGA ATXALANDABASO, Koldo': [u'Koldo Gorostiaga', u'koldo gorostiaga', u'koldogorostiaga'],
    }

TITLES=[u'Sir',
        u'Lady',
        u'Baroness',
        u'Baron',
        u'Lord',
        u'Gräfin von',
        u'Earl',
        u'Duke',
        u'The Earl of',
        u'(The Earl of)',
        u'The Lord',
        u'Professor Sir']
