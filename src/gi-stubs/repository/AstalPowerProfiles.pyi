import typing

from gi.repository import GObject
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalPowerProfiles"
_version: str = "0.1"

def get_default() -> PowerProfiles: ...

class Hold(GObject.GBoxed):
    """
    :Constructors:

    ::

        Hold()
    """
    application_id: str = ...
    profile: str = ...
    reason: str = ...

class PowerProfiles(GObject.Object):
    """
    :Constructors:

    ::

        PowerProfiles(**properties)
        new() -> AstalPowerProfiles.PowerProfiles

    Object AstalPowerProfilesPowerProfiles

    Signals from AstalPowerProfilesPowerProfiles:
      profile-released (guint)

    Properties from AstalPowerProfilesPowerProfiles:
      active-profile -> gchararray: active-profile
        active-profile
      icon-name -> gchararray: icon-name
        icon-name
      actions -> GStrv: actions
        actions
      performance-degraded -> gchararray: performance-degraded
        performance-degraded
      version -> gchararray: version
        version

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        active_profile: str
        icon_name: str
        actions: list[str]
        performance_degraded: str
        version: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: PowerProfilesPrivate = ...
    def __init__(self, active_profile: str = ...) -> None: ...
    def get_actions(self) -> list[str]: ...
    def get_active_profile(self) -> str: ...
    def get_active_profile_holds(self) -> list[Hold]: ...
    @staticmethod
    def get_default() -> PowerProfiles: ...
    def get_icon_name(self) -> str: ...
    def get_performance_degraded(self) -> str: ...
    def get_profiles(self) -> list[Profile]: ...
    def get_version(self) -> str: ...
    def hold_profile(self, profile: str, reason: str, application_id: str) -> int: ...
    @classmethod
    def new(cls) -> PowerProfiles: ...
    def release_profile(self, cookie: int) -> None: ...
    def set_active_profile(self, value: str) -> None: ...
    

class PowerProfilesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PowerProfilesClass()
    """
    parent_class: GObject.ObjectClass = ...

class PowerProfilesPrivate(GObject.GPointer): ...

class Profile(GObject.GBoxed):
    """
    :Constructors:

    ::

        Profile()
    """
    profile: str = ...
    cpu_driver: str = ...
    platform_driver: str = ...
    driver: str = ...


