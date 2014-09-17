#!/usr/bin/env python

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
import sys


def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = author(record)
    record = editor(record)
    record = journal(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    return record

with open('../bibtex/deeplearninggpuwithkeywords2014.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()
    bib_database = bibtexparser.loads(bibtex_str)
    #print(bib_database.entries)

    topics_to_titles_with_id = {}

    #import sys

    for entry in bib_database.entries:
        if entry.has_key('keyword'):
            keywords = [keyword.strip().lower() for keyword in entry['keyword'].split(',')]
            for keyword in set(keywords):
                if not topics_to_titles_with_id.has_key(keyword):
                    topics_to_titles_with_id[keyword] = []
                if entry.has_key('title') and entry.has_key('id'):
                    topics_to_titles_with_id[keyword].append((entry['id'],entry['title']))
            

    ignore_topics = ['','Misc']
    for topic in sorted(topics_to_titles_with_id):
        if not topic in ignore_topics:
            print topic, len(topics_to_titles_with_id[topic]), topics_to_titles_with_id[topic][:2]

    #parser = BibTexParser()
    #parser.customization = customizations
    #bib_database = bibtexparser.loads(bibtex_str, parser=parser)
    #print(bib_database.entries)

