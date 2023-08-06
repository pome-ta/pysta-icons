import json
from pathlib import Path
import plistlib

#_path = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_search.plist'

_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

coreGlyphsBundle_path = Path(_path)

plist_gene = coreGlyphsBundle_path.glob('*.plist')

plist_list = [{
  'name': f'{pl.name}',
  'data': plistlib.loads(pl.read_bytes())
} for pl in plist_gene]
'''
dumps_path = Path('./dumps').resolve()
for plst_name_dic in plist_list:
  _name = plst_name_dic['name']
  _data = plst_name_dic['data']
  dump = json.dumps(_data, ensure_ascii=False, indent=2)
  _tmp = Path(dumps_path, f'{_name}.json')
  _tmp.write_text(dump, encoding='utf-8')
'''

for plst_name_dic in plist_list:
  _name = plst_name_dic['name']
  _data = plst_name_dic['data']
  print(f'{_name}: {len(_data)}')

