import json
from pathlib import Path
import ui

json_path = Path('./dumps/symbol_order.plist.json')
json_text = json_path.read_text()


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    pass

