import json
from pathlib import Path
import ctypes

from objc_util import ObjCClass, ObjCInstance, uiimage_to_png, nsdata_to_bytes, c
import ui


def get_UIImagePNGRepresentation():
  _UIImagePNGRepresentation = c.UIImagePNGRepresentation
  _UIImagePNGRepresentation.argtypes = [ctypes.c_void_p]
  _UIImagePNGRepresentation.restype = ctypes.c_void_p
  return _UIImagePNGRepresentation


UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')

UIImagePNGRepresentation = get_UIImagePNGRepresentation()

json_path = Path('./dumps/symbol_order.plist.json')
json_text = json_path.read_text()
json_obj = json.loads(json_text)


def UIImage_systemName_(named: str) -> ObjCClass:
  _img = UIImage.systemImageNamed_(named)
  return _img


def get_image_data(named: str) -> ui.ImageContext:
  ui_image = UIImage_systemName_(named)
  conf = UIImageSymbolConfiguration.defaultConfiguration()

  _png_obj = UIImagePNGRepresentation(ui_image)
  _png_instance = ObjCInstance(_png_obj)
  png_data = nsdata_to_bytes(_png_instance)
  return png_data, uiimage_to_png(ui_image)


bd, pd = get_image_data('doc.badge.gearshape.fill')

sbd = str(bd)
spd = str(pd)

print(sbd == spd)


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    pass

