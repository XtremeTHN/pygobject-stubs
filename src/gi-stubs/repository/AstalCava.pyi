import typing

from gi.repository import GObject
T = typing.TypeVar("T")

_lock = ... # FIXME Constant
_namespace: str = "AstalCava"
_version: str = "0.1"

def get_default() -> typing.Optional[Cava]: ...

class Cava(GObject.Object):
    """
    :Constructors:

    ::

        Cava(**properties)

    Object AstalCavaCava

    Properties from AstalCavaCava:
      values -> GArray: values
        a list of values
      active -> gboolean: active
        active
      bars -> gint: bars
        number of bars per channel
      autosens -> gboolean: autosens
        dynamically adjust sensitivity
      stereo -> gboolean: stereo
        stereo
      noise-reduction -> gdouble: noise_reduction
        noise reduction
      framerate -> gint: framerate
        framerate
      input -> AstalCavaInput: input
        input
      source -> gchararray: source
        source
      channels -> gint: channels
        channels
      low-cutoff -> gint: low-cutoff
        lower frequency cutoff
      high-cutoff -> gint: high-cutoff
        higher frequency cutoff
      samplerate -> gint: samplerate
        samplerate

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        active: bool
        autosens: bool
        bars: int
        channels: int
        framerate: int
        high_cutoff: int
        input: Input
        low_cutoff: int
        noise_reduction: float
        samplerate: int
        source: str
        stereo: bool
        values: list[float]
    props: Props = ...
    def __init__(self, active: bool = ...,
                 autosens: bool = ...,
                 bars: int = ...,
                 channels: int = ...,
                 framerate: int = ...,
                 high_cutoff: int = ...,
                 input: Input = ...,
                 low_cutoff: int = ...,
                 noise_reduction: float = ...,
                 samplerate: int = ...,
                 source: str = ...,
                 stereo: bool = ...) -> None: ...
    def get_active(self) -> bool: ...
    def get_autosens(self) -> bool: ...
    def get_bars(self) -> int: ...
    def get_channels(self) -> int: ...
    @staticmethod
    def get_default() -> typing.Optional[Cava]: ...
    def get_framerate(self) -> int: ...
    def get_high_cutoff(self) -> int: ...
    def get_input(self) -> Input: ...
    def get_low_cutoff(self) -> int: ...
    def get_noise_reduction(self) -> float: ...
    def get_samplerate(self) -> int: ...
    def get_source(self) -> str: ...
    def get_stereo(self) -> bool: ...
    def get_values(self) -> list[float]: ...
    def set_active(self, active: bool) -> None: ...
    def set_autosens(self, autosens: bool) -> None: ...
    def set_bars(self, bars: int) -> None: ...
    def set_channels(self, channels: int) -> None: ...
    def set_framerate(self, framerate: int) -> None: ...
    def set_high_cutoff(self, high_cutoff: int) -> None: ...
    def set_input(self, input: Input) -> None: ...
    def set_low_cutoff(self, low_cutoff: int) -> None: ...
    def set_noise_reduction(self, noise: float) -> None: ...
    def set_samplerate(self, samplerate: int) -> None: ...
    def set_source(self, source: str) -> None: ...
    def set_stereo(self, stereo: bool) -> None: ...
    

class CavaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CavaClass()
    """
    parent_class: GObject.ObjectClass = ...

class Input(GObject.GEnum):
    ALSA = 3
    FIFO = 0
    JACK = 7
    OSS = 6
    PIPEWIRE = 2
    PORTAUDIO = 1
    PULSE = 4
    SHMEM = 8
    SNDIO = 5
    WINSCAP = 9


