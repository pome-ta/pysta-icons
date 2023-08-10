from objc_util import ObjCClass, ObjCInstance, uiimage_to_png
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')

#uiimage = UIImage.systemImageNamed_('play').resizableImageWithCapInsets_((105.0, 100.0, 115.0, 110.0))

uiimage = UIImage.systemImageNamed_('play')
#uiimage = UIImage.systemImageNamed_('play')._imageWithSize_((100.0, 100.0))


pdbg.state(uiimage.content().vectorGlyph())


#pdbg.state(UIImage.new().init())
#uiimage.size = (100.0, 100.0)

#size = uiimage.size()

#pdbg.state(size)


to_png = uiimage_to_png(uiimage)
png_img = ui.Image.from_data(to_png, 2)

