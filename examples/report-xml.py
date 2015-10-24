#!/usr/bin/env python3

from lxml import etree

filename = 'intergalacticfm.xml'
datafile = etree.parse(filename)
schema_doc = etree.parse('../channels.xsd')
schema = etree.XMLSchema(schema_doc)
if not schema.validate(datafile):
    print('ERROR: {} does not validate against schema'.format(filename))
    exit(1)

channels = datafile.getroot()
print('channels:'.format(filename))
for channel in channels:
    print('  {} id: {}'.format(channel.tag, channel.attrib['id']))
    for detail in channel:
        if detail.tag[-3:] == 'pls':
            print('    {} format:{} {}'.format(
                detail.tag, detail.attrib['format'], detail.text))
        else:
            print('    {}: {}'.format(detail.tag, detail.text))
