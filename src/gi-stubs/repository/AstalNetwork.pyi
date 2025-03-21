import typing

from gi.repository import GObject
from gi.repository import NM
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalNetwork"
_version: str = "0.1"

def connectivity_to_string() -> str: ...
def device_state_to_string() -> str: ...
def get_default() -> Network: ...
def internet_from_device(device: NM.Device) -> Internet: ...
def internet_to_string() -> str: ...
def primary_from_connection_type(type: str) -> Primary: ...
def primary_to_string() -> str: ...
def state_to_string() -> str: ...

class AccessPoint(GObject.Object):
    """
    :Constructors:

    ::

        AccessPoint(**properties)

    Object AstalNetworkAccessPoint

    Properties from AstalNetworkAccessPoint:
      bandwidth -> guint: bandwidth
        bandwidth
      bssid -> gchararray: bssid
        bssid
      frequency -> guint: frequency
        frequency
      last-seen -> gint: last-seen
        last-seen
      max-bitrate -> guint: max-bitrate
        max-bitrate
      strength -> guchar: strength
        strength
      icon-name -> gchararray: icon-name
        icon-name
      mode -> NM80211Mode: mode
        mode
      flags -> NM80211ApFlags: flags
        flags
      rsn-flags -> NM80211ApSecurityFlags: rsn-flags
        rsn-flags
      wpa-flags -> NM80211ApSecurityFlags: wpa-flags
        wpa-flags
      ssid -> gchararray: ssid
        ssid

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        bandwidth: int
        bssid: str
        frequency: int
        last_seen: int
        max_bitrate: int
        strength: int
        icon_name: str
        mode: NM.80211Mode
        flags: NM.80211ApFlags
        rsn_flags: NM.80211ApSecurityFlags
        wpa_flags: NM.80211ApSecurityFlags
        ssid: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: AccessPointPrivate = ...
    def __init__(self, icon_name: str = ...) -> None: ...
    def get_bandwidth(self) -> int: ...
    def get_bssid(self) -> str: ...
    def get_flags(self) -> NM.80211ApFlags: ...
    def get_frequency(self) -> int: ...
    def get_icon_name(self) -> str: ...
    def get_last_seen(self) -> int: ...
    def get_max_bitrate(self) -> int: ...
    def get_mode(self) -> NM.80211Mode: ...
    def get_rsn_flags(self) -> NM.80211ApSecurityFlags: ...
    def get_ssid(self) -> typing.Optional[str]: ...
    def get_strength(self) -> int: ...
    def get_wpa_flags(self) -> NM.80211ApSecurityFlags: ...
    

class AccessPointClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AccessPointClass()
    """
    parent_class: GObject.ObjectClass = ...

class AccessPointPrivate(GObject.GPointer): ...

class Network(GObject.Object):
    """
    :Constructors:

    ::

        Network(**properties)
        new() -> AstalNetwork.Network

    Object AstalNetworkNetwork

    Properties from AstalNetworkNetwork:
      client -> NMClient: client
        client
      wifi -> AstalNetworkWifi: wifi
        wifi
      wired -> AstalNetworkWired: wired
        wired
      primary -> AstalNetworkPrimary: primary
        primary
      connectivity -> AstalNetworkConnectivity: connectivity
        connectivity
      state -> AstalNetworkState: state
        state

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        client: NM.Client
        wifi: Wifi
        wired: Wired
        primary: Primary
        connectivity: Connectivity
        state: State
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: NetworkPrivate = ...
    def __init__(self, client: NM.Client = ...,
                 wifi: Wifi = ...,
                 wired: Wired = ...,
                 primary: Primary = ...) -> None: ...
    def get_client(self) -> NM.Client: ...
    def get_connectivity(self) -> Connectivity: ...
    @staticmethod
    def get_default() -> Network: ...
    def get_primary(self) -> Primary: ...
    def get_state(self) -> State: ...
    def get_wifi(self) -> typing.Optional[Wifi]: ...
    def get_wired(self) -> typing.Optional[Wired]: ...
    @classmethod
    def new(cls) -> Network: ...
    

class NetworkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkClass()
    """
    parent_class: GObject.ObjectClass = ...

class NetworkPrivate(GObject.GPointer): ...

class Wifi(GObject.Object):
    """
    :Constructors:

    ::

        Wifi(**properties)

    Object AstalNetworkWifi

    Signals from AstalNetworkWifi:
      state-changed (AstalNetworkDeviceState, AstalNetworkDeviceState, NMDeviceStateReason)

    Properties from AstalNetworkWifi:
      device -> NMDeviceWifi: device
        device
      active-connection -> NMActiveConnection: active-connection
        active-connection
      active-access-point -> AstalNetworkAccessPoint: active-access-point
        active-access-point
      access-points -> gpointer: access-points
        access-points
      enabled -> gboolean: enabled
        enabled
      internet -> AstalNetworkInternet: internet
        internet
      bandwidth -> guint: bandwidth
        bandwidth
      ssid -> gchararray: ssid
        ssid
      strength -> guchar: strength
        strength
      frequency -> guint: frequency
        frequency
      state -> AstalNetworkDeviceState: state
        state
      icon-name -> gchararray: icon-name
        icon-name
      is-hotspot -> gboolean: is-hotspot
        is-hotspot
      scanning -> gboolean: scanning
        scanning

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        device: NM.DeviceWifi
        active_connection: NM.ActiveConnection
        active_access_point: AccessPoint
        access_points: list[AccessPoint]
        enabled: bool
        internet: Internet
        bandwidth: int
        ssid: str
        strength: int
        frequency: int
        state: DeviceState
        icon_name: str
        is_hotspot: bool
        scanning: bool
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: WifiPrivate = ...
    def __init__(self, device: NM.DeviceWifi = ...,
                 active_connection: NM.ActiveConnection = ...,
                 active_access_point: AccessPoint = ...,
                 enabled: bool = ...,
                 internet: Internet = ...,
                 bandwidth: int = ...,
                 ssid: str = ...,
                 strength: int = ...,
                 frequency: int = ...,
                 state: DeviceState = ...,
                 icon_name: str = ...,
                 is_hotspot: bool = ...,
                 scanning: bool = ...) -> None: ...
    def get_access_points(self) -> list[AccessPoint]: ...
    def get_active_access_point(self) -> typing.Optional[AccessPoint]: ...
    def get_active_connection(self) -> typing.Optional[NM.ActiveConnection]: ...
    def get_bandwidth(self) -> int: ...
    def get_device(self) -> NM.DeviceWifi: ...
    def get_enabled(self) -> bool: ...
    def get_frequency(self) -> int: ...
    def get_icon_name(self) -> str: ...
    def get_internet(self) -> Internet: ...
    def get_is_hotspot(self) -> bool: ...
    def get_scanning(self) -> bool: ...
    def get_ssid(self) -> str: ...
    def get_state(self) -> DeviceState: ...
    def get_strength(self) -> int: ...
    def scan(self) -> None: ...
    def set_device(self, value: NM.DeviceWifi) -> None: ...
    def set_enabled(self, value: bool) -> None: ...
    

class WifiClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WifiClass()
    """
    parent_class: GObject.ObjectClass = ...

class WifiPrivate(GObject.GPointer): ...

class Wired(GObject.Object):
    """
    :Constructors:

    ::

        Wired(**properties)

    Object AstalNetworkWired

    Properties from AstalNetworkWired:
      device -> NMDeviceEthernet: device
        device
      speed -> guint: speed
        speed
      internet -> AstalNetworkInternet: internet
        internet
      state -> AstalNetworkDeviceState: state
        state
      icon-name -> gchararray: icon-name
        icon-name

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        device: NM.DeviceEthernet
        speed: int
        internet: Internet
        state: DeviceState
        icon_name: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: WiredPrivate = ...
    connection: NM.ActiveConnection = ...
    def __init__(self, device: NM.DeviceEthernet = ...,
                 speed: int = ...,
                 internet: Internet = ...,
                 state: DeviceState = ...,
                 icon_name: str = ...) -> None: ...
    def get_device(self) -> NM.DeviceEthernet: ...
    def get_icon_name(self) -> str: ...
    def get_internet(self) -> Internet: ...
    def get_speed(self) -> int: ...
    def get_state(self) -> DeviceState: ...
    def set_device(self, value: NM.DeviceEthernet) -> None: ...
    

class WiredClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WiredClass()
    """
    parent_class: GObject.ObjectClass = ...

class WiredPrivate(GObject.GPointer): ...

class Connectivity(GObject.GEnum):
    FULL = 4
    LIMITED = 3
    NONE = 1
    PORTAL = 2
    UNKNOWN = 0

class DeviceState(GObject.GEnum):
    ACTIVATED = 100
    CONFIG = 50
    DEACTIVATING = 110
    DISCONNECTED = 30
    FAILED = 120
    IP_CHECK = 80
    IP_CONFIG = 70
    NEED_AUTH = 60
    PREPARE = 40
    SECONDARIES = 90
    UNAVAILABLE = 20
    UNKNOWN = 0
    UNMANAGED = 10

class Internet(GObject.GEnum):
    CONNECTED = 0
    CONNECTING = 1
    DISCONNECTED = 2

class Primary(GObject.GEnum):
    UNKNOWN = 0
    WIFI = 2
    WIRED = 1

class State(GObject.GEnum):
    ASLEEP = 10
    CONNECTED_GLOBAL = 70
    CONNECTED_LOCAL = 50
    CONNECTED_SITE = 60
    CONNECTING = 40
    DISCONNECTED = 20
    DISCONNECTING = 30
    UNKNOWN = 0


