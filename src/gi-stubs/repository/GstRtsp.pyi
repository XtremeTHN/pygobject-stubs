from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstSdp

RTSP_DEFAULT_PORT: int = 554
_lock = ...  # FIXME Constant
_namespace: str = "GstRtsp"
_version: str = "1.0"

def rtsp_auth_credentials_free(credentials: RTSPAuthCredential) -> None: ...
def rtsp_connection_accept(
    socket: Gio.Socket, cancellable: Optional[Gio.Cancellable] = None
) -> Tuple[RTSPResult, RTSPConnection]: ...
def rtsp_connection_create(url: RTSPUrl) -> Tuple[RTSPResult, RTSPConnection]: ...
def rtsp_connection_create_from_socket(
    socket: Gio.Socket, ip: str, port: int, initial_buffer: str
) -> Tuple[RTSPResult, RTSPConnection]: ...
def rtsp_find_header_field(header: str) -> RTSPHeaderField: ...
def rtsp_find_method(method: str) -> RTSPMethod: ...
def rtsp_generate_digest_auth_response(
    algorithm: Optional[str],
    method: str,
    realm: str,
    username: str,
    password: str,
    uri: str,
    nonce: str,
) -> Optional[str]: ...
def rtsp_generate_digest_auth_response_from_md5(
    algorithm: Optional[str], method: str, md5: str, uri: str, nonce: str
) -> Optional[str]: ...
def rtsp_header_allow_multiple(field: RTSPHeaderField) -> bool: ...
def rtsp_header_as_text(field: RTSPHeaderField) -> Optional[str]: ...
def rtsp_message_new() -> Tuple[RTSPResult, RTSPMessage]: ...
def rtsp_message_new_data(channel: int) -> Tuple[RTSPResult, RTSPMessage]: ...
def rtsp_message_new_request(
    method: RTSPMethod, uri: str
) -> Tuple[RTSPResult, RTSPMessage]: ...
def rtsp_message_new_response(
    code: RTSPStatusCode,
    reason: Optional[str] = None,
    request: Optional[RTSPMessage] = None,
) -> Tuple[RTSPResult, RTSPMessage]: ...
def rtsp_method_as_text(method: RTSPMethod) -> Optional[str]: ...
def rtsp_options_as_text(options: RTSPMethod) -> str: ...
def rtsp_options_from_text(options: str) -> RTSPMethod: ...
def rtsp_range_convert_units(range: RTSPTimeRange, unit: RTSPRangeUnit) -> bool: ...
def rtsp_range_free(range: RTSPTimeRange) -> None: ...
def rtsp_range_get_times(range: RTSPTimeRange) -> Tuple[bool, int, int]: ...
def rtsp_range_parse(rangestr: str) -> Tuple[RTSPResult, RTSPTimeRange]: ...
def rtsp_range_to_string(range: RTSPTimeRange) -> str: ...
def rtsp_status_as_text(code: RTSPStatusCode) -> str: ...
def rtsp_strresult(result: RTSPResult) -> str: ...
def rtsp_transport_get_manager(
    trans: RTSPTransMode, option: int
) -> Tuple[RTSPResult, str]: ...
def rtsp_transport_get_mime(trans: RTSPTransMode) -> Tuple[RTSPResult, str]: ...
def rtsp_transport_init() -> Tuple[RTSPResult, RTSPTransport]: ...
def rtsp_transport_new() -> Tuple[RTSPResult, RTSPTransport]: ...
def rtsp_transport_parse(str: str) -> Tuple[RTSPResult, RTSPTransport]: ...
def rtsp_url_parse(urlstr: str) -> Tuple[RTSPResult, RTSPUrl]: ...
def rtsp_version_as_text(version: RTSPVersion) -> str: ...

class RTSPAuthCredential(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPAuthCredential()
    """

    scheme: RTSPAuthMethod = ...
    params: RTSPAuthParam = ...
    authorization: str = ...

class RTSPAuthParam(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPAuthParam()
    """

    name: str = ...
    value: str = ...
    def copy(self) -> RTSPAuthParam: ...
    def free(self) -> None: ...

class RTSPConnection(GObject.GPointer):
    @staticmethod
    def accept(
        socket: Gio.Socket, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[RTSPResult, RTSPConnection]: ...
    def clear_auth_params(self) -> None: ...
    def close(self) -> RTSPResult: ...
    def connect(self, timeout: GLib.TimeVal) -> RTSPResult: ...
    def connect_usec(self, timeout: int) -> RTSPResult: ...
    def connect_with_response(
        self, timeout: GLib.TimeVal, response: RTSPMessage
    ) -> RTSPResult: ...
    def connect_with_response_usec(
        self, timeout: int, response: RTSPMessage
    ) -> RTSPResult: ...
    @staticmethod
    def create(url: RTSPUrl) -> Tuple[RTSPResult, RTSPConnection]: ...
    @staticmethod
    def create_from_socket(
        socket: Gio.Socket, ip: str, port: int, initial_buffer: str
    ) -> Tuple[RTSPResult, RTSPConnection]: ...
    def do_tunnel(self, conn2: Optional[RTSPConnection] = None) -> RTSPResult: ...
    def flush(self, flush: bool) -> RTSPResult: ...
    def free(self) -> RTSPResult: ...
    def get_ignore_x_server_reply(self) -> bool: ...
    def get_ip(self) -> str: ...
    def get_read_socket(self) -> Optional[Gio.Socket]: ...
    def get_remember_session_id(self) -> bool: ...
    def get_tls(self) -> Gio.TlsConnection: ...
    def get_tls_database(self) -> Optional[Gio.TlsDatabase]: ...
    def get_tls_interaction(self) -> Optional[Gio.TlsInteraction]: ...
    def get_tls_validation_flags(self) -> Gio.TlsCertificateFlags: ...
    def get_tunnelid(self) -> Optional[str]: ...
    def get_url(self) -> RTSPUrl: ...
    def get_write_socket(self) -> Optional[Gio.Socket]: ...
    def is_tunneled(self) -> bool: ...
    def next_timeout(self, timeout: GLib.TimeVal) -> RTSPResult: ...
    def next_timeout_usec(self) -> int: ...
    def poll(
        self, events: RTSPEvent, timeout: GLib.TimeVal
    ) -> Tuple[RTSPResult, RTSPEvent]: ...
    def poll_usec(
        self, events: RTSPEvent, timeout: int
    ) -> Tuple[RTSPResult, RTSPEvent]: ...
    def read(self, data: Sequence[int], timeout: GLib.TimeVal) -> RTSPResult: ...
    def read_usec(self, data: Sequence[int], timeout: int) -> RTSPResult: ...
    def receive(self, message: RTSPMessage, timeout: GLib.TimeVal) -> RTSPResult: ...
    def receive_usec(self, message: RTSPMessage, timeout: int) -> RTSPResult: ...
    def reset_timeout(self) -> RTSPResult: ...
    def send(self, message: RTSPMessage, timeout: GLib.TimeVal) -> RTSPResult: ...
    def send_messages(
        self, messages: Sequence[RTSPMessage], timeout: GLib.TimeVal
    ) -> RTSPResult: ...
    def send_messages_usec(
        self, messages: Sequence[RTSPMessage], timeout: int
    ) -> RTSPResult: ...
    def send_usec(self, message: RTSPMessage, timeout: int) -> RTSPResult: ...
    def set_accept_certificate_func(
        self, func: Callable[..., bool], *user_data: Any
    ) -> None: ...
    def set_auth(self, method: RTSPAuthMethod, user: str, pass_: str) -> RTSPResult: ...
    def set_auth_param(self, param: str, value: str) -> None: ...
    def set_content_length_limit(self, limit: int) -> None: ...
    def set_http_mode(self, enable: bool) -> None: ...
    def set_ignore_x_server_reply(self, ignore: bool) -> None: ...
    def set_ip(self, ip: str) -> None: ...
    def set_proxy(self, host: str, port: int) -> RTSPResult: ...
    def set_qos_dscp(self, qos_dscp: int) -> RTSPResult: ...
    def set_remember_session_id(self, remember: bool) -> None: ...
    def set_tls_database(self, database: Optional[Gio.TlsDatabase] = None) -> None: ...
    def set_tls_interaction(
        self, interaction: Optional[Gio.TlsInteraction] = None
    ) -> None: ...
    def set_tls_validation_flags(self, flags: Gio.TlsCertificateFlags) -> bool: ...
    def set_tunneled(self, tunneled: bool) -> None: ...
    def write(self, data: Sequence[int], timeout: GLib.TimeVal) -> RTSPResult: ...
    def write_usec(self, data: Sequence[int], timeout: int) -> RTSPResult: ...

class RTSPExtension(GObject.GInterface):
    """
    Interface GstRTSPExtension
    """

    def after_send(self, req: RTSPMessage, resp: RTSPMessage) -> RTSPResult: ...
    def before_send(self, req: RTSPMessage) -> RTSPResult: ...
    def configure_stream(self, caps: Gst.Caps) -> bool: ...
    def detect_server(self, resp: RTSPMessage) -> bool: ...
    def get_transports(
        self, protocols: RTSPLowerTrans, transport: str
    ) -> RTSPResult: ...
    def parse_sdp(self, sdp: GstSdp.SDPMessage, s: Gst.Structure) -> RTSPResult: ...
    def receive_request(self, req: RTSPMessage) -> RTSPResult: ...
    def send(self, req: RTSPMessage, resp: RTSPMessage) -> RTSPResult: ...
    def setup_media(self, media: GstSdp.SDPMedia) -> RTSPResult: ...
    def stream_select(self, url: RTSPUrl) -> RTSPResult: ...

class RTSPExtensionInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPExtensionInterface()
    """

    parent: GObject.TypeInterface = ...
    detect_server: Callable[[RTSPExtension, RTSPMessage], bool] = ...
    before_send: Callable[[RTSPExtension, RTSPMessage], RTSPResult] = ...
    after_send: Callable[[RTSPExtension, RTSPMessage, RTSPMessage], RTSPResult] = ...
    parse_sdp: Callable[
        [RTSPExtension, GstSdp.SDPMessage, Gst.Structure], RTSPResult
    ] = ...
    setup_media: Callable[[RTSPExtension, GstSdp.SDPMedia], RTSPResult] = ...
    configure_stream: Callable[[RTSPExtension, Gst.Caps], bool] = ...
    get_transports: Callable[[RTSPExtension, RTSPLowerTrans, str], RTSPResult] = ...
    stream_select: Callable[[RTSPExtension, RTSPUrl], RTSPResult] = ...
    send: Callable[[RTSPExtension, RTSPMessage, RTSPMessage], RTSPResult] = ...
    receive_request: Callable[[RTSPExtension, RTSPMessage], RTSPResult] = ...
    _gst_reserved: list[None] = ...

class RTSPMessage(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPMessage()
    """

    type: RTSPMsgType = ...
    hdr_fields: list[None] = ...
    body: int = ...
    body_size: int = ...
    body_buffer: Gst.Buffer = ...
    _gst_reserved: list[None] = ...
    def add_header(self, field: RTSPHeaderField, value: str) -> RTSPResult: ...
    def add_header_by_name(self, header: str, value: str) -> RTSPResult: ...
    def append_headers(self, str: GLib.String) -> RTSPResult: ...
    def copy(self) -> Tuple[RTSPResult, RTSPMessage]: ...
    def dump(self) -> RTSPResult: ...
    def free(self) -> RTSPResult: ...
    def get_body(self) -> Tuple[RTSPResult, bytes]: ...
    def get_body_buffer(self) -> Tuple[RTSPResult, Gst.Buffer]: ...
    def get_header(
        self, field: RTSPHeaderField, indx: int
    ) -> Tuple[RTSPResult, str]: ...
    def get_header_by_name(self, header: str, index: int) -> Tuple[RTSPResult, str]: ...
    def get_type(self) -> RTSPMsgType: ...
    def has_body_buffer(self) -> bool: ...
    def init(self) -> RTSPResult: ...
    def init_data(self, channel: int) -> RTSPResult: ...
    def init_request(self, method: RTSPMethod, uri: str) -> RTSPResult: ...
    def init_response(
        self,
        code: RTSPStatusCode,
        reason: Optional[str] = None,
        request: Optional[RTSPMessage] = None,
    ) -> RTSPResult: ...
    def parse_auth_credentials(
        self, field: RTSPHeaderField
    ) -> list[RTSPAuthCredential]: ...
    def parse_data(self) -> Tuple[RTSPResult, int]: ...
    def parse_request(self) -> Tuple[RTSPResult, RTSPMethod, str, RTSPVersion]: ...
    def parse_response(self) -> Tuple[RTSPResult, RTSPStatusCode, str, RTSPVersion]: ...
    def remove_header(self, field: RTSPHeaderField, indx: int) -> RTSPResult: ...
    def remove_header_by_name(self, header: str, index: int) -> RTSPResult: ...
    def set_body(self, data: Sequence[int]) -> RTSPResult: ...
    def set_body_buffer(self, buffer: Gst.Buffer) -> RTSPResult: ...
    def steal_body(self) -> Tuple[RTSPResult, bytes]: ...
    def steal_body_buffer(self) -> Tuple[RTSPResult, Gst.Buffer]: ...
    def take_body(self, data: Sequence[int]) -> RTSPResult: ...
    def take_body_buffer(self, buffer: Gst.Buffer) -> RTSPResult: ...
    def take_header(self, field: RTSPHeaderField, value: str) -> RTSPResult: ...
    def take_header_by_name(self, header: str, value: str) -> RTSPResult: ...
    def unset(self) -> RTSPResult: ...

class RTSPRange(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPRange()
    """

    min: int = ...
    max: int = ...
    @staticmethod
    def convert_units(range: RTSPTimeRange, unit: RTSPRangeUnit) -> bool: ...
    @staticmethod
    def free(range: RTSPTimeRange) -> None: ...
    @staticmethod
    def get_times(range: RTSPTimeRange) -> Tuple[bool, int, int]: ...
    @staticmethod
    def parse(rangestr: str) -> Tuple[RTSPResult, RTSPTimeRange]: ...
    @staticmethod
    def to_string(range: RTSPTimeRange) -> str: ...

class RTSPTime(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPTime()
    """

    type: RTSPTimeType = ...
    seconds: float = ...

class RTSPTime2(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPTime2()
    """

    frames: float = ...
    year: int = ...
    month: int = ...
    day: int = ...

class RTSPTimeRange(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPTimeRange()
    """

    unit: RTSPRangeUnit = ...
    min: RTSPTime = ...
    max: RTSPTime = ...
    min2: RTSPTime2 = ...
    max2: RTSPTime2 = ...

class RTSPTransport(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPTransport()
    """

    trans: RTSPTransMode = ...
    profile: RTSPProfile = ...
    lower_transport: RTSPLowerTrans = ...
    destination: str = ...
    source: str = ...
    layers: int = ...
    mode_play: bool = ...
    mode_record: bool = ...
    append: bool = ...
    interleaved: RTSPRange = ...
    ttl: int = ...
    port: RTSPRange = ...
    client_port: RTSPRange = ...
    server_port: RTSPRange = ...
    ssrc: int = ...
    _gst_reserved: list[None] = ...
    def as_text(self) -> Optional[str]: ...
    def free(self) -> RTSPResult: ...
    @staticmethod
    def get_manager(trans: RTSPTransMode, option: int) -> Tuple[RTSPResult, str]: ...
    def get_media_type(self) -> Tuple[RTSPResult, str]: ...
    @staticmethod
    def get_mime(trans: RTSPTransMode) -> Tuple[RTSPResult, str]: ...
    @staticmethod
    def init() -> Tuple[RTSPResult, RTSPTransport]: ...
    @staticmethod
    def new() -> Tuple[RTSPResult, RTSPTransport]: ...
    @staticmethod
    def parse(str: str) -> Tuple[RTSPResult, RTSPTransport]: ...

class RTSPUrl(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPUrl()
    """

    transports: RTSPLowerTrans = ...
    family: RTSPFamily = ...
    user: str = ...
    passwd: str = ...
    host: str = ...
    port: int = ...
    abspath: str = ...
    query: str = ...
    def copy(self) -> RTSPUrl: ...
    def decode_path_components(self) -> list[str]: ...
    def free(self) -> None: ...
    def get_port(self) -> Tuple[RTSPResult, int]: ...
    def get_request_uri(self) -> str: ...
    def get_request_uri_with_control(self, control_path: str) -> str: ...
    @staticmethod
    def parse(urlstr: str) -> Tuple[RTSPResult, RTSPUrl]: ...
    def set_port(self, port: int) -> RTSPResult: ...

class RTSPWatch(GObject.GPointer):
    def attach(self, context: Optional[GLib.MainContext] = None) -> int: ...
    def get_send_backlog(self) -> Tuple[int, int]: ...
    def reset(self) -> None: ...
    def send_message(self, message: RTSPMessage) -> Tuple[RTSPResult, int]: ...
    def send_messages(
        self, messages: Sequence[RTSPMessage]
    ) -> Tuple[RTSPResult, int]: ...
    def set_flushing(self, flushing: bool) -> None: ...
    def set_send_backlog(self, bytes: int, messages: int) -> None: ...
    def unref(self) -> None: ...
    def wait_backlog(self, timeout: GLib.TimeVal) -> RTSPResult: ...
    def wait_backlog_usec(self, timeout: int) -> RTSPResult: ...
    def write_data(self, data: Sequence[int]) -> Tuple[RTSPResult, int]: ...

class RTSPWatchFuncs(GObject.GPointer):
    """
    :Constructors:

    ::

        RTSPWatchFuncs()
    """

    message_received: Callable[..., RTSPResult] = ...
    message_sent: Callable[..., RTSPResult] = ...
    closed: Callable[..., RTSPResult] = ...
    error: Callable[..., RTSPResult] = ...
    tunnel_start: Callable[..., RTSPStatusCode] = ...
    tunnel_complete: Callable[..., RTSPResult] = ...
    error_full: Callable[..., RTSPResult] = ...
    tunnel_lost: Callable[..., RTSPResult] = ...
    tunnel_http_response: Callable[..., RTSPResult] = ...
    _gst_reserved: list[None] = ...

class RTSPEvent(GObject.GFlags):
    READ = 1
    WRITE = 2

class RTSPLowerTrans(GObject.GFlags):
    HTTP = 16
    TCP = 4
    TLS = 32
    UDP = 1
    UDP_MCAST = 2
    UNKNOWN = 0

class RTSPMethod(GObject.GFlags):
    ANNOUNCE = 2
    DESCRIBE = 1
    GET = 2048
    GET_PARAMETER = 4
    INVALID = 0
    OPTIONS = 8
    PAUSE = 16
    PLAY = 32
    POST = 4096
    RECORD = 64
    REDIRECT = 128
    SETUP = 256
    SET_PARAMETER = 512
    TEARDOWN = 1024
    @staticmethod
    def as_text(method: RTSPMethod) -> Optional[str]: ...

class RTSPProfile(GObject.GFlags):
    AVP = 1
    AVPF = 4
    SAVP = 2
    SAVPF = 8
    UNKNOWN = 0

class RTSPTransMode(GObject.GFlags):
    RDT = 2
    RTP = 1
    UNKNOWN = 0

class RTSPAuthMethod(GObject.GEnum):
    BASIC = 1
    DIGEST = 2
    NONE = 0

class RTSPFamily(GObject.GEnum):
    INET = 1
    INET6 = 2
    NONE = 0

class RTSPHeaderField(GObject.GEnum):
    ACCEPT = 1
    ACCEPT_CHARSET = 56
    ACCEPT_ENCODING = 2
    ACCEPT_LANGUAGE = 3
    ACCEPT_RANGES = 86
    ALERT = 45
    ALLOW = 4
    AUTHENTICATION_INFO = 76
    AUTHORIZATION = 5
    BANDWIDTH = 6
    BLOCKSIZE = 7
    CACHE_CONTROL = 8
    CLIENT_CHALLENGE = 40
    CLIENT_ID = 46
    COMPANY_ID = 47
    CONFERENCE = 9
    CONNECTION = 10
    CONTENT_BASE = 11
    CONTENT_ENCODING = 12
    CONTENT_LANGUAGE = 13
    CONTENT_LENGTH = 14
    CONTENT_LOCATION = 15
    CONTENT_TYPE = 16
    CSEQ = 17
    DATE = 18
    ETAG = 54
    EXPIRES = 19
    FRAMES = 87
    FROM = 20
    GUID = 48
    HOST = 77
    IF_MATCH = 55
    IF_MODIFIED_SINCE = 21
    INVALID = 0
    KEYMGMT = 82
    LANGUAGE = 51
    LAST = 89
    LAST_MODIFIED = 22
    LOCATION = 53
    MAX_ASM_WIDTH = 50
    MEDIA_PROPERTIES = 84
    PIPELINED_REQUESTS = 83
    PLAYER_START_TIME = 52
    PRAGMA = 78
    PROXY_AUTHENTICATE = 23
    PROXY_REQUIRE = 24
    PUBLIC = 25
    RANGE = 26
    RATE_CONTROL = 88
    REAL_CHALLENGE1 = 41
    REAL_CHALLENGE2 = 42
    REAL_CHALLENGE3 = 43
    REFERER = 27
    REGION_DATA = 49
    REQUIRE = 28
    RETRY_AFTER = 29
    RTCP_INTERVAL = 81
    RTP_INFO = 30
    SCALE = 31
    SEEK_STYLE = 85
    SERVER = 33
    SESSION = 32
    SPEED = 34
    SUBSCRIBE = 44
    SUPPORTED = 57
    TIMESTAMP = 75
    TRANSPORT = 35
    UNSUPPORTED = 36
    USER_AGENT = 37
    VARY = 58
    VIA = 38
    WWW_AUTHENTICATE = 39
    X_ACCELERATE_STREAMING = 59
    X_ACCEPT_AUTHENT = 60
    X_ACCEPT_PROXY_AUTHENT = 61
    X_BROADCAST_ID = 62
    X_BURST_STREAMING = 63
    X_NOTICE = 64
    X_PLAYER_LAG_TIME = 65
    X_PLAYLIST = 66
    X_PLAYLIST_CHANGE_NOTICE = 67
    X_PLAYLIST_GEN_ID = 68
    X_PLAYLIST_SEEK_ID = 69
    X_PROXY_CLIENT_AGENT = 70
    X_PROXY_CLIENT_VERB = 71
    X_RECEDING_PLAYLISTCHANGE = 72
    X_RTP_INFO = 73
    X_SERVER_IP_ADDRESS = 79
    X_SESSIONCOOKIE = 80
    X_STARTUPPROFILE = 74

class RTSPMsgType(GObject.GEnum):
    DATA = 5
    HTTP_REQUEST = 3
    HTTP_RESPONSE = 4
    INVALID = 0
    REQUEST = 1
    RESPONSE = 2

class RTSPRangeUnit(GObject.GEnum):
    CLOCK = 4
    NPT = 3
    SMPTE = 0
    SMPTE_25 = 2
    SMPTE_30_DROP = 1

class RTSPResult(GObject.GEnum):
    EEOF = -11
    EINTR = -3
    EINVAL = -2
    ELAST = -17
    ENET = -12
    ENOMEM = -4
    ENOTIMPL = -6
    ENOTIP = -13
    EPARSE = -8
    ERESOLV = -5
    ERROR = -1
    ESYS = -7
    ETGET = -15
    ETIMEOUT = -14
    ETPOST = -16
    EWSASTART = -9
    EWSAVERSION = -10
    OK = 0

class RTSPState(GObject.GEnum):
    INIT = 1
    INVALID = 0
    PLAYING = 4
    READY = 2
    RECORDING = 5
    SEEKING = 3

class RTSPStatusCode(GObject.GEnum):
    AGGREGATE_OPERATION_NOT_ALLOWED = 459
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
    CONFERENCE_NOT_FOUND = 452
    CONTINUE = 100
    CREATED = 201
    DESTINATION_UNREACHABLE = 462
    FORBIDDEN = 403
    GATEWAY_TIMEOUT = 504
    GONE = 410
    HEADER_FIELD_NOT_VALID_FOR_RESOURCE = 456
    INTERNAL_SERVER_ERROR = 500
    INVALID = 0
    INVALID_RANGE = 457
    KEY_MANAGEMENT_FAILURE = 463
    LENGTH_REQUIRED = 411
    LOW_ON_STORAGE = 250
    METHOD_NOT_ALLOWED = 405
    METHOD_NOT_VALID_IN_THIS_STATE = 455
    MOVED_PERMANENTLY = 301
    MOVE_TEMPORARILY = 302
    MULTIPLE_CHOICES = 300
    NOT_ACCEPTABLE = 406
    NOT_ENOUGH_BANDWIDTH = 453
    NOT_FOUND = 404
    NOT_IMPLEMENTED = 501
    NOT_MODIFIED = 304
    OK = 200
    ONLY_AGGREGATE_OPERATION_ALLOWED = 460
    OPTION_NOT_SUPPORTED = 551
    PARAMETER_IS_READONLY = 458
    PARAMETER_NOT_UNDERSTOOD = 451
    PAYMENT_REQUIRED = 402
    PRECONDITION_FAILED = 412
    PROXY_AUTH_REQUIRED = 407
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_TIMEOUT = 408
    REQUEST_URI_TOO_LARGE = 414
    RTSP_VERSION_NOT_SUPPORTED = 505
    SEE_OTHER = 303
    SERVICE_UNAVAILABLE = 503
    SESSION_NOT_FOUND = 454
    UNAUTHORIZED = 401
    UNSUPPORTED_MEDIA_TYPE = 415
    UNSUPPORTED_TRANSPORT = 461
    USE_PROXY = 305

class RTSPTimeType(GObject.GEnum):
    END = 2
    FRAMES = 3
    NOW = 1
    SECONDS = 0
    UTC = 4

class RTSPVersion(GObject.GEnum):
    INVALID = 0
    @staticmethod
    def as_text(version: RTSPVersion) -> str: ...
