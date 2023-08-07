import json
from pathlib import Path
import ctypes

from objc_util import ObjCClass, ObjCInstance, c
import ui

UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


def get_UIImagePNGRepresentation():
  _UIImagePNGRepresentation = c.UIImagePNGRepresentation


json_path = Path('./dumps/symbol_order.plist.json')
json_text = json_path.read_text()
json_obj = json.loads(json_text)


def get_uiImage(named: str) -> ui.Image:
  pass


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    pass


a = ui.Image

