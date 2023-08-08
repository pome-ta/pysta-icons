from pathlib import Path
import plistlib

from objc_util import ObjCClass, ObjCInstance, uiimage_to_png

import ui

UIImage = ObjCClass('UIImage')


class SymbolOrder:
  """
  現在意味がないclass
  """

  def __init__(self):
    _path = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_order.plist'
    _symbol_order_bundle = Path(_path)
    self.order_list = plistlib.loads(_symbol_order_bundle.read_bytes())

  def search_name(self, name: str) -> str:
    if name in self.order_list:
      return self.order_list[self.order_list.index(name)]
    return None

  def search_names(self, names: list) -> list[str]:
    print(names)

  def get_all_items(self):
    return self.order_list


def __UIImage_systemName_(_symbol_name: str) -> ObjCClass:
  _img = UIImage.systemImageNamed_(_symbol_name)
  return _img


def set_items(symbol_name: str) -> dict:
  _uiimage = __UIImage_systemName_(symbol_name)
  _img_bytes = uiimage_to_png(_uiimage)
  img = ui.Image.from_data(_img_bytes)
  return {'title': symbol_name, 'image': img}


# xxx: 後から作りたいから、UIImage と一緒に作らない
def get_png_bytes(named: str) -> bytes:
  ui_image = __UIImage_systemName_(named)
  png_data = uiimage_to_png(ui_image)
  return png_data


symbol_order = SymbolOrder()
aaa = symbol_order.search_name('play')

