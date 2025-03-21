import typing

from gi.repository import GLib
from gi.repository import GObject
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalNotifd"
_version: str = "0.1"

def get_default() -> Notifd: ...

class Action(GObject.GBoxed):
    """
    :Constructors:

    ::

        Action()
    """
    id: str = ...
    label: str = ...

class Notifd(GObject.Object):
    """
    :Constructors:

    ::

        Notifd(**properties)
        new() -> AstalNotifd.Notifd

    Object AstalNotifdNotifd

    Signals from AstalNotifdNotifd:
      active (AstalNotifdActiveType)
      notified (guint, gboolean)
      resolved (guint, AstalNotifdClosedReason)

    Properties from AstalNotifdNotifd:
      ignore-timeout -> gboolean: ignore-timeout
        ignore-timeout
      dont-disturb -> gboolean: dont-disturb
        dont-disturb
      notifications -> gpointer: notifications
        notifications

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        ignore_timeout: bool
        dont_disturb: bool
        notifications: list[Notification]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: NotifdPrivate = ...
    def __init__(self, ignore_timeout: bool = ...,
                 dont_disturb: bool = ...) -> None: ...
    @staticmethod
    def get_default() -> Notifd: ...
    def get_dont_disturb(self) -> bool: ...
    def get_ignore_timeout(self) -> bool: ...
    def get_notification(self, id: int) -> Notification: ...
    def get_notifications(self) -> list[Notification]: ...
    @classmethod
    def new(cls) -> Notifd: ...
    def set_dont_disturb(self, value: bool) -> None: ...
    def set_ignore_timeout(self, value: bool) -> None: ...
    

class NotifdClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NotifdClass()
    """
    parent_class: GObject.ObjectClass = ...

class NotifdPrivate(GObject.GPointer): ...

class Notification(GObject.Object):
    """
    :Constructors:

    ::

        Notification(**properties)

    Object AstalNotifdNotification

    Signals from AstalNotifdNotification:
      resolved (AstalNotifdClosedReason)
      invoked (gchararray)
      dismissed ()

    Properties from AstalNotifdNotification:
      time -> gint64: time
        time
      app-name -> gchararray: app-name
        app-name
      app-icon -> gchararray: app-icon
        app-icon
      summary -> gchararray: summary
        summary
      body -> gchararray: body
        body
      id -> guint: id
        id
      expire-timeout -> gint: expire-timeout
        expire-timeout
      actions -> gpointer: actions
        actions
      image -> gchararray: image
        image
      action-icons -> gboolean: action-icons
        action-icons
      category -> gchararray: category
        category
      desktop-entry -> gchararray: desktop-entry
        desktop-entry
      resident -> gboolean: resident
        resident
      sound-file -> gchararray: sound-file
        sound-file
      sound-name -> gchararray: sound-name
        sound-name
      suppress-sound -> gboolean: suppress-sound
        suppress-sound
      transient -> gboolean: transient
        transient
      x -> gint: x
        x
      y -> gint: y
        y
      urgency -> AstalNotifdUrgency: urgency
        urgency

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        time: int
        app_name: str
        app_icon: str
        summary: str
        body: str
        id: int
        expire_timeout: int
        actions: list[Action]
        image: str
        action_icons: bool
        category: str
        desktop_entry: str
        resident: bool
        sound_file: str
        sound_name: str
        suppress_sound: bool
        transient: bool
        x: int
        y: int
        urgency: Urgency
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: NotificationPrivate = ...
    def __init__(self, time: int = ...,
                 app_name: str = ...,
                 app_icon: str = ...,
                 summary: str = ...,
                 body: str = ...,
                 id: int = ...,
                 expire_timeout: int = ...) -> None: ...
    def dismiss(self) -> None: ...
    def get_action_icons(self) -> bool: ...
    def get_actions(self) -> list[Action]: ...
    def get_app_icon(self) -> str: ...
    def get_app_name(self) -> str: ...
    def get_body(self) -> str: ...
    def get_bool_hint(self, hint: str) -> bool: ...
    def get_byte_hint(self, hint: str) -> int: ...
    def get_category(self) -> str: ...
    def get_desktop_entry(self) -> str: ...
    def get_expire_timeout(self) -> int: ...
    def get_hint(self, hint: str) -> typing.Optional[GLib.Variant]: ...
    def get_id(self) -> int: ...
    def get_image(self) -> str: ...
    def get_int_hint(self, hint: str) -> int: ...
    def get_resident(self) -> bool: ...
    def get_sound_file(self) -> str: ...
    def get_sound_name(self) -> str: ...
    def get_str_hint(self, hint: str) -> str: ...
    def get_summary(self) -> str: ...
    def get_suppress_sound(self) -> bool: ...
    def get_time(self) -> int: ...
    def get_transient(self) -> bool: ...
    def get_urgency(self) -> Urgency: ...
    def get_x(self) -> int: ...
    def get_y(self) -> int: ...
    def invoke(self, action_id: str) -> None: ...
    

class NotificationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NotificationClass()
    """
    parent_class: GObject.ObjectClass = ...

class NotificationPrivate(GObject.GPointer): ...

class ClosedReason(GObject.GEnum):
    CLOSED = 3
    DISMISSED_BY_USER = 2
    EXPIRED = 1
    UNDEFINED = 4

class Urgency(GObject.GEnum):
    CRITICAL = 2
    LOW = 0
    NORMAL = 1


