from mimesis.schema import Field, Schema
import datetime
#from pandas import DataFrame as pdf

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

