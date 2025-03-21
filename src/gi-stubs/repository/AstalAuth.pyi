import typing

from gi.repository import GObject
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalAuth"
_version: str = "0.1"

class Pam(GObject.Object):
    """
    :Constructors:

    ::

        Pam(**properties)

    Object AstalAuthPam

    Signals from AstalAuthPam:
      auth-prompt-visible (gchararray)
      auth-prompt-hidden (gchararray)
      auth-info (gchararray)
      auth-error (gchararray)
      success ()
      fail (gchararray)

    Properties from AstalAuthPam:
      username -> gchararray: username
        username used for authentication
      service -> gchararray: service
        the pam service to use

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        service: str
        username: str
    props: Props = ...
    def __init__(self, service: str = ...,
                 username: str = ...) -> None: ...
    @staticmethod
    def authenticate(password: str, result_callback: typing.Optional[typing.Callable[..., None]] = None, *user_data: typing.Any) -> bool: ...
    @staticmethod
    def authenticate_finish(res: Gio.AsyncResult) -> int: ...
    def get_service(self) -> str: ...
    def get_username(self) -> str: ...
    def set_service(self, service: str) -> None: ...
    def set_username(self, username: str) -> None: ...
    def start_authenticate(self) -> bool: ...
    def supply_secret(self, secret: typing.Optional[str] = None) -> None: ...
    

class PamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PamClass()
    """
    parent_class: GObject.ObjectClass = ...


