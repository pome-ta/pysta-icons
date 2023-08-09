from objc_util import ObjCClass
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.bg_color = 0.2

    self.variableValue = 0.3

    multicolor = UIImageSymbolConfiguration.configurationPreferringMulticolor()
    #speaker.wave.3
    name = 'touchid'
    #name = 'speaker.wave.3'
    self.img_obj = UIImage.systemImageNamed_variableValue_withConfiguration_(
      name, self.variableValue, multicolor)
    self.im_view = UIImageView.new()
    w = self.img_obj.size().width * 10
    h = self.img_obj.size().height * 10

    self.im_view.setSize_((w, h))
    self.im_view.setImage_(self.img_obj)

    self.wrap = ui.View()
    self.wrap.width = w
    self.wrap.height = h
    self.wrap.objc_instance.addSubview_(self.im_view)

    #pdbg.state(self.im_view.image())

    self.add_subview(self.wrap)

    self.sl = ui.Slider()
    self.sl.value = self.variableValue
    self.sl.action = self.sl_action
    self.add_subview(self.sl)

  def sl_action(self, sender):
    #print(sender.value)
    self.variableValue = sender.value
    multicolor = UIImageSymbolConfiguration.configurationPreferringMulticolor()

    #name = 'speaker.wave.3'
    name = 'touchid'
    self.img_obj = UIImage.systemImageNamed_variableValue_withConfiguration_(
      name, self.variableValue, multicolor)
    self.im_view.setImage_(self.img_obj)

  def layout(self):
    _, _, w, h = self.frame
    sl_w = w * 0.88
    self.sl.width = sl_w
    self.sl.x = (w / 2) - (sl_w / 2)
    self.sl.y = h * 0.6

    self.wrap.x = (w / 2) - (self.wrap.width / 2)
    self.wrap.y = (h / 2) - (self.wrap.height / 2) - self.wrap.height / 2


view = View()
view.present()

