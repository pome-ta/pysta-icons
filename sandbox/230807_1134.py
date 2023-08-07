import json
from pathlib import Path
import ctypes

from objc_util import ObjCClass, ObjCInstance, c
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


def get_uiImage(named: str) -> ui.Image:
  pass


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    pass

