import json
from pathlib import Path
import plistlib

#_path = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_search.plist'

_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

coreGlyphsBundle_path = Path(_path)

plist_gene = coreGlyphsBundle_path.glob('*.plist')
'''
plist_list = [{
  f'{pl.name}': plistlib.loads(pl.read_bytes())
} for pl in plist_gene]
'''

plist_list_dics = [plistlib.loads(pl.read_bytes()) for pl in plist_gene]

#[print(len(i)) for i in plist_list_dics]

test_dic = plist_list_dics[5]
#print(len(test_dic))
test_data = json.dumps(test_dic, ensure_ascii=False, indent=2)

print(test_data)

