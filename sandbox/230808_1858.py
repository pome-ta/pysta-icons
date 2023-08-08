from pathlib import Path
import plistlib

from objc_util import ObjCClass, ObjCInstance, uiimage_to_png
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')

#pdbg.state(UIImageSymbolConfiguration)


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
  multicolor = UIImageSymbolConfiguration.configurationPreferringMulticolor()
  #_img.configuration().configurationByApplyingConfiguration_(multicolor)
  #pdbg.state(_img.configuration())
  _img = UIImage.systemImageNamed_withConfiguration_(_symbol_name, multicolor)

  return _img


symbol_order = SymbolOrder()
#play_symbol = symbol_order.search_name('checkmark.circle.trianglebadge.exclamationmark')

play_symbol = symbol_order.search_name('cloud.sun.rain.fill')

#cloud.sun.fill
uiimage_objc = __UIImage_systemName_(play_symbol)

conf = UIImageSymbolConfiguration.defaultConfiguration()
pnt = UIImageSymbolConfiguration.configurationWithPointSize_(100.0)
#conf = UIImageSymbolConfiguration.configurationWithPointSize_(pnt)

#pdbg.state(UIImageSymbolConfiguration)

#pdbg.state(UIImageView.alloc().initWithSize_((120.0, 24.0)))

#pdbg.state(UIImage)


def resize_icon(uiimage):
  _size = (220.5, 324.1)
  im_view = UIImageView.new()  #.alloc().initWithSize_(_size)
  #pdbg.state(uiimage)
  w = uiimage.size().width
  h = uiimage.size().height

  im_view.setSize_((w * 10, h * 10))
  im_view.setImage_(uiimage)
  return im_view


aimim = resize_icon(uiimage_objc)
#pdbg.state(aimim)


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.bg_color = 0.5
    self.im_view = ui.ImageView()
    self.im_view.bg_color = 'maroon'
    #self.im_view.size_to_fit()
    self.im_view.width = 200

    #self.res = uiimage_objc.imageByApplyingSymbolConfiguration(conf)
    #self.img_data = uiimage_to_png(self.res)
    #pdbg.state(uiimage_objc.size())
    #uiimage_objc.size = (50.0, 50.0)
    #height
    #width
    uiimage_objc.size.width = 50.0

    #pdbg.state(uiimage_objc)

    self.img_data = uiimage_to_png(uiimage_objc)
    self.img_png_data = ui.Image.from_data(self.img_data)
    self.im_view.image = self.img_png_data

    self.im_view.size_to_fit()
    self.objc_instance.addSubview_(aimim)

    #self.add_subview(self.im_view)


view = View()
view.present()

