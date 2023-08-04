from pathlib import Path

#from objc_util import ObjCClass, nsurl

path = Path('/System/Library/CoreServices/CoreGlyphs.bundle')

path_list = [f'{_p}\n\n' for _p in path.glob('**/*')]
print(*path_list)

#/System/Library/CoreServices/CoreGlyphs.bundle/symbol_search.plist

