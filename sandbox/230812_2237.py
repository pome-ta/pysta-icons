from io import BytesIO

from PIL import Image as ImageP

from objc_util import ObjCClass, uiimage_to_png
import ui

import pdbg

UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')

symbol_name = 'play'
symbol_name = 'cable.connector.horizontal'
symbol_name = 'cable.connector'
symbol_name = 'cloud.sun.rain.fill'

uisc = UIImageSymbolConfiguration

conf: UIImageSymbolConfiguration
conf = uisc.defaultConfiguration()

_ps = 512.0

_point_size = uisc.configurationWithPointSize_(_ps)
_color = uisc.configurationPreferringMulticolor()

conf = conf.configurationByApplyingConfiguration_(_point_size)
conf = conf.configurationByApplyingConfiguration_(_color)

uiimage = UIImage.systemImageNamed_withConfiguration_(symbol_name, conf)

uii_w = uiimage.size().width
uii_h = uiimage.size().height
asp = max(uii_w, uii_h)

png_bytes = uiimage_to_png(uiimage)

sq_size = 128
p_size = (uii_w * sq_size / asp, uii_h * sq_size / asp)

#a_img = ImageP.frombytes('RGBA',p_size,png_bytes)
a_img = ImageP.open(BytesIO(png_bytes))

r_w, r_h = p_size

thumbnail_img = a_img.copy()
thumbnail_img.thumbnail(p_size, resample=ImageP.LANCZOS, reducing_gap=3.0)
thumbnail_re = a_img.resize(list(map(int, p_size)))

png_img = ui.Image.from_data(png_bytes, 2)

