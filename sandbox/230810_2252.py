from objc_util import ObjCClass, uiimage_to_png
import ui

import pdbg


UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


_ps = 64.0
point_size = UIImageSymbolConfiguration.configurationWithPointSize_(_ps)

conf = UIImageSymbolConfiguration.defaultConfiguration()

conf.configurationByApplyingConfiguration_(point_size)


#uiimage = UIImage.systemImageNamed_('play')

uiimage = UIImage.symbolImageNamed_('play')

#uiimage.imageWithConfiguration_(conf)
pdbg.state(uiimage)

to_png = uiimage_to_png(uiimage)
png_img = ui.Image.from_data(to_png, 2)

