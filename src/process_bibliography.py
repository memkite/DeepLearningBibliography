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

    id_to_entry = {}

    topics_to_titles_with_id = {}

    #import sys

    for entry in bib_database.entries:
        if entry.has_key('id'): # probably unecessary, but for now
            id_to_entry[entry['id']] = entry

        if entry.has_key('keyword'):
            keywords = [keyword.strip().lower() for keyword in entry['keyword'].split(',')]
            for keyword in set(keywords):
                if not topics_to_titles_with_id.has_key(keyword):
                    topics_to_titles_with_id[keyword] = []
                if entry.has_key('title') and entry.has_key('id'):
                    topics_to_titles_with_id[keyword].append((entry['id'],entry['title']))
            

    ignore_topics = ['','misc']
    topic_line_len = 0

    # a) create hyperlinks to topics
    for topic in sorted(topics_to_titles_with_id):
        topic = topic.lower().strip()
        if not topic.lower().strip() in ignore_topics:
            topic_line_len += len(topic) + 3
            if topic_line_len > 80:
                print "<br>"
            spaceless_topic = topic.replace(' ','_')
            print '''<a href="#%s">[%s]</a> ''' % (spaceless_topic, topic)
            #print topic, len(topics_to_titles_with_id[topic]), topics_to_titles_with_id[topic][:2]

    # b) create list of titles per topic
    for topic in sorted(topics_to_titles_with_id):
        print 
        topic = topic.lower().strip()
        if not topic in ignore_topics:
            spaceless_topic = topic.replace(' ','_')
            print '''<h2><a name="%s"></a>%s''' % (spaceless_topic, topic.title())
            print "<ol>"
            for (pubid,title) in topics_to_titles_with_id[topic]:
                print u'''<li><a href="#%s">%s</a> ''' % (pubid, title.encode('utf-8'))
            print "</ol>"
    
    # c) create bibtex list at the end, that get pointed to by 2
    for pubid in sorted(id_to_entry):
        print '''<a name="%s"></a>''' % (pubid)

    #parser = BibTexParser()
    #parser.customization = customizations
    #bib_database = bibtexparser.loads(bibtex_str, parser=parser)
    #print(bib_database.entries)

