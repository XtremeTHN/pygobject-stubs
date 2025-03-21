import typing

from gi.repository import GObject
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalWp"
_version: str = "0.1"

def get_default() -> typing.Optional[Wp]: ...

class Audio(GObject.Object):
    """
    :Constructors:

    ::

        Audio(**properties)
        new(wp:AstalWp.Wp) -> AstalWp.Audio

    Object AstalWpAudio

    Signals from AstalWpAudio:
      microphone-added (AstalWpEndpoint)
      microphone-removed (AstalWpEndpoint)
      speaker-added (AstalWpEndpoint)
      speaker-removed (AstalWpEndpoint)
      stream-added (AstalWpEndpoint)
      stream-removed (AstalWpEndpoint)
      recorder-added (AstalWpEndpoint)
      recorder-removed (AstalWpEndpoint)
      device-added (AstalWpDevice)
      device-removed (AstalWpDevice)

    Properties from AstalWpAudio:
      microphones -> gpointer: microphones
        microphones
      speakers -> gpointer: speakers
        speakers
      streams -> gpointer: streams
        streams
      recorders -> gpointer: recorders
        recorders
      devices -> gpointer: devices
        devices
      default-speaker -> AstalWpEndpoint: default-speaker
        default-speaker
      default-microphone -> AstalWpEndpoint: default-microphone
        default-microphone

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        default_microphone: typing.Optional[Endpoint]
        default_speaker: typing.Optional[Endpoint]
        devices: typing.Optional[list[Device]]
        microphones: typing.Optional[list[Endpoint]]
        recorders: typing.Optional[list[Endpoint]]
        speakers: typing.Optional[list[Endpoint]]
        streams: typing.Optional[list[Endpoint]]
    props: Props = ...
    def get_default_microphone(self) -> typing.Optional[Endpoint]: ...
    def get_default_speaker(self) -> typing.Optional[Endpoint]: ...
    def get_device(self, id: int) -> typing.Optional[Device]: ...
    def get_devices(self) -> typing.Optional[list[Device]]: ...
    def get_endpoint(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_microphone(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_microphones(self) -> typing.Optional[list[Endpoint]]: ...
    def get_recorder(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_recorders(self) -> typing.Optional[list[Endpoint]]: ...
    def get_speaker(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_speakers(self) -> typing.Optional[list[Endpoint]]: ...
    def get_stream(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_streams(self) -> typing.Optional[list[Endpoint]]: ...
    @classmethod
    def new(cls, wp: Wp) -> Audio: ...
    

class AudioClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioClass()
    """
    parent_class: GObject.ObjectClass = ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object AstalWpDevice

    Properties from AstalWpDevice:
      id -> guint: id
        id
      description -> gchararray: description
        description
      icon -> gchararray: icon
        icon
      profiles -> gpointer: profiles
        profiles
      active-profile-id -> gint: active-profile-id
        active-profile-id
      device-type -> AstalWpDeviceType: device-type
        device-type

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        active_profile_id: int
        description: str
        device_type: DeviceType
        icon: str
        id: int
        profiles: typing.Optional[list[Profile]]
    props: Props = ...
    def __init__(self, active_profile_id: int = ...) -> None: ...
    def get_active_profile(self) -> int: ...
    def get_description(self) -> str: ...
    def get_device_type(self) -> DeviceType: ...
    def get_icon(self) -> str: ...
    def get_id(self) -> int: ...
    def get_profile(self, id: int) -> typing.Optional[Profile]: ...
    def get_profiles(self) -> typing.Optional[list[Profile]]: ...
    def set_active_profile(self, profile_id: int) -> None: ...
    

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """
    parent_class: GObject.ObjectClass = ...

class Endpoint(GObject.Object):
    """
    :Constructors:

    ::

        Endpoint(**properties)

    Object AstalWpEndpoint

    Properties from AstalWpEndpoint:
      id -> guint: id
        id
      volume -> gdouble: volume
        volume
      mute -> gboolean: mute
        mute
      description -> gchararray: description
        description
      name -> gchararray: name
        name
      media-class -> AstalWpMediaClass: media-class
        media-class
      is-default -> gboolean: is-default
        is-default
      icon -> gchararray: icon
        icon
      volume-icon -> gchararray: volume-icon
        volume-icon
      lock-channels -> gboolean: lock-channels
        lock channels
      serial -> guint: serial
        serial
      path -> gchararray: path
        path

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        description: str
        icon: str
        id: int
        is_default: bool
        lock_channels: bool
        media_class: MediaClass
        mute: bool
        name: str
        path: str
        serial: int
        volume: float
        volume_icon: str
    props: Props = ...
    def __init__(self, icon: str = ...,
                 is_default: bool = ...,
                 lock_channels: bool = ...,
                 mute: bool = ...,
                 volume: float = ...) -> None: ...
    def get_description(self) -> str: ...
    def get_icon(self) -> str: ...
    def get_id(self) -> int: ...
    def get_is_default(self) -> bool: ...
    def get_lock_channels(self) -> bool: ...
    def get_media_class(self) -> MediaClass: ...
    def get_mute(self) -> bool: ...
    def get_name(self) -> str: ...
    def get_path(self) -> str: ...
    def get_serial(self) -> int: ...
    def get_volume(self) -> float: ...
    def get_volume_icon(self) -> str: ...
    def set_is_default(self, is_default: bool) -> None: ...
    def set_lock_channels(self, lock_channels: bool) -> None: ...
    def set_mute(self, mute: bool) -> None: ...
    def set_volume(self, volume: float) -> None: ...
    

class EndpointClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EndpointClass()
    """
    parent_class: GObject.ObjectClass = ...

class Profile(GObject.Object):
    """
    :Constructors:

    ::

        Profile(**properties)

    Object AstalWpProfile

    Properties from AstalWpProfile:
      index -> gint: index
        index
      description -> gchararray: description
        description

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        description: str
        index: int
    props: Props = ...
    def __init__(self, description: str = ...,
                 index: int = ...) -> None: ...
    def get_description(self) -> str: ...
    def get_index(self) -> int: ...
    

class ProfileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProfileClass()
    """
    parent_class: GObject.ObjectClass = ...

class Video(GObject.Object):
    """
    :Constructors:

    ::

        Video(**properties)
        new(wp:AstalWp.Wp) -> AstalWp.Video

    Object AstalWpVideo

    Signals from AstalWpVideo:
      stream-added (AstalWpEndpoint)
      stream-removed (AstalWpEndpoint)
      recorder-added (AstalWpEndpoint)
      recorder-removed (AstalWpEndpoint)
      device-added (AstalWpDevice)
      device-removed (AstalWpDevice)
      source-added (AstalWpEndpoint)
      source-removed (AstalWpEndpoint)
      sink-added (AstalWpEndpoint)
      sink-removed (AstalWpEndpoint)

    Properties from AstalWpVideo:
      sources -> gpointer: sources
        sources
      sinks -> gpointer: sinks
        sinks
      streams -> gpointer: streams
        streams
      recorders -> gpointer: recorders
        recorders
      devices -> gpointer: devices
        devices

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        devices: typing.Optional[list[Endpoint]]
        recorders: typing.Optional[None]
        sinks: typing.Optional[list[Endpoint]]
        sources: typing.Optional[list[Endpoint]]
        streams: typing.Optional[list[Endpoint]]
    props: Props = ...
    def get_device(self, id: int) -> typing.Optional[Device]: ...
    def get_devices(self) -> typing.Optional[list[Device]]: ...
    def get_recorder(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_recorders(self) -> typing.Optional[list[Endpoint]]: ...
    def get_sink(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_sinks(self) -> typing.Optional[list[Endpoint]]: ...
    def get_source(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_sources(self) -> typing.Optional[list[Endpoint]]: ...
    def get_stream(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_streams(self) -> typing.Optional[list[Endpoint]]: ...
    @classmethod
    def new(cls, wp: Wp) -> Video: ...
    

class VideoClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VideoClass()
    """
    parent_class: GObject.ObjectClass = ...

class Wp(GObject.Object):
    """
    :Constructors:

    ::

        Wp(**properties)

    Object AstalWpWp

    Signals from AstalWpWp:
      device-added (AstalWpDevice)
      device-removed (AstalWpDevice)
      endpoint-added (AstalWpEndpoint)
      endpoint-removed (AstalWpEndpoint)

    Properties from AstalWpWp:
      audio -> AstalWpAudio: audio
        audio
      video -> AstalWpVideo: video
        video
      endpoints -> gpointer: endpoints
        endpoints
      devices -> gpointer: devices
        devices
      default-speaker -> AstalWpEndpoint: default-speaker
        default-speaker
      default-microphone -> AstalWpEndpoint: default-microphone
        default-microphone
      scale -> AstalWpScale: scale
        scale

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        audio: typing.Optional[Audio]
        default_microphone: typing.Optional[Endpoint]
        default_speaker: typing.Optional[Endpoint]
        devices: typing.Optional[list[Device]]
        endpoints: typing.Optional[list[Endpoint]]
        scale: Scale
        video: typing.Optional[Video]
    props: Props = ...
    def __init__(self, scale: Scale = ...) -> None: ...
    def get_audio(self) -> typing.Optional[Audio]: ...
    @staticmethod
    def get_default() -> typing.Optional[Wp]: ...
    def get_default_microphone(self) -> typing.Optional[Endpoint]: ...
    def get_default_speaker(self) -> typing.Optional[Endpoint]: ...
    def get_device(self, id: int) -> typing.Optional[Device]: ...
    def get_devices(self) -> typing.Optional[list[Device]]: ...
    def get_endpoint(self, id: int) -> typing.Optional[Endpoint]: ...
    def get_endpoints(self) -> typing.Optional[list[Endpoint]]: ...
    def get_scale(self) -> Scale: ...
    def get_video(self) -> typing.Optional[Video]: ...
    def set_scale(self, scale: Scale) -> None: ...
    

class WpClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WpClass()
    """
    parent_class: GObject.ObjectClass = ...

class DeviceType(GObject.GEnum):
    AUDIO = 0
    VIDEO = 1

class MediaClass(GObject.GEnum):
    AUDIO_MICROPHONE = 0
    AUDIO_RECORDER = 2
    AUDIO_SPEAKER = 1
    AUDIO_STREAM = 3
    VIDEO_RECORDER = 6
    VIDEO_SINK = 5
    VIDEO_SOURCE = 4
    VIDEO_STREAM = 7

class Scale(GObject.GEnum):
    CUBIC = 1
    LINEAR = 0


