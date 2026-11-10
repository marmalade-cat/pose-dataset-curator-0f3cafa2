#!/usr/bin/env python3
"""Simple local CSV/JSON validator and provenance reporter.
Usage: python main.py file1.csv file2.json

No external dependencies.
"""
import sys, json, csv

def check_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return {'type':'csv','rows':0,'headers':[], 'consistent':True}
    headers = rows[0]
    consistent = all(len(r)==len(headers) for r in rows)
    return {'type':'csv','rows':len(rows)-1,'headers':headers,'consistent':consistent}

def check_json(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return {'type':'json','top_type':('array' if isinstance(data,list) else 'object'),'items':(len(data) if isinstance(data,list) else None)}

if __name__=='__main__':
    if len(sys.argv)<=1:
        print('Provide file paths to CSV or JSON files to validate.')
        sys.exit(1)
    for p in sys.argv[1:]:
        print('---', p)
        try:
            if p.lower().endswith('.csv'):
                r = check_csv(p)
                print('CSV rows:', r['rows'])
                print('Headers:', ', '.join(r['headers']))
                print('Consistent row lengths:', r['consistent'])
            elif p.lower().endswith('.json'):
                r = check_json(p)
                print('JSON top-level:', r['top_type'])
                if r['items'] is not None: print('Items:', r['items'])
            else:
                print('Unknown extension; try CSV or JSON')
        except Exception as e:
            print('Error reading file:', e)
