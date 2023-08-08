from pathlib import Path
import plistlib

from objc_util import ObjCClass, ObjCInstance, uiimage_to_png
import ui

import pdbg

UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


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
play_symbol = symbol_order.search_name('play')
uiimage_objc = __UIImage_systemName_(play_symbol)

conf = UIImageSymbolConfiguration.defaultConfiguration()
pnt = UIImageSymbolConfiguration.configurationWithPointSize_(100.0)
conf = UIImageSymbolConfiguration.configurationWithPointSize_(pnt)

#pdbg.state(UIImageSymbolConfiguration)
class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.im_view = ui.ImageView()
    self.im_view.bg_color = 'maroon'
    #self.im_view.size_to_fit()
    self.im_view.width = 200

    self.res = uiimage_objc.imageByApplyingSymbolConfiguration(conf)

    self.img_data = uiimage_to_png(self.res)
    self.img_png_data = ui.Image.from_data(self.img_data)
    self.im_view.image = self.img_png_data

    self.im_view.size_to_fit()

    self.add_subview(self.im_view)


view = View()
view.present()

