from objc_util import ObjCClass
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.bg_color = 0.4

    self.variableValue = 0.3

    multicolor = UIImageSymbolConfiguration.configurationPreferringMulticolor()
    #speaker.wave.3
    #touchid
    name = 'speaker.wave.3'
    self.img_obj = UIImage.systemImageNamed_variableValue_withConfiguration_(
      name, self.variableValue, multicolor)
    self.im_view = UIImageView.new()
    w = self.img_obj.size().width
    h = self.img_obj.size().height

    self.im_view.setSize_((w * 10, h * 10))
    self.im_view.setImage_(self.img_obj)
    pdbg.state(self.im_view.image())

    self.objc_instance.addSubview_(self.im_view)

    self.sl = ui.Slider()
    self.sl.value = self.variableValue
    self.sl.action = self.sl_action
    self.add_subview(self.sl)

  def sl_action(self, sender):
    #print(sender.value)
    self.variableValue = sender.value

  def layout(self):
    _, _, w, h = self.frame
    sl_w = w * 0.88
    self.sl.width = sl_w
    self.sl.x = (w / 2) - (sl_w / 2)
    self.sl.y = h * 0.5


view = View()
view.present()


systemImageNamed:variableValue:withConfiguration:
imageNamed:inBundle:variableValue:withConfiguration:
Creates an image by using the nam
