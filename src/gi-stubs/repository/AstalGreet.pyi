import typing

from gi.repository import GObject
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalGreet"
_version: str = "0.1"

def login(username: str, password: str, cmd: str, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
def login_finish(_res_: Gio.AsyncResult) -> None: ...
def login_with_env(username: str, password: str, cmd: str, env: typing.Sequence[str], _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
def login_with_env_finish(_res_: Gio.AsyncResult) -> None: ...

class AuthMessage(Response):
    """
    :Constructors:

    ::

        AuthMessage(**properties)

    Object AstalGreetAuthMessage

    Properties from AstalGreetAuthMessage:
      message-type -> AstalGreetAuthMessageType: message-type
        message-type
      message -> gchararray: message
        message

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        message_type: AuthMessageType
        message: str
    props: Props = ...
    parent_instance: Response = ...
    priv: AuthMessagePrivate = ...
    def __init__(self, message_type: AuthMessageType = ...,
                 message: str = ...) -> None: ...
    def get_message(self) -> str: ...
    def get_message_type(self) -> AuthMessageType: ...
    

class AuthMessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthMessageClass()
    """
    parent_class: ResponseClass = ...

class AuthMessagePrivate(GObject.GPointer): ...

class CancelSession(Request):
    """
    :Constructors:

    ::

        CancelSession(**properties)
        new() -> AstalGreet.CancelSession

    Object AstalGreetCancelSession

    Properties from AstalGreetCancelSession:
      type-name -> gchararray: type-name
        type-name

    Properties from AstalGreetRequest:
      type-name -> gchararray: type-name
        type-name

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        type_name: str
    props: Props = ...
    parent_instance: Request = ...
    priv: CancelSessionPrivate = ...
    @classmethod
    def new(cls) -> CancelSession: ...
    

class CancelSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CancelSessionClass()
    """
    parent_class: RequestClass = ...

class CancelSessionPrivate(GObject.GPointer): ...

class CreateSession(Request):
    """
    :Constructors:

    ::

        CreateSession(**properties)
        new(username:str) -> AstalGreet.CreateSession

    Object AstalGreetCreateSession

    Properties from AstalGreetCreateSession:
      type-name -> gchararray: type-name
        type-name
      username -> gchararray: username
        username

    Properties from AstalGreetRequest:
      type-name -> gchararray: type-name
        type-name

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        username: str
        type_name: str
    props: Props = ...
    parent_instance: Request = ...
    priv: CreateSessionPrivate = ...
    def __init__(self, username: str = ...) -> None: ...
    def get_username(self) -> str: ...
    @classmethod
    def new(cls, username: str) -> CreateSession: ...
    def set_username(self, value: str) -> None: ...
    

class CreateSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CreateSessionClass()
    """
    parent_class: RequestClass = ...

class CreateSessionPrivate(GObject.GPointer): ...

class Error(Response):
    """
    :Constructors:

    ::

        Error(**properties)

    Object AstalGreetError

    Properties from AstalGreetError:
      error-type -> AstalGreetErrorType: error-type
        error-type
      description -> gchararray: description
        description

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        error_type: ErrorType
        description: str
    props: Props = ...
    parent_instance: Response = ...
    priv: ErrorPrivate = ...
    def __init__(self, error_type: ErrorType = ...,
                 description: str = ...) -> None: ...
    def get_description(self) -> str: ...
    def get_error_type(self) -> ErrorType: ...
    

class ErrorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ErrorClass()
    """
    parent_class: ResponseClass = ...

class ErrorPrivate(GObject.GPointer): ...

class PostAuthMesssage(Request):
    """
    :Constructors:

    ::

        PostAuthMesssage(**properties)
        new(response:str) -> AstalGreet.PostAuthMesssage

    Object AstalGreetPostAuthMesssage

    Properties from AstalGreetPostAuthMesssage:
      type-name -> gchararray: type-name
        type-name
      response -> gchararray: response
        response

    Properties from AstalGreetRequest:
      type-name -> gchararray: type-name
        type-name

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        response: str
        type_name: str
    props: Props = ...
    parent_instance: Request = ...
    priv: PostAuthMesssagePrivate = ...
    def __init__(self, response: str = ...) -> None: ...
    def get_response(self) -> str: ...
    @classmethod
    def new(cls, response: str) -> PostAuthMesssage: ...
    def set_response(self, value: str) -> None: ...
    

class PostAuthMesssageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PostAuthMesssageClass()
    """
    parent_class: RequestClass = ...

class PostAuthMesssagePrivate(GObject.GPointer): ...

class Request(GObject.Object):
    """
    :Constructors:

    ::

        Request(**properties)

    Object AstalGreetRequest

    Properties from AstalGreetRequest:
      type-name -> gchararray: type-name
        type-name

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        type_name: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: RequestPrivate = ...
    def do_get_type_name(self) -> str: ...
    def get_type_name(self) -> str: ...
    def send(self, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def send_finish(self, _res_: Gio.AsyncResult) -> Response: ...
    

class RequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RequestClass()
    """
    parent_class: GObject.ObjectClass = ...

class RequestPrivate(GObject.GPointer): ...

class Response(GObject.Object):
    """
    :Constructors:

    ::

        Response(**properties)

    Object AstalGreetResponse

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: GObject.Object = ...
    priv: ResponsePrivate = ...

class ResponseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ResponseClass()
    """
    parent_class: GObject.ObjectClass = ...

class ResponsePrivate(GObject.GPointer): ...

class StartSession(Request):
    """
    :Constructors:

    ::

        StartSession(**properties)
        new(cmd:list, env:list) -> AstalGreet.StartSession

    Object AstalGreetStartSession

    Properties from AstalGreetStartSession:
      type-name -> gchararray: type-name
        type-name
      cmd -> GStrv: cmd
        cmd
      env -> GStrv: env
        env

    Properties from AstalGreetRequest:
      type-name -> gchararray: type-name
        type-name

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        cmd: list[str]
        env: list[str]
        type_name: str
    props: Props = ...
    parent_instance: Request = ...
    priv: StartSessionPrivate = ...
    def __init__(self, cmd: typing.Sequence[str] = ...,
                 env: typing.Sequence[str] = ...) -> None: ...
    def get_cmd(self) -> list[str]: ...
    def get_env(self) -> list[str]: ...
    @classmethod
    def new(cls, cmd: typing.Sequence[str], env: typing.Sequence[str]) -> StartSession: ...
    def set_cmd(self, value: typing.Sequence[str]) -> None: ...
    def set_env(self, value: typing.Sequence[str]) -> None: ...
    

class StartSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StartSessionClass()
    """
    parent_class: RequestClass = ...

class StartSessionPrivate(GObject.GPointer): ...

class Success(Response):
    """
    :Constructors:

    ::

        Success(**properties)

    Object AstalGreetSuccess

    Signals from GObject:
      notify (GParam)
    """
    parent_instance: Response = ...
    priv: SuccessPrivate = ...

class SuccessClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SuccessClass()
    """
    parent_class: ResponseClass = ...

class SuccessPrivate(GObject.GPointer): ...

class AuthMessageType(GObject.GEnum):
    ERROR = 3
    INFO = 2
    SECRET = 1
    VISIBLE = 0

class ErrorType(GObject.GEnum):
    AUTH_ERROR = 0
    ERROR = 1


