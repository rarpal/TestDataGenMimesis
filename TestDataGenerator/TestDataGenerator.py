import argparse
import json
import generators
import convertors

def main(args):

    with open(args.schm, encoding='utf-8') as fp:
        insch = json.loads(fp.read())

    """ 
    tdat = pdf()
    for r in range(args.rows):
        tdat = tdat.append(dict(map(lambda l: schflds(l), insch.items())), ignore_index=True) 
    """

    tdat = [dict(map(lambda l: generators.schflds(l), insch.items())) for r in range(args.rows)]

    if args.fmat=="csv":
        convertors.out_csv(tdat, args.datf)
    
    elif args.fmat=="json":
        convertors.out_json(tdat, args.datf)

    else:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test data", prog="TestDataGenerator.py")
    parser.add_argument("schm", metavar="<Schema Fle>", help="fully qualified schema file in json format", type=str)
    parser.add_argument("datf", metavar="<Data File>", help="fully qualified output test data file", type=str)
    parser.add_argument("fmat", metavar="<Format>", help="output test data file format as csv, json or xml", choices=['csv','json','xml'], type=str)
    parser.add_argument("-rows", metavar="<Number of rows>", help="Number of test data rows to generate (defaults to 10)", type=int, default=10)
    args = parser.parse_args()

    main(args)