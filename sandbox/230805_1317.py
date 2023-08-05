from objc_util import ObjCClass, nsurl
#from objc_util import NSDictionary

import pdbg

NSBundle = ObjCClass('NSBundle')
#NSDictionary = ObjCClass('NSDictionary')

symbol_search_plist = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_search.plist'

#path = NSBundle.bundleWithPath_(symbol_search_plist).bundlePath()

#plist_dic = NSDictionary.new().initWithContentsOfFile_(symbol_search_plist)

#plist_dic = NSDictionary.alloc().initWithContentsOfURL_(nsurl(symbol_search_plist))

#plist_dic = NSDictionary.new().initWithContentsOfURL_(nsurl(symbol_search_plist))

#pdbg.state(NSDictionary.new())

#pdbg.state(NSBundle.mainBundle())

coreGlyphsBundle_path = '/System/Library/CoreServices/CoreGlyphs.bundle'

bundle = NSBundle.bundleWithPath_(coreGlyphsBundle_path).bundlePath()

pdbg.state(bundle)

