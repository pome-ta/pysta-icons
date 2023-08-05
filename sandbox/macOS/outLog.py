import json
from pathlib import Path
import plistlib

_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'
coreGlyphsBundle_path = Path(_path)


plist_gene = coreGlyphsBundle_path.glob('**/*.plist')
plist_list = [{
    'name': f'{pl.name}',
    'data': plistlib.loads(pl.read_bytes())
} for pl in plist_gene]


for plst_name_dic in plist_list:
  _name = plst_name_dic['name']
  _data = plst_name_dic['data']
  print(f'{_name}: {len(_data)}')
