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
    self.icon_view_this = self.icon_view._objc_ptr
    pdbg.state(self.icon_view)


view = View()
view.present()

