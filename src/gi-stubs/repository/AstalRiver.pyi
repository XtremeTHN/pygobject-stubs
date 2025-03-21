import typing

from gi.repository import GObject
from gi.repository import Gio
T = typing.TypeVar("T")

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 0
MINOR_VERSION: int = 1
VERSION: str = "0.1.0"
_lock = ... # FIXME Constant
_namespace: str = "AstalRiver"
_version: str = "0.1"

def get_default() -> typing.Optional[River]: ...

class Output(GObject.Object):
    """
    :Constructors:

    ::

        Output(**properties)

    Object AstalRiverOutput

    Signals from AstalRiverOutput:
      changed ()

    Properties from AstalRiverOutput:
      focused-tags -> guint: focused-tags
        currently focused tags
      occupied-tags -> guint: occupied-tags
        currently occupied tags
      urgent-tags -> guint: urgent-tags
        currently urgent tags
      layout-name -> gchararray: layout-name
        name of the current layout
      name -> gchararray: name
        name of the output
      focused-view -> gchararray: focused-view
        name of last focused view on this output
      id -> guint: id
        id of the output object

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        focused_tags: int
        focused_view: typing.Optional[str]
        id: int
        layout_name: typing.Optional[str]
        name: typing.Optional[str]
        occupied_tags: int
        urgent_tags: int
    props: Props = ...
    def __init__(self, focused_tags: int = ...) -> None: ...
    def get_focused_tags(self) -> int: ...
    def get_focused_view(self) -> typing.Optional[str]: ...
    def get_id(self) -> int: ...
    def get_layout_name(self) -> typing.Optional[str]: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_occupied_tags(self) -> int: ...
    def get_urgent_tags(self) -> int: ...
    def set_focused_tags(self, tags: int) -> None: ...
    

class OutputClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OutputClass()
    """
    parent_class: GObject.ObjectClass = ...

class River(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        River(**properties)
        new() -> AstalRiver.River or None

    Object AstalRiverRiver

    Signals from AstalRiverRiver:
      changed ()
      output-added (gchararray)
      output-removed (gchararray)

    Properties from AstalRiverRiver:
      focused-output -> gchararray: focused-output
        currently focused-output
      focused-view -> gchararray: focused-view
        currently focused view
      mode -> gchararray: mode
        currently active mode
      outputs -> gpointer: outputs
        a list of all outputs

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        focused_output: typing.Optional[str]
        focused_view: typing.Optional[str]
        mode: typing.Optional[str]
        outputs: list[Output]
    props: Props = ...
    @staticmethod
    def get_default() -> typing.Optional[River]: ...
    def get_focused_output(self) -> typing.Optional[str]: ...
    def get_focused_view(self) -> typing.Optional[str]: ...
    def get_mode(self) -> typing.Optional[str]: ...
    def get_output(self, name: str) -> typing.Optional[Output]: ...
    def get_outputs(self) -> list[Output]: ...
    @classmethod
    def new(cls) -> typing.Optional[River]: ...
    def run_command_async(self, cmd: typing.Sequence[str], callback: typing.Optional[typing.Callable[[bool, str], None]] = None) -> None: ...
    

class RiverClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RiverClass()
    """
    parent_class: GObject.ObjectClass = ...


