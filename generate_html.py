#!/usr/bin/env python3
import json

TEMPLATE_PATH = 'template.html'
DATA_PATH     = 'url_oilGas_feeds.json'
OUTPUT_PATH   = 'index.html'

def main():
    # Load the full JSON, then extract the "list" array
    with open(DATA_PATH) as f:
        obj = json.load(f)
    items = obj.get('list', [])

    # Read the template, inject only the list array
    with open(TEMPLATE_PATH) as f:
        template = f.read()
    html = template.format(data_json=json.dumps(items))

    # Write out the finished page
    with open(OUTPUT_PATH, 'w') as f:
        f.write(html)

   # print("✅ index.html generated")

if __name__ == '__main__':
    main()