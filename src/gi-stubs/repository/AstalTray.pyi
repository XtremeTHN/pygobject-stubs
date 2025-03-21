import typing

from gi.repository import GObject
from gi.repository import GdkPixbuf
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalTray"
_version: str = "0.1"

def category_to_nick() -> str: ...
def get_default() -> Tray: ...
def status_to_nick() -> str: ...

class Pixmap(GObject.GBoxed):
    """
    :Constructors:

    ::

        Pixmap()
    """
    width: int = ...
    height: int = ...
    bytes: bytes = ...
    bytes_length1: int = ...

class Tooltip(GObject.GBoxed):
    """
    :Constructors:

    ::

        Tooltip()
    """
    icon_name: str = ...
    icon: list[Pixmap] = ...
    icon_length1: int = ...
    title: str = ...
    description: str = ...

class Tray(GObject.Object):
    """
    :Constructors:

    ::

        Tray(**properties)
        new() -> AstalTray.Tray

    Object AstalTrayTray

    Signals from AstalTrayTray:
      item-added (gchararray)
      item-removed (gchararray)

    Properties from AstalTrayTray:
      items -> gpointer: items
        items

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        items: list[TrayItem]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: TrayPrivate = ...
    @staticmethod
    def get_default() -> Tray: ...
    def get_item(self, item_id: str) -> TrayItem: ...
    def get_items(self) -> list[TrayItem]: ...
    @classmethod
    def new(cls) -> Tray: ...
    

class TrayClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TrayClass()
    """
    parent_class: GObject.ObjectClass = ...
    item_added: typing.Callable[[Tray, str], None] = ...
    item_removed: typing.Callable[[Tray, str], None] = ...

class TrayItem(GObject.Object):
    """
    :Constructors:

    ::

        TrayItem(**properties)

    Object AstalTrayTrayItem

    Signals from AstalTrayTrayItem:
      changed ()
      ready ()

    Properties from AstalTrayTrayItem:
      title -> gchararray: title
        title
      category -> AstalTrayCategory: category
        category
      status -> AstalTrayStatus: status
        status
      tooltip -> AstalTrayTooltip: tooltip
        tooltip
      tooltip-markup -> gchararray: tooltip-markup
        tooltip-markup
      id -> gchararray: id
        id
      is-menu -> gboolean: is-menu
        is-menu
      icon-theme-path -> gchararray: icon-theme-path
        icon-theme-path
      icon-name -> gchararray: icon-name
        icon-name
      icon-pixbuf -> GdkPixbuf: icon-pixbuf
        icon-pixbuf
      gicon -> GIcon: gicon
        gicon
      item-id -> gchararray: item-id
        item-id
      menu-model -> GMenuModel: menu-model
        menu-model
      action-group -> GActionGroup: action-group
        action-group

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        title: str
        category: Category
        status: Status
        tooltip: Tooltip
        tooltip_markup: str
        id: str
        is_menu: bool
        icon_theme_path: str
        icon_name: str
        icon_pixbuf: GdkPixbuf.Pixbuf
        gicon: Gio.Icon
        item_id: str
        menu_model: Gio.MenuModel
        action_group: Gio.ActionGroup
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: TrayItemPrivate = ...
    def __init__(self, gicon: Gio.Icon = ...,
                 item_id: str = ...) -> None: ...
    def about_to_show(self) -> None: ...
    def activate(self, x: int, y: int) -> None: ...
    def get_action_group(self) -> typing.Optional[Gio.ActionGroup]: ...
    def get_category(self) -> Category: ...
    def get_gicon(self) -> Gio.Icon: ...
    def get_icon_name(self) -> str: ...
    def get_icon_pixbuf(self) -> GdkPixbuf.Pixbuf: ...
    def get_icon_theme_path(self) -> str: ...
    def get_id(self) -> str: ...
    def get_is_menu(self) -> bool: ...
    def get_item_id(self) -> str: ...
    def get_menu_model(self) -> typing.Optional[Gio.MenuModel]: ...
    def get_status(self) -> Status: ...
    def get_title(self) -> str: ...
    def get_tooltip(self) -> typing.Optional[Tooltip]: ...
    def get_tooltip_markup(self) -> str: ...
    def scroll(self, delta: int, orientation: str) -> None: ...
    def secondary_activate(self, x: int, y: int) -> None: ...
    def to_json_string(self) -> str: ...
    

class TrayItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TrayItemClass()
    """
    parent_class: GObject.ObjectClass = ...

class TrayItemPrivate(GObject.GPointer): ...

class TrayPrivate(GObject.GPointer): ...

class Category(GObject.GEnum):
    APPLICATION = 0
    COMMUNICATIONS = 1
    HARDWARE = 3
    SYSTEM = 2

class Status(GObject.GEnum):
    ACTIVE = 1
    NEEDS_ATTENTION = 2
    PASSIVE = 0


