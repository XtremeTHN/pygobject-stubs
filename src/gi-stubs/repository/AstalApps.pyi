import typing

from gi.repository import GLib
from gi.repository import GObject
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalApps"
_version: str = "0.1"

class Application(GObject.Object):
    """
    :Constructors:

    ::

        Application(**properties)

    Object AstalAppsApplication

    Properties from AstalAppsApplication:
      app -> GDesktopAppInfo: app
        app
      frequency -> gint: frequency
        frequency
      name -> gchararray: name
        name
      entry -> gchararray: entry
        entry
      description -> gchararray: description
        description
      wm-class -> gchararray: wm-class
        wm-class
      executable -> gchararray: executable
        executable
      icon-name -> gchararray: icon-name
        icon-name
      keywords -> GStrv: keywords
        keywords
      categories -> GStrv: categories
        categories

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        app: GLib.DesktopAppInfo
        frequency: int
        name: str
        entry: str
        description: str
        wm_class: str
        executable: str
        icon_name: str
        keywords: list[str]
        categories: list[str]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ApplicationPrivate = ...
    def __init__(self, app: GLib.DesktopAppInfo = ...,
                 frequency: int = ...) -> None: ...
    def exact_match(self, term: str) -> Score: ...
    def fuzzy_match(self, term: str) -> Score: ...
    def get_app(self) -> GLib.DesktopAppInfo: ...
    def get_categories(self) -> list[str]: ...
    def get_description(self) -> str: ...
    def get_entry(self) -> str: ...
    def get_executable(self) -> str: ...
    def get_frequency(self) -> int: ...
    def get_icon_name(self) -> str: ...
    def get_key(self, key: str) -> str: ...
    def get_keywords(self) -> list[str]: ...
    def get_name(self) -> str: ...
    def get_wm_class(self) -> str: ...
    def launch(self) -> bool: ...
    def set_app(self, value: GLib.DesktopAppInfo) -> None: ...
    def set_frequency(self, value: int) -> None: ...
    

class ApplicationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationClass()
    """
    parent_class: GObject.ObjectClass = ...

class ApplicationPrivate(GObject.GPointer): ...

class Apps(GObject.Object):
    """
    :Constructors:

    ::

        Apps(**properties)
        new() -> AstalApps.Apps

    Object AstalAppsApps

    Properties from AstalAppsApps:
      show-hidden -> gboolean: show-hidden
        show-hidden
      list -> gpointer: list
        list
      min-score -> gdouble: min-score
        min-score
      name-multiplier -> gdouble: name-multiplier
        name-multiplier
      entry-multiplier -> gdouble: entry-multiplier
        entry-multiplier
      executable-multiplier -> gdouble: executable-multiplier
        executable-multiplier
      description-multiplier -> gdouble: description-multiplier
        description-multiplier
      keywords-multiplier -> gdouble: keywords-multiplier
        keywords-multiplier
      categories-multiplier -> gdouble: categories-multiplier
        categories-multiplier

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        show_hidden: bool
        list: list[Application]
        min_score: float
        name_multiplier: float
        entry_multiplier: float
        executable_multiplier: float
        description_multiplier: float
        keywords_multiplier: float
        categories_multiplier: float
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: AppsPrivate = ...
    def __init__(self, show_hidden: bool = ...,
                 min_score: float = ...,
                 name_multiplier: float = ...,
                 entry_multiplier: float = ...,
                 executable_multiplier: float = ...,
                 description_multiplier: float = ...,
                 keywords_multiplier: float = ...,
                 categories_multiplier: float = ...) -> None: ...
    def exact_query(self, search: typing.Optional[str] = None) -> list[Application]: ...
    def exact_score(self, search: str, a: Application) -> float: ...
    def fuzzy_query(self, search: typing.Optional[str] = None) -> list[Application]: ...
    def fuzzy_score(self, search: str, a: Application) -> float: ...
    def get_categories_multiplier(self) -> float: ...
    def get_description_multiplier(self) -> float: ...
    def get_entry_multiplier(self) -> float: ...
    def get_executable_multiplier(self) -> float: ...
    def get_keywords_multiplier(self) -> float: ...
    def get_list(self) -> list[Application]: ...
    def get_min_score(self) -> float: ...
    def get_name_multiplier(self) -> float: ...
    def get_show_hidden(self) -> bool: ...
    @classmethod
    def new(cls) -> Apps: ...
    def reload(self) -> None: ...
    def set_categories_multiplier(self, value: float) -> None: ...
    def set_description_multiplier(self, value: float) -> None: ...
    def set_entry_multiplier(self, value: float) -> None: ...
    def set_executable_multiplier(self, value: float) -> None: ...
    def set_keywords_multiplier(self, value: float) -> None: ...
    def set_min_score(self, value: float) -> None: ...
    def set_name_multiplier(self, value: float) -> None: ...
    def set_show_hidden(self, value: bool) -> None: ...
    

class AppsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AppsClass()
    """
    parent_class: GObject.ObjectClass = ...

class AppsPrivate(GObject.GPointer): ...

class Score(GObject.GBoxed):
    """
    :Constructors:

    ::

        Score()
    """
    name: int = ...
    entry: int = ...
    executable: int = ...
    description: int = ...
    keywords: int = ...
    categories: int = ...


