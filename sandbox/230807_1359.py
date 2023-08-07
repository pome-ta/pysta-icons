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

    self.f_img_v = ui.ImageView()
    self.f_image = ui.Image.named('iob:arrow_down_a_256')
    #self.f_img_v.image = self.f_image

    #pdbg.all(ObjCInstance(self.f_image))
    self.ins = ObjCInstance(self.f_image)
    #pdbg.state(self.ins.images())
    #pdbg.state(ObjCInstance(self.ins.imageRef()))
    #pdbg.state(self.ins.imageAsset())
    pdbg.state(ObjCInstance(self.ins._isNamed()))

    
    
    
    
    self.aaa = ui.Image.named('doc.badge.gearshape.fill')

    self.add_subview(self.icon_view)
    self.add_subview(self.f_img_v)

  def layout(self):
    self.icon_view.width = 400
    self.icon_view.height = 400


view = View()
view.present()

