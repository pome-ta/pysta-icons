from objc_util import ObjCClass, ObjCInstance, uiimage_to_png
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')

#uiimage = UIImage.systemImageNamed_('play').resizableImageWithCapInsets_((105.0, 100.0, 115.0, 110.0))

uiimage = UIImage.systemImageNamed_('play')

#pdbg.state(ObjCInstance(uiimage.CGImage()))

#reimg = uiimage.resizableImageWithCapInsets_resizingMode_((5.0,10.0,5.0,20.0), 0)

#pdbg.state(UIImage.new())

to_png = uiimage_to_png(uiimage)
png_img = ui.Image.from_data(to_png)

