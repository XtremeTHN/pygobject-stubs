import typing

from gi.repository import GObject
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalHyprland"
_version: str = "0.1"

def get_default() -> Hyprland: ...

class Bind(GObject.Object):
    """
    :Constructors:

    ::

        Bind(**properties)
        new() -> AstalHyprland.Bind

    Object AstalHyprlandBind

    Properties from AstalHyprlandBind:
      locked -> gboolean: locked
        locked
      mouse -> gboolean: mouse
        mouse
      release -> gboolean: release
        release
      repeat -> gboolean: repeat
        repeat
      long-press -> gboolean: long-press
        long-press
      non-consuming -> gboolean: non-consuming
        non-consuming
      has-description -> gboolean: has-description
        has-description
      modmask -> gint64: modmask
        modmask
      submap -> gchararray: submap
        submap
      key -> gchararray: key
        key
      keycode -> gint64: keycode
        keycode
      catch-all -> gboolean: catch-all
        catch-all
      description -> gchararray: description
        description
      dispatcher -> gchararray: dispatcher
        dispatcher
      arg -> gchararray: arg
        arg

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        locked: bool
        mouse: bool
        release: bool
        repeat: bool
        long_press: bool
        non_consuming: bool
        has_description: bool
        modmask: int
        submap: str
        key: str
        keycode: int
        catch_all: bool
        description: str
        dispatcher: str
        arg: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: BindPrivate = ...
    def __init__(self, locked: bool = ...,
                 mouse: bool = ...,
                 release: bool = ...,
                 repeat: bool = ...,
                 long_press: bool = ...,
                 non_consuming: bool = ...,
                 has_description: bool = ...,
                 modmask: int = ...,
                 submap: str = ...,
                 key: str = ...,
                 keycode: int = ...,
                 catch_all: bool = ...,
                 description: str = ...,
                 dispatcher: str = ...,
                 arg: str = ...) -> None: ...
    def get_arg(self) -> str: ...
    def get_catch_all(self) -> bool: ...
    def get_description(self) -> str: ...
    def get_dispatcher(self) -> str: ...
    def get_has_description(self) -> bool: ...
    def get_key(self) -> str: ...
    def get_keycode(self) -> int: ...
    def get_locked(self) -> bool: ...
    def get_long_press(self) -> bool: ...
    def get_modmask(self) -> int: ...
    def get_mouse(self) -> bool: ...
    def get_non_consuming(self) -> bool: ...
    def get_release(self) -> bool: ...
    def get_repeat(self) -> bool: ...
    def get_submap(self) -> str: ...
    @classmethod
    def new(cls) -> Bind: ...
    def set_arg(self, value: str) -> None: ...
    def set_catch_all(self, value: bool) -> None: ...
    def set_description(self, value: str) -> None: ...
    def set_dispatcher(self, value: str) -> None: ...
    def set_has_description(self, value: bool) -> None: ...
    def set_key(self, value: str) -> None: ...
    def set_keycode(self, value: int) -> None: ...
    def set_locked(self, value: bool) -> None: ...
    def set_long_press(self, value: bool) -> None: ...
    def set_modmask(self, value: int) -> None: ...
    def set_mouse(self, value: bool) -> None: ...
    def set_non_consuming(self, value: bool) -> None: ...
    def set_release(self, value: bool) -> None: ...
    def set_repeat(self, value: bool) -> None: ...
    def set_submap(self, value: str) -> None: ...
    

class BindClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BindClass()
    """
    parent_class: GObject.ObjectClass = ...

class BindPrivate(GObject.GPointer): ...

class Client(GObject.Object):
    """
    :Constructors:

    ::

        Client(**properties)
        new() -> AstalHyprland.Client

    Object AstalHyprlandClient

    Signals from AstalHyprlandClient:
      removed ()
      moved-to (AstalHyprlandWorkspace)

    Properties from AstalHyprlandClient:
      address -> gchararray: address
        address
      mapped -> gboolean: mapped
        mapped
      hidden -> gboolean: hidden
        hidden
      x -> gint: x
        x
      y -> gint: y
        y
      width -> gint: width
        width
      height -> gint: height
        height
      workspace -> AstalHyprlandWorkspace: workspace
        workspace
      floating -> gboolean: floating
        floating
      monitor -> AstalHyprlandMonitor: monitor
        monitor
      class -> gchararray: class
        class
      title -> gchararray: title
        title
      initial-class -> gchararray: initial-class
        initial-class
      initial-title -> gchararray: initial-title
        initial-title
      pid -> guint: pid
        pid
      xwayland -> gboolean: xwayland
        xwayland
      pinned -> gboolean: pinned
        pinned
      fullscreen -> AstalHyprlandFullscreen: fullscreen
        fullscreen
      fullscreen-client -> AstalHyprlandFullscreen: fullscreen-client
        fullscreen-client
      swallowing -> gchararray: swallowing
        swallowing
      focus-history-id -> gint: focus-history-id
        focus-history-id

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        address: str
        mapped: bool
        hidden: bool
        x: int
        y: int
        width: int
        height: int
        workspace: Workspace
        floating: bool
        monitor: Monitor
        title: str
        initial_class: str
        initial_title: str
        pid: int
        xwayland: bool
        pinned: bool
        fullscreen: Fullscreen
        fullscreen_client: Fullscreen
        swallowing: str
        focus_history_id: int
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ClientPrivate = ...
    def __init__(self, address: str = ...,
                 mapped: bool = ...,
                 hidden: bool = ...,
                 x: int = ...,
                 y: int = ...,
                 width: int = ...,
                 height: int = ...,
                 workspace: Workspace = ...,
                 floating: bool = ...,
                 monitor: Monitor = ...,
                 title: str = ...,
                 initial_class: str = ...,
                 initial_title: str = ...,
                 pid: int = ...,
                 xwayland: bool = ...,
                 pinned: bool = ...,
                 fullscreen: Fullscreen = ...,
                 fullscreen_client: Fullscreen = ...,
                 swallowing: str = ...,
                 focus_history_id: int = ...) -> None: ...
    def focus(self) -> None: ...
    def get_address(self) -> str: ...
    def get_class(self) -> str: ...
    def get_floating(self) -> bool: ...
    def get_focus_history_id(self) -> int: ...
    def get_fullscreen(self) -> Fullscreen: ...
    def get_fullscreen_client(self) -> Fullscreen: ...
    def get_height(self) -> int: ...
    def get_hidden(self) -> bool: ...
    def get_initial_class(self) -> str: ...
    def get_initial_title(self) -> str: ...
    def get_mapped(self) -> bool: ...
    def get_monitor(self) -> Monitor: ...
    def get_pid(self) -> int: ...
    def get_pinned(self) -> bool: ...
    def get_swallowing(self) -> str: ...
    def get_title(self) -> str: ...
    def get_width(self) -> int: ...
    def get_workspace(self) -> Workspace: ...
    def get_x(self) -> int: ...
    def get_xwayland(self) -> bool: ...
    def get_y(self) -> int: ...
    def kill(self) -> None: ...
    def move_to(self, ws: Workspace) -> None: ...
    @classmethod
    def new(cls) -> Client: ...
    def toggle_floating(self) -> None: ...
    

class ClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientClass()
    """
    parent_class: GObject.ObjectClass = ...

class ClientPrivate(GObject.GPointer): ...

class Hyprland(GObject.Object):
    """
    :Constructors:

    ::

        Hyprland(**properties)
        new() -> AstalHyprland.Hyprland

    Object AstalHyprlandHyprland

    Signals from AstalHyprlandHyprland:
      submap (gchararray)
      floating (AstalHyprlandClient, gboolean)
      event (gchararray, gchararray)
      minimize (AstalHyprlandClient, gboolean)
      urgent (AstalHyprlandClient)
      client-moved (AstalHyprlandClient, AstalHyprlandWorkspace)
      keyboard-layout (gchararray, gchararray)
      config-reloaded ()
      client-added (AstalHyprlandClient)
      client-removed (gchararray)
      workspace-added (AstalHyprlandWorkspace)
      workspace-removed (gint)
      monitor-added (AstalHyprlandMonitor)
      monitor-removed (gint)

    Properties from AstalHyprlandHyprland:
      monitors -> gpointer: monitors
        monitors
      workspaces -> gpointer: workspaces
        workspaces
      clients -> gpointer: clients
        clients
      focused-workspace -> AstalHyprlandWorkspace: focused-workspace
        focused-workspace
      focused-monitor -> AstalHyprlandMonitor: focused-monitor
        focused-monitor
      focused-client -> AstalHyprlandClient: focused-client
        focused-client
      binds -> gpointer: binds
        binds
      cursor-position -> AstalHyprlandPosition: cursor-position
        cursor-position

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        monitors: list[Monitor]
        workspaces: list[Workspace]
        clients: list[Client]
        focused_workspace: Workspace
        focused_monitor: Monitor
        focused_client: Client
        binds: list[Bind]
        cursor_position: Position
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: HyprlandPrivate = ...
    def __init__(self, focused_workspace: Workspace = ...,
                 focused_monitor: Monitor = ...,
                 focused_client: Client = ...) -> None: ...
    def dispatch(self, dispatcher: str, args: str) -> None: ...
    def get_binds(self) -> list[Bind]: ...
    def get_client(self, address: str) -> typing.Optional[Client]: ...
    def get_clients(self) -> list[Client]: ...
    def get_cursor_position(self) -> Position: ...
    @staticmethod
    def get_default() -> typing.Optional[Hyprland]: ...
    def get_focused_client(self) -> Client: ...
    def get_focused_monitor(self) -> Monitor: ...
    def get_focused_workspace(self) -> Workspace: ...
    def get_monitor(self, id: int) -> Monitor: ...
    def get_monitor_by_name(self, name: str) -> typing.Optional[Monitor]: ...
    def get_monitors(self) -> list[Monitor]: ...
    def get_workspace(self, id: int) -> Workspace: ...
    def get_workspace_by_name(self, name: str) -> typing.Optional[Workspace]: ...
    def get_workspaces(self) -> list[Workspace]: ...
    def message(self, message: str) -> str: ...
    def message_async(self, message: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def message_finish(self, _res_: Gio.AsyncResult) -> str: ...
    def move_cursor(self, x: int, y: int) -> None: ...
    @classmethod
    def new(cls) -> Hyprland: ...
    def sync_clients(self, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def sync_clients_finish(self, _res_: Gio.AsyncResult) -> None: ...
    def sync_monitors(self, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def sync_monitors_finish(self, _res_: Gio.AsyncResult) -> None: ...
    def sync_workspaces(self, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def sync_workspaces_finish(self, _res_: Gio.AsyncResult) -> None: ...
    

class HyprlandClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HyprlandClass()
    """
    parent_class: GObject.ObjectClass = ...

class HyprlandPrivate(GObject.GPointer): ...

class Monitor(GObject.Object):
    """
    :Constructors:

    ::

        Monitor(**properties)
        new() -> AstalHyprland.Monitor

    Object AstalHyprlandMonitor

    Signals from AstalHyprlandMonitor:
      removed ()

    Properties from AstalHyprlandMonitor:
      id -> gint: id
        id
      name -> gchararray: name
        name
      description -> gchararray: description
        description
      make -> gchararray: make
        make
      model -> gchararray: model
        model
      serial -> gchararray: serial
        serial
      width -> gint: width
        width
      height -> gint: height
        height
      refresh-rate -> gdouble: refresh-rate
        refresh-rate
      x -> gint: x
        x
      y -> gint: y
        y
      active-workspace -> AstalHyprlandWorkspace: active-workspace
        active-workspace
      special-workspace -> AstalHyprlandWorkspace: special-workspace
        special-workspace
      reserved-top -> gint: reserved-top
        reserved-top
      reserved-bottom -> gint: reserved-bottom
        reserved-bottom
      reserved-left -> gint: reserved-left
        reserved-left
      reserved-right -> gint: reserved-right
        reserved-right
      scale -> gdouble: scale
        scale
      transform -> AstalHyprlandMonitorTransform: transform
        transform
      focused -> gboolean: focused
        focused
      dpms-status -> gboolean: dpms-status
        dpms-status
      vrr -> gboolean: vrr
        vrr
      actively-tearing -> gboolean: actively-tearing
        actively-tearing
      disabled -> gboolean: disabled
        disabled
      current-format -> gchararray: current-format
        current-format
      available-modes -> GArray: available-modes
        available-modes

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        id: int
        name: str
        description: str
        make: str
        model: str
        serial: str
        width: int
        height: int
        refresh_rate: float
        x: int
        y: int
        active_workspace: Workspace
        special_workspace: Workspace
        reserved_top: int
        reserved_bottom: int
        reserved_left: int
        reserved_right: int
        scale: float
        transform: MonitorTransform
        focused: bool
        dpms_status: bool
        vrr: bool
        actively_tearing: bool
        disabled: bool
        current_format: str
        available_modes: list[str]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: MonitorPrivate = ...
    def __init__(self, id: int = ...,
                 name: str = ...,
                 description: str = ...,
                 make: str = ...,
                 model: str = ...,
                 serial: str = ...,
                 width: int = ...,
                 height: int = ...,
                 refresh_rate: float = ...,
                 x: int = ...,
                 y: int = ...,
                 active_workspace: Workspace = ...,
                 special_workspace: Workspace = ...,
                 reserved_top: int = ...,
                 reserved_bottom: int = ...,
                 reserved_left: int = ...,
                 reserved_right: int = ...,
                 scale: float = ...,
                 transform: MonitorTransform = ...,
                 focused: bool = ...,
                 dpms_status: bool = ...,
                 vrr: bool = ...,
                 actively_tearing: bool = ...,
                 disabled: bool = ...,
                 current_format: str = ...,
                 available_modes: typing.Sequence[str] = ...) -> None: ...
    def focus(self) -> None: ...
    def get_active_workspace(self) -> Workspace: ...
    def get_actively_tearing(self) -> bool: ...
    def get_available_modes(self) -> list[str]: ...
    def get_current_format(self) -> str: ...
    def get_description(self) -> str: ...
    def get_disabled(self) -> bool: ...
    def get_dpms_status(self) -> bool: ...
    def get_focused(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_id(self) -> int: ...
    def get_make(self) -> str: ...
    def get_model(self) -> str: ...
    def get_name(self) -> str: ...
    def get_refresh_rate(self) -> float: ...
    def get_reserved_bottom(self) -> int: ...
    def get_reserved_left(self) -> int: ...
    def get_reserved_right(self) -> int: ...
    def get_reserved_top(self) -> int: ...
    def get_scale(self) -> float: ...
    def get_serial(self) -> str: ...
    def get_special_workspace(self) -> Workspace: ...
    def get_transform(self) -> MonitorTransform: ...
    def get_vrr(self) -> bool: ...
    def get_width(self) -> int: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    @classmethod
    def new(cls) -> Monitor: ...
    

class MonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MonitorClass()
    """
    parent_class: GObject.ObjectClass = ...

class MonitorPrivate(GObject.GPointer): ...

class Position(GObject.Object):
    """
    :Constructors:

    ::

        Position(**properties)
        new() -> AstalHyprland.Position

    Object AstalHyprlandPosition

    Properties from AstalHyprlandPosition:
      x -> gint: x
        x
      y -> gint: y
        y

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        x: int
        y: int
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: PositionPrivate = ...
    def __init__(self, x: int = ...,
                 y: int = ...) -> None: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    @classmethod
    def new(cls) -> Position: ...
    def set_x(self, value: int) -> None: ...
    def set_y(self, value: int) -> None: ...
    

class PositionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PositionClass()
    """
    parent_class: GObject.ObjectClass = ...

class PositionPrivate(GObject.GPointer): ...

class Workspace(GObject.Object):
    """
    :Constructors:

    ::

        Workspace(**properties)
        dummy(id:int, monitor:AstalHyprland.Monitor=None) -> AstalHyprland.Workspace
        new() -> AstalHyprland.Workspace

    Object AstalHyprlandWorkspace

    Signals from AstalHyprlandWorkspace:
      removed ()

    Properties from AstalHyprlandWorkspace:
      id -> gint: id
        id
      name -> gchararray: name
        name
      monitor -> AstalHyprlandMonitor: monitor
        monitor
      clients -> gpointer: clients
        clients
      has-fullscreen -> gboolean: has-fullscreen
        has-fullscreen
      last-client -> AstalHyprlandClient: last-client
        last-client

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        id: int
        name: str
        monitor: Monitor
        clients: list[Client]
        has_fullscreen: bool
        last_client: Client
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: WorkspacePrivate = ...
    _clients: list[Client] = ...
    def __init__(self, id: int = ...,
                 name: str = ...,
                 monitor: Monitor = ...,
                 has_fullscreen: bool = ...,
                 last_client: Client = ...) -> None: ...
    @classmethod
    def dummy(cls, id: int, monitor: typing.Optional[Monitor] = None) -> Workspace: ...
    def focus(self) -> None: ...
    def get_clients(self) -> list[Client]: ...
    def get_has_fullscreen(self) -> bool: ...
    def get_id(self) -> int: ...
    def get_last_client(self) -> Client: ...
    def get_monitor(self) -> Monitor: ...
    def get_name(self) -> str: ...
    def move_to(self, m: Monitor) -> None: ...
    @classmethod
    def new(cls) -> Workspace: ...
    

class WorkspaceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WorkspaceClass()
    """
    parent_class: GObject.ObjectClass = ...

class WorkspacePrivate(GObject.GPointer): ...

class Fullscreen(GObject.GFlags):
    CURRENT = 18446744073709551615
    FULLSCREEN = 2
    MAXIMIZED = 1
    NONE = 0

class MonitorTransform(GObject.GEnum):
    FLIPPED = 4
    FLIPPED_ROTATE_180_DEG = 6
    FLIPPED_ROTATE_270_DEG = 7
    FLIPPED_ROTATE_90_DEG = 5
    NORMAL = 0
    ROTATE_180_DEG = 2
    ROTATE_270_DEG = 3
    ROTATE_90_DEG = 1


