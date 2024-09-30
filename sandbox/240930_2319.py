"""
note: 追加日時から、新規追加情報得られるかしら？
"""
import sys
from pathlib import Path
import plistlib
import json

executable = Path(sys.executable).parent
info_plist_path = Path(executable, 'Info.plist')
plist_bytes = info_plist_path.read_bytes()
plist = plistlib.loads(plist_bytes)
kwargs = {
  'indent': 1,
  'sort_keys': True,
  'ensure_ascii': False,
}

plist_json = json.dumps(plist, **kwargs)
print(plist_json)
