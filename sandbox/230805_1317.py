from pathlib import Path
import plistlib

coreGlyphsBundle_path = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_search.plist'

path = Path(coreGlyphsBundle_path)

a = path.read_bytes()
aa = plistlib.loads(a)
