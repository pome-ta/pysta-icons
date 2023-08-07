import json
from pathlib import Path

from objc_util import ObjCClass, ObjCInstance
import ui

import pdbg

UIImage = ObjCClass('UIImage')

icon_obj = UIImage.systemImageNamed_('doc.badge.gearshape.fill')


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    #self.this = ObjCInstance(self._objc_ptr)
    #pdbg.state(self.this)
    self.icon_view = ui.ImageView()
    self.icon_view.bg_color = 'maroon'
    self.icon_view_this = ObjCInstance(self.icon_view._objc_ptr)
    self.icon_view_this.image = icon_obj
    #pdbg.state(self.icon_view_this)
    self.add_subview(self.icon_view)

  def layout(self):
    self.icon_view.width = 400
    self.icon_view.height = 400


view = View()
view.present()

