import typing

from gi.repository import GObject
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalIO"
_version: str = "0.1"

def acquire_socket(app: Application) -> typing.Tuple[Gio.SocketService, str]: ...
def get_instances() -> list[str]: ...
def monitor_file(path: str, callback: typing.Callable[..., typing.Any]) -> typing.Optional[Gio.FileMonitor]: ...
def open_inspector(instance: str) -> None: ...
def quit_instance(instance: str) -> None: ...
def read_file(path: str) -> str: ...
def read_file_async(path: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
def read_file_finish(_res_: Gio.AsyncResult) -> str: ...
def read_sock(conn: Gio.SocketConnection, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
def read_sock_finish(_res_: Gio.AsyncResult) -> str: ...
def send_message(instance: str, msg: str) -> str: ...
def toggle_window_by_name(instance: str, window: str) -> None: ...
def write_file(path: str, content: str) -> None: ...
def write_file_async(path: str, content: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
def write_file_finish(_res_: Gio.AsyncResult) -> None: ...
def write_sock(conn: Gio.SocketConnection, response: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
def write_sock_finish(_res_: Gio.AsyncResult) -> None: ...

class Application(GObject.GInterface):
    """
    Interface AstalIOApplication

    Signals from GObject:
      notify (GParam)
    """
    def acquire_socket(self) -> None: ...
    def get_instance_name(self) -> str: ...
    def inspector(self) -> None: ...
    def quit(self) -> None: ...
    def request(self, msg: str, conn: Gio.SocketConnection) -> None: ...
    def set_instance_name(self, value: str) -> None: ...
    def toggle_window(self, window: str) -> None: ...
    

class ApplicationIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationIface()
    """
    parent_iface: GObject.TypeInterface = ...
    quit: typing.Callable[[Application], None] = ...
    inspector: typing.Callable[[Application], None] = ...
    toggle_window: typing.Callable[[Application, str], None] = ...
    acquire_socket: typing.Callable[[Application], None] = ...
    request: typing.Callable[[Application, str, Gio.SocketConnection], None] = ...
    get_instance_name: typing.Callable[[Application], str] = ...
    set_instance_name: typing.Callable[[Application, str], None] = ...

class Daemon(Gio.Application, Application):
    """
    :Constructors:

    ::

        Daemon(**properties)
        new() -> AstalIO.Daemon

    Object AstalIODaemon

    Properties from AstalIODaemon:
      instance-name -> gchararray: instance-name
        instance-name

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GApplication:
      startup ()
      shutdown ()
      activate ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean

    Properties from GApplication:
      application-id -> gchararray: application-id
      version -> gchararray: version
      flags -> GApplicationFlags: flags
      resource-base-path -> gchararray: resource-base-path
      is-registered -> gboolean: is-registered
      is-remote -> gboolean: is-remote
      inactivity-timeout -> guint: inactivity-timeout
      action-group -> GActionGroup: action-group
      is-busy -> gboolean: is-busy

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        application_id: typing.Optional[str]
        flags: Gio.ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: typing.Optional[str]
        version: typing.Optional[str]
        instance_name: str
        action_group: typing.Optional[Gio.ActionGroup]
    props: Props = ...
    parent_instance: Gio.Application = ...
    priv: DaemonPrivate = ...
    def __init__(self, action_group: typing.Optional[Gio.ActionGroup] = ...,
                 application_id: typing.Optional[str] = ...,
                 flags: Gio.ApplicationFlags = ...,
                 inactivity_timeout: int = ...,
                 resource_base_path: typing.Optional[str] = ...,
                 version: str = ...,
                 instance_name: str = ...) -> None: ...
    def do_request(self, msg: str, conn: Gio.SocketConnection) -> None: ...
    @classmethod
    def new(cls) -> Daemon: ...
    def request(self, msg: str, conn: Gio.SocketConnection) -> None: ...
    

class DaemonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DaemonClass()
    """
    parent_class: Gio.ApplicationClass = ...
    request: typing.Callable[[Daemon, str, Gio.SocketConnection], None] = ...

class DaemonPrivate(GObject.GPointer): ...

class Process(GObject.Object):
    """
    :Constructors:

    ::

        Process(**properties)
        new(cmd:list) -> AstalIO.Process

    Object AstalIOProcess

    Signals from AstalIOProcess:
      stdout (gchararray)
      stderr (gchararray)
      exit (gint, gboolean)

    Properties from AstalIOProcess:
      argv -> GStrv: argv
        argv

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        argv: list[str]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: ProcessPrivate = ...
    def __init__(self, argv: typing.Sequence[str] = ...) -> None: ...
    @staticmethod
    def exec(cmd: str) -> str: ...
    @staticmethod
    def exec_async(cmd: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    @staticmethod
    def exec_asyncv(cmd: typing.Sequence[str], _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    @staticmethod
    def exec_asyncv_finish(_res_: Gio.AsyncResult) -> str: ...
    @staticmethod
    def exec_finish(_res_: Gio.AsyncResult) -> str: ...
    @staticmethod
    def execv(cmd: typing.Sequence[str]) -> str: ...
    def get_argv(self) -> list[str]: ...
    def kill(self) -> None: ...
    @classmethod
    def new(cls, cmd: typing.Sequence[str]) -> Process: ...
    def signal(self, signal_num: int) -> None: ...
    @staticmethod
    def subprocess(cmd: str) -> Process: ...
    @staticmethod
    def subprocessv(cmd: typing.Sequence[str]) -> Process: ...
    def write(self, in_: str) -> None: ...
    def write_async(self, in_: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def write_finish(self, _res_: Gio.AsyncResult) -> None: ...
    

class ProcessClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProcessClass()
    """
    parent_class: GObject.ObjectClass = ...

class ProcessPrivate(GObject.GPointer): ...

class Time(GObject.Object):
    """
    :Constructors:

    ::

        Time(**properties)
        interval_prio(interval:int, prio:int, fn:GObject.Closure=None) -> AstalIO.Time
        timeout_prio(timeout:int, prio:int, fn:GObject.Closure=None) -> AstalIO.Time
        idle_prio(prio:int, fn:GObject.Closure=None) -> AstalIO.Time
        new() -> AstalIO.Time

    Object AstalIOTime

    Signals from AstalIOTime:
      now ()
      cancelled ()

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    priv: TimePrivate = ...
    def cancel(self) -> None: ...
    @staticmethod
    def idle(fn: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Time: ...
    @classmethod
    def idle_prio(cls, prio: int, fn: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Time: ...
    @staticmethod
    def interval(interval: int, fn: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Time: ...
    @classmethod
    def interval_prio(cls, interval: int, prio: int, fn: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Time: ...
    @classmethod
    def new(cls) -> Time: ...
    @staticmethod
    def timeout(timeout: int, fn: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Time: ...
    @classmethod
    def timeout_prio(cls, timeout: int, prio: int, fn: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Time: ...
    

class TimeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TimeClass()
    """
    parent_class: GObject.ObjectClass = ...

class TimePrivate(GObject.GPointer): ...

class Variable(VariableBase):
    """
    :Constructors:

    ::

        Variable(**properties)
        new(init:GObject.Value) -> AstalIO.Variable

    Object AstalIOVariable

    Properties from AstalIOVariable:
      value -> GValue: value
        value

    Signals from AstalIOVariableBase:
      changed ()
      dropped ()
      error (gchararray)

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        value: typing.Any
    props: Props = ...
    parent_instance: VariableBase = ...
    priv: VariablePrivate = ...
    def __init__(self, value: typing.Any = ...) -> None: ...
    def get_value(self) -> typing.Any: ...
    def is_polling(self) -> bool: ...
    def is_watching(self) -> bool: ...
    @classmethod
    def new(cls, init: typing.Any) -> Variable: ...
    def poll(self, interval: int, exec: str, transform: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Variable: ...
    def pollfn(self, interval: int, fn: typing.Callable[..., typing.Any]) -> Variable: ...
    def pollv(self, interval: int, execv: typing.Sequence[str], transform: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Variable: ...
    def set_value(self, value: typing.Any) -> None: ...
    def start_poll(self) -> None: ...
    def start_watch(self) -> None: ...
    def stop_poll(self) -> None: ...
    def stop_watch(self) -> None: ...
    def watch(self, exec: str, transform: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Variable: ...
    def watchv(self, execv: typing.Sequence[str], transform: typing.Optional[typing.Callable[..., typing.Any]] = None) -> Variable: ...
    

class VariableBase(GObject.Object):
    """
    :Constructors:

    ::

        VariableBase(**properties)
        new() -> AstalIO.VariableBase

    Object AstalIOVariableBase

    Signals from AstalIOVariableBase:
      changed ()
      dropped ()
      error (gchararray)

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    priv: VariableBasePrivate = ...
    def emit_changed(self) -> None: ...
    def emit_dropped(self) -> None: ...
    def emit_error(self, err: str) -> None: ...
    @classmethod
    def new(cls) -> VariableBase: ...
    

class VariableBaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VariableBaseClass()
    """
    parent_class: GObject.ObjectClass = ...

class VariableBasePrivate(GObject.GPointer): ...

class VariableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VariableClass()
    """
    parent_class: VariableBaseClass = ...

class VariablePrivate(GObject.GPointer): ...

class AppError(GObject.GEnum):
    NAME_OCCUPIED = 0
    TAKEOVER_FAILED = 1


