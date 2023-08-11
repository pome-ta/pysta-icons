from objc_util import ObjCClass, uiimage_to_png
import ui

import pdbg

UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')

_ps = 100.0
point_size = UIImageSymbolConfiguration.configurationWithPointSize_(_ps)

symbol_name = 'play'
symbol_name = 'cable.connector.horizontal'
symbol_name = 'cable.connector'

uiimage = UIImage.systemImageNamed_withConfiguration_(symbol_name, point_size)

to_png = uiimage_to_png(uiimage)
png_img = ui.Image.from_data(to_png, 2)

