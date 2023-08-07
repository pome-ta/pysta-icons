import json
from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, uiimage_to_png
import dialogs
import ui

UIImage = ObjCClass('UIImage')

json_path = Path('./dumps/symbol_order.plist.json')
json_text = json_path.read_text()
json_obj = json.loads(json_text)


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


#symbols = [__UIImage_systemName_(_name) for _name in json_obj]

items = [set_items(_name) for _name in json_obj]
dialogs.list_dialog(title=f'{len(items)}', items=items)
'''
aaa = get_png_bytes('doc.badge.gearshape.fill')


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    pass
'''

