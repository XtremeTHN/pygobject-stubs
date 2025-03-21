import typing

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalBluetooth"
_version: str = "0.1"

def get_default() -> Bluetooth: ...

class Adapter(GObject.Object):
    """
    :Constructors:

    ::

        Adapter(**properties)

    Object AstalBluetoothAdapter

    Properties from AstalBluetoothAdapter:
      object-path -> gchararray: object-path
        object-path
      uuids -> GStrv: uuids
        uuids
      discovering -> gboolean: discovering
        discovering
      modalias -> gchararray: modalias
        modalias
      name -> gchararray: name
        name
      class -> guint: class
        class
      address -> gchararray: address
        address
      discoverable -> gboolean: discoverable
        discoverable
      pairable -> gboolean: pairable
        pairable
      powered -> gboolean: powered
        powered
      alias -> gchararray: alias
        alias
      discoverable-timeout -> guint: discoverable-timeout
        discoverable-timeout
      pairable-timeout -> guint: pairable-timeout
        pairable-timeout

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        uuids: list[str]
        discovering: bool
        modalias: str
        name: str
        address: str
        discoverable: bool
        pairable: bool
        powered: bool
        alias: str
        discoverable_timeout: int
        pairable_timeout: int
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: AdapterPrivate = ...
    def __init__(self, discoverable: bool = ...,
                 pairable: bool = ...,
                 powered: bool = ...,
                 alias: str = ...,
                 discoverable_timeout: int = ...,
                 pairable_timeout: int = ...) -> None: ...
    def get_address(self) -> str: ...
    def get_alias(self) -> str: ...
    def get_class(self) -> int: ...
    def get_discoverable(self) -> bool: ...
    def get_discoverable_timeout(self) -> int: ...
    def get_discovering(self) -> bool: ...
    def get_modalias(self) -> str: ...
    def get_name(self) -> str: ...
    def get_pairable(self) -> bool: ...
    def get_pairable_timeout(self) -> int: ...
    def get_powered(self) -> bool: ...
    def get_uuids(self) -> list[str]: ...
    def remove_device(self, device: Device) -> None: ...
    def set_alias(self, value: str) -> None: ...
    def set_discoverable(self, value: bool) -> None: ...
    def set_discoverable_timeout(self, value: int) -> None: ...
    def set_pairable(self, value: bool) -> None: ...
    def set_pairable_timeout(self, value: int) -> None: ...
    def set_powered(self, value: bool) -> None: ...
    def start_discovery(self) -> None: ...
    def stop_discovery(self) -> None: ...
    

class AdapterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AdapterClass()
    """
    parent_class: GObject.ObjectClass = ...

class AdapterPrivate(GObject.GPointer): ...

class Bluetooth(GObject.Object):
    """
    :Constructors:

    ::

        Bluetooth(**properties)
        new() -> AstalBluetooth.Bluetooth

    Object AstalBluetoothBluetooth

    Signals from AstalBluetoothBluetooth:
      device-added (AstalBluetoothDevice)
      device-removed (AstalBluetoothDevice)
      adapter-added (AstalBluetoothAdapter)
      adapter-removed (AstalBluetoothAdapter)

    Properties from AstalBluetoothBluetooth:
      is-powered -> gboolean: is-powered
        is-powered
      is-connected -> gboolean: is-connected
        is-connected
      adapter -> AstalBluetoothAdapter: adapter
        adapter
      adapters -> gpointer: adapters
        adapters
      devices -> gpointer: devices
        devices

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        is_powered: bool
        is_connected: bool
        adapter: Adapter
        adapters: list[Adapter]
        devices: list[Device]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: BluetoothPrivate = ...
    def __init__(self, is_powered: bool = ...,
                 is_connected: bool = ...) -> None: ...
    def get_adapter(self) -> typing.Optional[Adapter]: ...
    def get_adapters(self) -> list[Adapter]: ...
    @staticmethod
    def get_default() -> Bluetooth: ...
    def get_devices(self) -> list[Device]: ...
    def get_is_connected(self) -> bool: ...
    def get_is_powered(self) -> bool: ...
    @classmethod
    def new(cls) -> Bluetooth: ...
    def toggle(self) -> None: ...
    

class BluetoothClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BluetoothClass()
    """
    parent_class: GObject.ObjectClass = ...
    device_added: typing.Callable[[Bluetooth, Device], None] = ...
    device_removed: typing.Callable[[Bluetooth, Device], None] = ...
    adapter_added: typing.Callable[[Bluetooth, Adapter], None] = ...
    adapter_removed: typing.Callable[[Bluetooth, Adapter], None] = ...

class BluetoothPrivate(GObject.GPointer): ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object AstalBluetoothDevice

    Properties from AstalBluetoothDevice:
      object-path -> gchararray: object-path
        object-path
      uuids -> GStrv: uuids
        uuids
      connected -> gboolean: connected
        connected
      legacy-pairing -> gboolean: legacy-pairing
        legacy-pairing
      paired -> gboolean: paired
        paired
      rssi -> gint: rssi
        rssi
      adapter -> gchararray: adapter
        adapter
      address -> gchararray: address
        address
      icon -> gchararray: icon
        icon
      modalias -> gchararray: modalias
        modalias
      name -> gchararray: name
        name
      appearance -> guint: appearance
        appearance
      class -> guint: class
        class
      connecting -> gboolean: connecting
        connecting
      blocked -> gboolean: blocked
        blocked
      trusted -> gboolean: trusted
        trusted
      battery-percentage -> gdouble: battery-percentage
        battery-percentage
      alias -> gchararray: alias
        alias

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        uuids: list[str]
        connected: bool
        legacy_pairing: bool
        paired: bool
        rssi: int
        adapter: GLib.ObjectPath
        address: str
        icon: str
        modalias: str
        name: str
        appearance: int
        connecting: bool
        blocked: bool
        trusted: bool
        battery_percentage: float
        alias: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DevicePrivate = ...
    def __init__(self, connecting: bool = ...,
                 blocked: bool = ...,
                 trusted: bool = ...,
                 alias: str = ...) -> None: ...
    def cancel_pairing(self) -> None: ...
    def connect_device(self, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def connect_device_finish(self, _res_: Gio.AsyncResult) -> None: ...
    def connect_profile(self, uuid: str) -> None: ...
    def disconnect_device(self, _callback_: typing.Optional[typing.Callable[..., None]] = None, *_callback__target: typing.Any) -> None: ...
    def disconnect_device_finish(self, _res_: Gio.AsyncResult) -> None: ...
    def disconnect_profile(self, uuid: str) -> None: ...
    def get_adapter(self) -> GLib.ObjectPath: ...
    def get_address(self) -> str: ...
    def get_alias(self) -> str: ...
    def get_appearance(self) -> int: ...
    def get_battery_percentage(self) -> float: ...
    def get_blocked(self) -> bool: ...
    def get_class(self) -> int: ...
    def get_connected(self) -> bool: ...
    def get_connecting(self) -> bool: ...
    def get_icon(self) -> str: ...
    def get_legacy_pairing(self) -> bool: ...
    def get_modalias(self) -> str: ...
    def get_name(self) -> str: ...
    def get_paired(self) -> bool: ...
    def get_rssi(self) -> int: ...
    def get_trusted(self) -> bool: ...
    def get_uuids(self) -> list[str]: ...
    def pair(self) -> None: ...
    def set_alias(self, value: str) -> None: ...
    def set_blocked(self, value: bool) -> None: ...
    def set_trusted(self, value: bool) -> None: ...
    

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """
    parent_class: GObject.ObjectClass = ...

class DevicePrivate(GObject.GPointer): ...


