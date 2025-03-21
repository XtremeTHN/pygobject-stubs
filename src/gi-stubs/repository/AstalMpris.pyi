import typing

from gi.repository import GLib
from gi.repository import GObject
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalMpris"
_version: str = "0.1"

def get_default() -> Mpris: ...

class Mpris(GObject.Object):
    """
    :Constructors:

    ::

        Mpris(**properties)
        new() -> AstalMpris.Mpris

    Object AstalMprisMpris

    Signals from AstalMprisMpris:
      player-added (AstalMprisPlayer)
      player-closed (AstalMprisPlayer)

    Properties from AstalMprisMpris:
      players -> gpointer: players
        players

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        players: list[Player]
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: MprisPrivate = ...
    @staticmethod
    def get_default() -> Mpris: ...
    def get_players(self) -> list[Player]: ...
    @classmethod
    def new(cls) -> Mpris: ...
    

class MprisClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MprisClass()
    """
    parent_class: GObject.ObjectClass = ...

class MprisPrivate(GObject.GPointer): ...

class Player(GObject.Object):
    """
    :Constructors:

    ::

        Player(**properties)
        new(name:str) -> AstalMpris.Player

    Object AstalMprisPlayer

    Signals from AstalMprisPlayer:
      appeared ()
      closed ()

    Properties from AstalMprisPlayer:
      bus-name -> gchararray: bus-name
        bus-name
      available -> gboolean: available
        available
      can-quit -> gboolean: can-quit
        can-quit
      fullscreen -> gboolean: fullscreen
        fullscreen
      can-set-fullscreen -> gboolean: can-set-fullscreen
        can-set-fullscreen
      can-raise -> gboolean: can-raise
        can-raise
      identity -> gchararray: identity
        identity
      entry -> gchararray: entry
        entry
      supported-uri-schemes -> GStrv: supported-uri-schemes
        supported-uri-schemes
      supported-mime-types -> GStrv: supported-mime-types
        supported-mime-types
      loop-status -> AstalMprisLoop: loop-status
        loop-status
      rate -> gdouble: rate
        rate
      shuffle-status -> AstalMprisShuffle: shuffle-status
        shuffle-status
      volume -> gdouble: volume
        volume
      position -> gdouble: position
        position
      playback-status -> AstalMprisPlaybackStatus: playback-status
        playback-status
      minimum-rate -> gdouble: minimum-rate
        minimum-rate
      maximum-rate -> gdouble: maximum-rate
        maximum-rate
      can-go-next -> gboolean: can-go-next
        can-go-next
      can-go-previous -> gboolean: can-go-previous
        can-go-previous
      can-play -> gboolean: can-play
        can-play
      can-pause -> gboolean: can-pause
        can-pause
      can-seek -> gboolean: can-seek
        can-seek
      can-control -> gboolean: can-control
        can-control
      metadata -> GHashTable: metadata
        metadata
      trackid -> gchararray: trackid
        trackid
      length -> gdouble: length
        length
      art-url -> gchararray: art-url
        art-url
      album -> gchararray: album
        album
      album-artist -> gchararray: album-artist
        album-artist
      artist -> gchararray: artist
        artist
      lyrics -> gchararray: lyrics
        lyrics
      title -> gchararray: title
        title
      composer -> gchararray: composer
        composer
      comments -> gchararray: comments
        comments
      cover-art -> gchararray: cover-art
        cover-art

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        bus_name: str
        available: bool
        can_quit: bool
        fullscreen: bool
        can_set_fullscreen: bool
        can_raise: bool
        identity: str
        entry: str
        supported_uri_schemes: list[str]
        supported_mime_types: list[str]
        loop_status: Loop
        rate: float
        shuffle_status: Shuffle
        volume: float
        position: float
        playback_status: PlaybackStatus
        minimum_rate: float
        maximum_rate: float
        can_go_next: bool
        can_go_previous: bool
        can_play: bool
        can_pause: bool
        can_seek: bool
        can_control: bool
        metadata: dict[str, GLib.Variant]
        trackid: str
        length: float
        art_url: str
        album: str
        album_artist: str
        artist: str
        lyrics: str
        title: str
        composer: str
        comments: str
        cover_art: str
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: PlayerPrivate = ...
    def __init__(self, bus_name: str = ...,
                 available: bool = ...,
                 can_quit: bool = ...,
                 fullscreen: bool = ...,
                 can_set_fullscreen: bool = ...,
                 can_raise: bool = ...,
                 identity: str = ...,
                 entry: str = ...,
                 supported_uri_schemes: typing.Sequence[str] = ...,
                 supported_mime_types: typing.Sequence[str] = ...,
                 loop_status: Loop = ...,
                 rate: float = ...,
                 shuffle_status: Shuffle = ...,
                 volume: float = ...,
                 position: float = ...,
                 playback_status: PlaybackStatus = ...,
                 minimum_rate: float = ...,
                 maximum_rate: float = ...,
                 can_go_next: bool = ...,
                 can_go_previous: bool = ...,
                 can_play: bool = ...,
                 can_pause: bool = ...,
                 can_seek: bool = ...,
                 can_control: bool = ...,
                 metadata: dict[str, GLib.Variant] = ...,
                 trackid: str = ...,
                 length: float = ...,
                 art_url: str = ...,
                 album: str = ...,
                 album_artist: str = ...,
                 artist: str = ...,
                 lyrics: str = ...,
                 title: str = ...,
                 composer: str = ...,
                 comments: str = ...,
                 cover_art: str = ...) -> None: ...
    def get_album(self) -> str: ...
    def get_album_artist(self) -> str: ...
    def get_art_url(self) -> str: ...
    def get_artist(self) -> str: ...
    def get_available(self) -> bool: ...
    def get_bus_name(self) -> str: ...
    def get_can_control(self) -> bool: ...
    def get_can_go_next(self) -> bool: ...
    def get_can_go_previous(self) -> bool: ...
    def get_can_pause(self) -> bool: ...
    def get_can_play(self) -> bool: ...
    def get_can_quit(self) -> bool: ...
    def get_can_raise(self) -> bool: ...
    def get_can_seek(self) -> bool: ...
    def get_can_set_fullscreen(self) -> bool: ...
    def get_comments(self) -> str: ...
    def get_composer(self) -> str: ...
    def get_cover_art(self) -> str: ...
    def get_entry(self) -> str: ...
    def get_fullscreen(self) -> bool: ...
    def get_identity(self) -> str: ...
    def get_length(self) -> float: ...
    def get_loop_status(self) -> Loop: ...
    def get_lyrics(self) -> str: ...
    def get_maximum_rate(self) -> float: ...
    def get_meta(self, key: str) -> typing.Optional[GLib.Variant]: ...
    def get_metadata(self) -> dict[str, GLib.Variant]: ...
    def get_minimum_rate(self) -> float: ...
    def get_playback_status(self) -> PlaybackStatus: ...
    def get_position(self) -> float: ...
    def get_rate(self) -> float: ...
    def get_shuffle_status(self) -> Shuffle: ...
    def get_supported_mime_types(self) -> list[str]: ...
    def get_supported_uri_schemes(self) -> list[str]: ...
    def get_title(self) -> str: ...
    def get_trackid(self) -> str: ...
    def get_volume(self) -> float: ...
    def loop(self) -> None: ...
    @classmethod
    def new(cls, name: str) -> Player: ...
    def next(self) -> None: ...
    def open_uri(self, uri: str) -> None: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    def play_pause(self) -> None: ...
    def previous(self) -> None: ...
    def quit(self) -> None: ...
    def raise_(self) -> None: ...
    def set_loop_status(self, value: Loop) -> None: ...
    def set_position(self, value: float) -> None: ...
    def set_rate(self, value: float) -> None: ...
    def set_shuffle_status(self, value: Shuffle) -> None: ...
    def set_volume(self, value: float) -> None: ...
    def shuffle(self) -> None: ...
    def stop(self) -> None: ...
    def toggle_fullscreen(self) -> None: ...
    

class PlayerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PlayerClass()
    """
    parent_class: GObject.ObjectClass = ...
    appeared: typing.Callable[[Player], None] = ...
    closed: typing.Callable[[Player], None] = ...

class PlayerPrivate(GObject.GPointer): ...

class Loop(GObject.GEnum):
    NONE = 1
    PLAYLIST = 3
    TRACK = 2
    UNSUPPORTED = 0

class PlaybackStatus(GObject.GEnum):
    PAUSED = 1
    PLAYING = 0
    STOPPED = 2

class Shuffle(GObject.GEnum):
    OFF = 2
    ON = 1
    UNSUPPORTED = 0


