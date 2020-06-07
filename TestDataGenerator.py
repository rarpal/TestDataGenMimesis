from mimesis.schema import Field, Schema
import json
import csv
import datetime
from xml.etree.ElementTree import Element
from pandas import DataFrame as pdf
import argparse

def dtconvert(o):
        if isinstance(o, datetime.datetime or datetime.date):
            return o.__str__()

def schflds(item):
    field = Field('en')
    dictkey = item[0]
    dictval = item[1]
    if "provider" in dictval:
        return ( dictkey, field(dictval["provider"],**dictval["kwargs"]))
    else:
        innerdict = dict()
        innerdict[dictkey] = dict(map(lambda i: schflds(i), dictval.items()))
        returntup = tuple(innerdict.items())
        return ( (returntup[0][0], returntup[0][1]) )

def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

def dict_to_xml_str(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
        parts.append('</{}>'.format(tag))
    return ''.join(parts)

def main(args):

    with open(args.schm, encoding='utf-8') as fp:
        insch = json.loads(fp.read())

    """ tdat = pdf()
    for r in range(args.rows):
        tdat = tdat.append(dict(map(lambda l: schflds(l), insch.items())), ignore_index=True) """

    tdat = [dict(map(lambda l: schflds(l), insch.items())) for r in range(args.rows)]

    if args.fmat=="csv":

        keys = tdat[0].keys()
        with open(args.datf, 'w', newline='', encoding='utf-8') as fp:
            wrtr = csv.DictWriter(fp, keys)
            wrtr.writeheader()
            wrtr.writerows(tdat)
            #tdat.to_csv(fp, encoding='utf-8', index=False)
    elif args.fmat=="json":

        with open(args.datf, 'w', newline='', encoding='utf-8') as fp:
            json.dump(tdat, fp, default=dtconvert)
    else:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test data", prog="TestDataGenerator.py")
    parser.add_argument("schm", metavar="<Schema Fle>", help="fully qualified schema file in json format", type=str)
    parser.add_argument("datf", metavar="<Data File>", help="fully qualified output test data file", type=str)
    parser.add_argument("fmat", metavar="<Format>", help="output test data file format as csv, json or xml", choices=['csv','json','xml'], type=str)
    parser.add_argument("-rows", metavar="<Number of rows>", help="Number of test data rows to generate", type=int, default=10)
    args = parser.parse_args()

    main(args)