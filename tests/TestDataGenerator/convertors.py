import json
import csv
import datetime
from xml.etree.ElementTree import Element

def func(x):
    return x + 1

def dtconvert(o):
        if isinstance(o, datetime.datetime or datetime.date):
            return o.__str__()

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

def out_csv(tdat, datf):
    keys = tdat[0].keys()
    with open(datf, 'w', newline='', encoding='utf-8') as fp:
        wrtr = csv.DictWriter(fp, keys)
        wrtr.writeheader()
        wrtr.writerows(tdat)

    #tdat.to_csv(fp, encoding='utf-8', index=False)

def out_json(tdat, datf):
    with open(datf, 'w', newline='', encoding='utf-8') as fp:
            json.dump(tdat, fp, default=dtconvert)        

