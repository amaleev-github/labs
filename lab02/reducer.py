#!/usr/bin/env python
import sys

import happybase
connection = happybase.Connection( 'node2.newprolab.com' )
connection.open()
table = connection.table( 'andrey.maleev' )

connection.create_table( 'andrey.maleev', {'data': dict(max_versions=4096, block_cache_enabled=True)} )

for line in sys.stdin:
    line_elements = line.strip().split("\t")
    if len(line_elements) != 3:
        continue
    elements_bad = False
    for element in line_elements:
        if element.strip() == "" or element.strip() == "-":
            elements_bad = True
            continue
    if elements_bad:
        continue
    uid, timestamp, url = line_elements
    print(line_elements)
    table.put(uid, {'data:url': url}, timestamp=int(float(timestamp)*1000))

#connection.disable_table('andrey.maleev')
#connection.delete_table('andrey.maleev')
connection.close()