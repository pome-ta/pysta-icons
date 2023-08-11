from objc_util import ObjCClass, ObjCInstance, uiimage_to_png
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')

#uiimage = UIImage.systemImageNamed_('play').resizableImageWithCapInsets_((105.0, 100.0, 115.0, 110.0))

uiimage = UIImage.systemImageNamed_('play')
#uiimage = UIImage.systemImageNamed_('play')._imageWithSize_((100.0, 100.0))
'''
bottom
left
right
top
'''

c_bottom = uiimage.capInsets().bottom
c_left = uiimage.capInsets().left
c_right = uiimage.capInsets().right
c_top = uiimage.capInsets().top
#pdbg.state()

#pdbg.state(UIImage.new().init())
#uiimage.size = (100.0, 100.0)

#size = uiimage.size()

#pdbg.state(uiimage.symbolConfiguration().pointSizeForScalingWithTextStyle())
pdbg.state(UIImageSymbolConfiguration.defaultConfiguration())

to_png = uiimage_to_png(uiimage)
png_img = ui.Image.from_data(to_png, 2)

