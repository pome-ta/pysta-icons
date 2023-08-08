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
  #_img = UIImage.systemImageNamed_(_symbol_name)
  multicolor = UIImageSymbolConfiguration.configurationPreferringMulticolor()
  #_img.configuration().configurationByApplyingConfiguration_(multicolor)
  #pdbg.state(_img.configuration())
  #_img = UIImage.systemImageNamed_withConfiguration_(_symbol_name, multicolor)
  #pdbg.state(_img.configuration())
  _img = UIImage.systemImageNamed_variableValue_withConfiguration_(_symbol_name, 0.1, multicolor)
  #_img._imageWithVariableValue_(_symbol_name, 0.5)
  pdbg.state(_img)

  return _img


symbol_order = SymbolOrder()
#play_symbol = symbol_order.search_name('checkmark.circle.trianglebadge.exclamationmark')

#play_symbol = symbol_order.search_name('cloud.sun.rain.fill')

#play_symbol = symbol_order.search_name('speaker.wave.2.circle.fill')


play_symbol = symbol_order.search_name('touchid')



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
    self.bg_color = 0.4
    
    self.variableValue = 0.0
    
    multicolor = UIImageSymbolConfiguration.configurationPreferringMulticolor()
    self.img_obj = UIImage.systemImageNamed_variableValue_withConfiguration_('touchid', self.variableValue, multicolor)
    
    
    self.objc_instance.addSubview_(self.img_obj)
    
    self.sl = ui.Slider()
    self.add_subview(self.sl)

  def layout(self):
    _, _, w, h = self.frame
    sl_w = w *0.88
    self.sl.width = sl_w
    self.sl.x = (w/2) - (sl_w/2)
    self.sl.y = h * 0.5


view = View()
view.present()

