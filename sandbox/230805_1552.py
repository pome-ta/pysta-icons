from pathlib import Path
import plistlib

#_path = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_search.plist'

_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

coreGlyphsBundle_path = Path(_path)

al = list(coreGlyphsBundle_path.glob('*.plist'))

