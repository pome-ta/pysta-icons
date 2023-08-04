from objc_util import ObjCClass, nsurl
import ui

from pprint import pprint


def create_icons():
  Catalog = ObjCClass('CUICatalog').alloc()
  NSBundle = ObjCClass('NSBundle')
  path = nsurl(str(NSBundle.mainBundle().bundlePath()) + '/Assets.car')
  assets = Catalog.initWithURL_error_(path, None)
  all_names = assets.allImageNames()
  named = ui.Image.named
  return [named(str(i)) for i in all_names]


class DataSource:

  def __init__(self):
    self.all_icons = create_icons()

  def tableview_number_of_rows(self, tv, section):
    return len(self.all_icons)

  def tableview_cell_for_row(self, tv, section, row):
    cell = ui.TableViewCell()
    icon = self.all_icons[row]

    img_view = ui.ImageView(frame=(24, 6.4, 32, 32))
    img_view.image = icon
    img_view.content_mode = 1
    cell.content_view.add_subview(img_view)

    label = ui.Label(frame=(80, 0, cell.content_view.bounds.w, 32))
    label.text = icon.name
    cell.content_view.add_subview(label)

    sub_label = ui.Label(frame=(label.frame))
    sub_label.y += 16
    sub_label.font = ('<System>', 10)
    sub_label.text_color = '#555'
    sub_label.text = f'Size: {icon.size}'
    cell.content_view.add_subview(sub_label)

    return cell


class TVDelegate:

  def tableview_did_select(self, tv, section, row):
    icon = tv.data_source.all_icons[row]
    DetailView(icon)


class DetailView(ui.View):

  def __init__(self, icon):
    w_size = ui.get_window_size()
    self._h2, self._w2 = w_size / 2
    self.look_view(icon)
    self.present(hide_title_bar=True)

  def image_under(self):
    # todo: とりまサイズ
    _width = self._w2 * 1.28
    _height = self._h2 * 1.28
    under = ui.View()
    under.bg_color = 'silver'
    under.width = under.height = min(_width, _height)

    under.x = self._h2 - (under.height * .5)
    under.y = self._w2 - (under.width * .925)
    under.corner_radius = 8
    self.add_subview(under)
    return under

  def look_view(self, icon):
    base = self.image_under()
    _, _, b_w, b_h = base.frame
    i_view = ui.ImageView()
    i_view.image = icon
    i_view.content_mode = 1
    i_view.width = b_w * .925
    i_view.height = b_h * .925
    i_view.x = (b_w * .5) - (i_view.width * .5)
    i_view.y = (b_h * .5) - (i_view.height * .5)
    base.add_subview(i_view)

  def set_name(self):
    label = ui.Label()
    label.bg_color = 'red'
    label.text = 'Name: Hoge_Huga_Piyo'
    label.flex = 'W'
    return label


class MainView(ui.View):

  def __init__(self):
    self.table_view = ui.TableView()
    self.table_view.data_source = DataSource()
    self.table_view.delegate = TVDelegate()
    self.table_view.flex = 'WH'
    self.add_subview(self.table_view)

    total = len(self.table_view.data_source.all_icons)

    self.name = f'Assets.car icons @{total}'


mv = MainView()
mv.present()

