from objc_util import ObjCClass, uiimage_to_png, nsurl
import dialogs
import ui

UIImage = ObjCClass('UIImage')


def get_symbols(assets_list):
  symbols = []
  for symbol in assets_list:
    ins = UIImage.systemImageNamed_(symbol)
    if ins:
      png = uiimage_to_png(ins)
      data = {'title': str(symbol), 'image': ui.Image.from_data(png)}
    else:
      data = {'title': str(symbol)}
    symbols.append(data)
  return symbols


NSBundle = ObjCClass("NSBundle")
CUICatalog = ObjCClass('CUICatalog')

path = NSBundle.bundleWithPath_(
  '/System/Library/CoreServices/CoreGlyphs.bundle').bundlePath()
sf_assets = CUICatalog.alloc().initWithURL_error_(
  nsurl(str(path) + '/Assets.car'), None)

assets_list = sf_assets.allImageNames()
dialogs.list_dialog(items=get_symbols(assets_list))

