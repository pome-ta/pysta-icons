from pathlib import Path
import plistlib

from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

#import pdbg

UIView = ObjCClass('UIView')
UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')
UIImage = ObjCClass('UIImage')
UIColor = ObjCClass('UIColor')


def get_order_list():
  CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

  symbol_order_path = 'symbol_order.plist'
  symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

  order_list = plistlib.loads(symbol_order_bundle.read_bytes())
  return order_list


all_items = get_order_list()
#all_items.sort()


class TableViewController(object):

  def __init__(self, items: list = [], cell_identifier: str = 'cell'):
    self.items = items
    self.cell_identifier = cell_identifier
    self._table_dataSource: 'UITableViewDataSource'
    self._table_delegate: 'UITableViewDelegate'

    self.init_table_dataSource()
    self.init_table_delegate()

  @property
  def table_dataSource(self):
    return self._table_dataSource

  @property
  def table_delegate(self):
    return self._table_delegate

  def init_table_dataSource(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return len(self.items)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
        self.cell_identifier, indexPath)

      cell_text = self.items[indexPath.row()]
      cell_image = UIImage.systemImageNamed_(cell_text)

      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines_(1)
      content.setText_(cell_text)
      content.setImage_(cell_image)

      cell.setContentConfiguration_(content)

      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
      return 1

    # --- `UITableViewDataSource` set up
    _methods = [
      tableView_numberOfRowsInSection_,
      tableView_cellForRowAtIndexPath_,
      numberOfSectionsInTableView_,
    ]
    _protocols = [
      'UITableViewDataSource',
    ]

    create_kwargs = {
      'name': 'table_dataSource',
      'methods': _methods,
      'protocols': _protocols,
    }

    table_dataSource = create_objc_class(**create_kwargs)
    self._table_dataSource = table_dataSource.new()

  def init_table_delegate(self):
    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      indexPath = ObjCInstance(_indexPath)
      print(indexPath)
      item = self.items[indexPath.row()]
      print(item)

    # --- `UITableViewDelegate` set uo
    _methods = [
      tableView_didSelectRowAtIndexPath_,
    ]
    _protocols = [
      'UITableViewDelegate',
    ]

    create_kwargs = {
      'name': 'table_delegate',
      'methods': _methods,
      'protocols': _protocols,
    }

    table_delegate = create_objc_class(**create_kwargs)
    self._table_delegate = table_delegate.new()


class ObjcControlView(object):

  def __init__(self):
    self.view = UIView.new()
    self.table_view = UITableView.new()

    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))
    self.cell_identifier = 'cell'

    self.controllers = TableViewController(all_items, self.cell_identifier)

    self.viewDidLoad()
    self.view.addSubview_(self.table_view)

  def init_UITableView(self):
    # [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
    '''
    0 : UITableViewStylePlain
    1 : UITableViewStyleGrouped
    2 : UITableViewStyleInsetGrouped
    '''
    self.table_view.initWithFrame_style_(self.tmp_frame, 0)

    # xxx: 2度`frame` 指定している。`init` からは`frame` が反映されないため -> `setAutoresizingMask_` がいい感じにならない
    self.table_view.setFrame_(self.tmp_frame)
    self.table_view.registerClass_forCellReuseIdentifier_(
      UITableViewCell, self.cell_identifier)

    self.table_view.setDataSource_(self.controllers.table_dataSource)
    self.table_view.setDelegate_(self.controllers.table_delegate)

    self.table_view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.table_view.autorelease()

  def viewDidLoad(self):
    self.view.setFrame_(self.tmp_frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()

    self.init_UITableView()

  def layout(self):
    pass


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

    self.objc_view = ObjcControlView()
    self.objc_instance.addSubview_(self.objc_view.view)

  def layout(self):
    pass

if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()
