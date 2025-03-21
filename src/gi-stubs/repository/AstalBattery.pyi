import typing

from gi.repository import GLib
from gi.repository import GObject
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalBattery"
_version: str = "0.1"

def get_default() -> Device: ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)
        new(path:GLib.ObjectPath) -> AstalBattery.Device

    Object AstalBatteryDevice

    Properties from AstalBatteryDevice:
      device-type -> AstalBatteryType: device-type
        device-type
      native-path -> gchararray: native-path
        native-path
      vendor -> gchararray: vendor
        vendor
      model -> gchararray: model
        model
      serial -> gchararray: serial
        serial
      update-time -> guint64: update-time
        update-time
      power-supply -> gboolean: power-supply
        power-supply
      online -> gboolean: online
        online
      energy -> gdouble: energy
        energy
      energy-empty -> gdouble: energy-empty
        energy-empty
      energy-full -> gdouble: energy-full
        energy-full
      energy-full-design -> gdouble: energy-full-design
        energy-full-design
      energy-rate -> gdouble: energy-rate
        energy-rate
      voltage -> gdouble: voltage
        voltage
      charge-cycles -> gint: charge-cycles
        charge-cycles
      luminosity -> gdouble: luminosity
        luminosity
      time-to-empty -> gint64: time-to-empty
        time-to-empty
      time-to-full -> gint64: time-to-full
        time-to-full
      percentage -> gdouble: percentage
        percentage
      temperature -> gdouble: temperature
        temperature
      is-present -> gboolean: is-present
        is-present
      state -> AstalBatteryState: state
        state
      is-rechargable -> gboolean: is-rechargable
        is-rechargable
      capacity -> gdouble: capacity
        capacity
      technology -> AstalBatteryTechnology: technology
        technology
      warning-level -> AstalBatteryWarningLevel: warning-level
        warning-level
      battery-level -> AstalBatteryBatteryLevel: battery-level
        battery-level
      icon-name -> gchararray: icon-name
        icon-name
      charging -> gboolean: charging
        charging
      is-battery -> gboolean: is-battery
        is-battery
      battery-icon-name -> gchararray: battery-icon-name
        battery-icon-name
      device-type-name -> gchararray: device-type-name
        device-type-name
      device-type-icon -> gchararray: device-type-icon
        device-type-icon

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        device_type: Type
        native_path: str
        vendor: str
        model: str
        serial: str
        update_time: int
        power_supply: bool
        online: bool
        energy: float
        energy_empty: float
        energy_full: float
        energy_full_design: float
        energy_rate: float
        voltage: float
        charge_cycles: int
        luminosity: float
        time_to_empty: int
        time_to_full: int
        percentage: float
        temperature: float
        is_present: bool
        state: State
        is_rechargable: bool
        capacity: float
        technology: Technology
        warning_level: WarningLevel
        battery_level: BatteryLevel
        icon_name: str
        charging: bool
        is_battery: bool
        battery_icon_name: str
        device_type_name: str
        device_type_icon: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: DevicePrivate = ...
    def __init__(self, device_type: Type = ...,
                 native_path: str = ...,
                 vendor: str = ...,
                 model: str = ...,
                 serial: str = ...,
                 update_time: int = ...,
                 power_supply: bool = ...,
                 online: bool = ...,
                 energy: float = ...,
                 energy_empty: float = ...,
                 energy_full: float = ...,
                 energy_full_design: float = ...,
                 energy_rate: float = ...,
                 voltage: float = ...,
                 charge_cycles: int = ...,
                 luminosity: float = ...,
                 time_to_empty: int = ...,
                 time_to_full: int = ...,
                 percentage: float = ...,
                 temperature: float = ...,
                 is_present: bool = ...,
                 state: State = ...,
                 is_rechargable: bool = ...,
                 capacity: float = ...,
                 technology: Technology = ...,
                 warning_level: WarningLevel = ...,
                 battery_level: BatteryLevel = ...,
                 icon_name: str = ...,
                 charging: bool = ...,
                 is_battery: bool = ...,
                 battery_icon_name: str = ...,
                 device_type_name: str = ...,
                 device_type_icon: str = ...) -> None: ...
    def get_battery_icon_name(self) -> str: ...
    def get_battery_level(self) -> BatteryLevel: ...
    def get_capacity(self) -> float: ...
    def get_charge_cycles(self) -> int: ...
    def get_charging(self) -> bool: ...
    @staticmethod
    def get_default() -> typing.Optional[Device]: ...
    def get_device_type(self) -> Type: ...
    def get_device_type_icon(self) -> str: ...
    def get_device_type_name(self) -> str: ...
    def get_energy(self) -> float: ...
    def get_energy_empty(self) -> float: ...
    def get_energy_full(self) -> float: ...
    def get_energy_full_design(self) -> float: ...
    def get_energy_rate(self) -> float: ...
    def get_icon_name(self) -> str: ...
    def get_is_battery(self) -> bool: ...
    def get_is_present(self) -> bool: ...
    def get_is_rechargable(self) -> bool: ...
    def get_luminosity(self) -> float: ...
    def get_model(self) -> str: ...
    def get_native_path(self) -> str: ...
    def get_online(self) -> bool: ...
    def get_percentage(self) -> float: ...
    def get_power_supply(self) -> bool: ...
    def get_serial(self) -> str: ...
    def get_state(self) -> State: ...
    def get_technology(self) -> Technology: ...
    def get_temperature(self) -> float: ...
    def get_time_to_empty(self) -> int: ...
    def get_time_to_full(self) -> int: ...
    def get_update_time(self) -> int: ...
    def get_vendor(self) -> str: ...
    def get_voltage(self) -> float: ...
    def get_warning_level(self) -> WarningLevel: ...
    @classmethod
    def new(cls, path: GLib.ObjectPath) -> Device: ...
    

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """
    parent_class: GObject.ObjectClass = ...

class DevicePrivate(GObject.GPointer): ...

class UPower(GObject.Object):
    """
    :Constructors:

    ::

        UPower(**properties)
        new() -> AstalBattery.UPower

    Object AstalBatteryUPower

    Signals from AstalBatteryUPower:
      device-added (AstalBatteryDevice)
      device-removed (AstalBatteryDevice)

    Properties from AstalBatteryUPower:
      devices -> gpointer: devices
        devices
      display-device -> AstalBatteryDevice: display-device
        display-device
      daemon-version -> gchararray: daemon-version
        daemon-version
      on-battery -> gboolean: on-battery
        on-battery
      lid-is-closed -> gboolean: lid-is-closed
        lid-is-closed
      lid-is-present -> gboolean: lid-is-present
        lid-is-present
      critical-action -> gchararray: critical-action
        critical-action

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        devices: list[Device]
        display_device: Device
        daemon_version: str
        on_battery: bool
        lid_is_closed: bool
        lid_is_present: bool
        critical_action: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: UPowerPrivate = ...
    def get_critical_action(self) -> str: ...
    def get_daemon_version(self) -> str: ...
    def get_devices(self) -> list[Device]: ...
    def get_display_device(self) -> Device: ...
    def get_lid_is_closed(self) -> bool: ...
    def get_lid_is_present(self) -> bool: ...
    def get_on_battery(self) -> bool: ...
    @classmethod
    def new(cls) -> UPower: ...
    

class UPowerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UPowerClass()
    """
    parent_class: GObject.ObjectClass = ...

class UPowerPrivate(GObject.GPointer): ...

class BatteryLevel(GObject.GEnum):
    CRITICIAL = 3
    FULL = 6
    HIGH = 5
    LOW = 2
    NONE = 1
    NORMAL = 4
    UNKNOWN = 0

class State(GObject.GEnum):
    CHARGING = 1
    DISCHARGING = 2
    EMPTY = 3
    FULLY_CHARGED = 4
    PENDING_CHARGE = 5
    PENDING_DISCHARGE = 6
    UNKNOWN = 0

class Technology(GObject.GEnum):
    LEAD_ACID = 4
    LITHIUM_ION = 1
    LITHIUM_IRON_PHOSPHATE = 3
    LITHIUM_POLYMER = 2
    NICKEL_CADMIUM = 5
    NICKEL_METAL_HYDRIDE = 6
    UNKNOWN = 0

class Type(GObject.GEnum):
    BATTERY = 2
    BLUETOOTH_GENERIC = 28
    CAMERA = 25
    COMPUTER = 11
    GAMING_INPUT = 12
    HEADPHONES = 19
    HEADSET = 17
    KEYBOARD = 6
    LINE_POWER = 1
    MEDIA_PLAYER = 9
    MODEM = 15
    MONITOR = 4
    MOUSE = 5
    NETWORK = 16
    OTHER_AUDIO = 21
    PDA = 7
    PEN = 13
    PHONE = 8
    PRINTER = 23
    REMOVE_CONTROL = 22
    SCANNER = 24
    SPEAKERS = 18
    TABLET = 10
    TOUCHPAD = 14
    TOY = 27
    UNKNOWN = 0
    UPS = 3
    VIDEO = 20
    WEARABLE = 26

class WarningLevel(GObject.GEnum):
    ACTION = 5
    CRITICIAL = 4
    DISCHARGING = 2
    LOW = 3
    NONE = 1
    UNKNOWN = 0


