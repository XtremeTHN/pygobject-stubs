import typing

from gi.repository import AstalIO
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import Gtk
T = typing.TypeVar("T")

MAJOR_VERSION: int = 4
MICRO_VERSION: int = 0
MINOR_VERSION: int = 0
VERSION: str = "4.0.0"
_lock = ... # FIXME Constant
_namespace: str = "Astal"
_version: str = "4.0"

class Application(Gtk.Application, AstalIO.Application):
    """
    :Constructors:

    ::

        Application(**properties)
        new() -> Astal.Application

    Object AstalApplication

    Signals from AstalApplication:
      window-toggled (GtkWindow)

    Properties from AstalApplication:
      monitors -> gpointer: monitors
        monitors
      instance-name -> gchararray: instance-name
        instance-name
      windows -> gpointer: windows
        windows
      gtk-theme -> gchararray: gtk-theme
        gtk-theme
      icon-theme -> gchararray: icon-theme
        icon-theme
      cursor-theme -> gchararray: cursor-theme
        cursor-theme

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkApplication:
      window-added (GtkWindow)
      window-removed (GtkWindow)
      query-end ()

    Properties from GtkApplication:
      register-session -> gboolean: register-session
      screensaver-active -> gboolean: screensaver-active
      menubar -> GMenuModel: menubar
      active-window -> GtkWindow: active-window

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GApplication:
      startup ()
      shutdown ()
      activate ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean

    Properties from GApplication:
      application-id -> gchararray: application-id
      version -> gchararray: version
      flags -> GApplicationFlags: flags
      resource-base-path -> gchararray: resource-base-path
      is-registered -> gboolean: is-registered
      is-remote -> gboolean: is-remote
      inactivity-timeout -> guint: inactivity-timeout
      action-group -> GActionGroup: action-group
      is-busy -> gboolean: is-busy

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        monitors: list[Gdk.Monitor]
        windows: list[Gtk.Window]
        gtk_theme: str
        icon_theme: str
        cursor_theme: str
        active_window: typing.Optional[Gtk.Window]
        menubar: typing.Optional[Gio.MenuModel]
        register_session: bool
        screensaver_active: bool
        application_id: typing.Optional[str]
        flags: Gio.ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: typing.Optional[str]
        version: typing.Optional[str]
        instance_name: str
        action_group: typing.Optional[Gio.ActionGroup]
    props: Props = ...
    parent_instance: Gtk.Application = ...
    priv: ApplicationPrivate = ...
    def __init__(self, gtk_theme: str = ...,
                 icon_theme: str = ...,
                 cursor_theme: str = ...,
                 menubar: typing.Optional[Gio.MenuModel] = ...,
                 register_session: bool = ...,
                 action_group: typing.Optional[Gio.ActionGroup] = ...,
                 application_id: typing.Optional[str] = ...,
                 flags: Gio.ApplicationFlags = ...,
                 inactivity_timeout: int = ...,
                 resource_base_path: typing.Optional[str] = ...,
                 version: str = ...,
                 instance_name: str = ...) -> None: ...
    def add_icons(self, path: typing.Optional[str] = None) -> None: ...
    def apply_css(self, style: str, reset: bool) -> None: ...
    def do_request(self, msg: str, conn: Gio.SocketConnection) -> None: ...
    def get_cursor_theme(self) -> str: ...
    def get_gtk_theme(self) -> str: ...
    def get_icon_theme(self) -> str: ...
    def get_monitors(self) -> list[Gdk.Monitor]: ...
    def get_window(self, name: str) -> typing.Optional[Gtk.Window]: ...
    def get_windows(self) -> list[Gtk.Window]: ...
    @classmethod
    def new(cls) -> Application: ...
    def request(self, msg: str, conn: Gio.SocketConnection) -> None: ...
    def reset_css(self) -> None: ...
    def set_cursor_theme(self, value: str) -> None: ...
    def set_gtk_theme(self, value: str) -> None: ...
    def set_icon_theme(self, value: str) -> None: ...
    

class ApplicationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationClass()
    """
    parent_class: Gtk.ApplicationClass = ...
    request: typing.Callable[[Application, str, Gio.SocketConnection], None] = ...

class ApplicationPrivate(GObject.GPointer): ...

class Box(Gtk.Box):
    """
    :Constructors:

    ::

        Box(**properties)
        new() -> Astal.Box

    Object AstalBox

    Properties from AstalBox:
      vertical -> gboolean: vertical
        vertical
      children -> gpointer: children
        children
      child -> GtkWidget: child
        child

    Properties from GtkBox:
      spacing -> gint: spacing
      homogeneous -> gboolean: homogeneous
      baseline-child -> gint: baseline-child
      baseline-position -> GtkBaselinePosition: baseline-position

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        vertical: bool
        children: list[Gtk.Widget]
        child: Gtk.Widget
        baseline_child: int
        baseline_position: Gtk.BaselinePosition
        homogeneous: bool
        spacing: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
    props: Props = ...
    parent_instance: Gtk.Box = ...
    priv: BoxPrivate = ...
    def __init__(self, vertical: bool = ...,
                 children: list[Gtk.Widget] = ...,
                 child: Gtk.Widget = ...,
                 baseline_child: int = ...,
                 baseline_position: Gtk.BaselinePosition = ...,
                 homogeneous: bool = ...,
                 spacing: int = ...,
                 can_focus: bool = ...,
                 can_target: bool = ...,
                 css_classes: typing.Sequence[str] = ...,
                 css_name: str = ...,
                 cursor: typing.Optional[Gdk.Cursor] = ...,
                 focus_on_click: bool = ...,
                 focusable: bool = ...,
                 halign: Gtk.Align = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 opacity: float = ...,
                 overflow: Gtk.Overflow = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_children(self) -> list[Gtk.Widget]: ...
    def get_vertical(self) -> bool: ...
    @classmethod
    def new(cls) -> Box: ...
    def set_child(self, value: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_children(self, value: list[Gtk.Widget]) -> None: ...
    def set_vertical(self, value: bool) -> None: ...
    

class BoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BoxClass()
    """
    parent_class: Gtk.BoxClass = ...

class BoxPrivate(GObject.GPointer): ...

class Slider(Gtk.Scale):
    """
    :Constructors:

    ::

        Slider(**properties)
        new() -> Astal.Slider

    Object AstalSlider

    Properties from AstalSlider:
      value -> gdouble: value
        value
      min -> gdouble: min
        min
      max -> gdouble: max
        max
      step -> gdouble: step
        step
      page -> gdouble: page
        page

    Properties from GtkScale:
      digits -> gint: digits
      draw-value -> gboolean: draw-value
      has-origin -> gboolean: has-origin
      value-pos -> GtkPositionType: value-pos

    Signals from GtkRange:
      value-changed ()
      adjust-bounds (gdouble)
      move-slider (GtkScrollType)
      change-value (GtkScrollType, gdouble) -> gboolean

    Properties from GtkRange:
      adjustment -> GtkAdjustment: adjustment
      inverted -> gboolean: inverted
      show-fill-level -> gboolean: show-fill-level
      restrict-to-fill-level -> gboolean: restrict-to-fill-level
      fill-level -> gdouble: fill-level
      round-digits -> gint: round-digits

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        value: float
        min: float
        max: float
        step: float
        page: float
        digits: int
        draw_value: bool
        has_origin: bool
        value_pos: Gtk.PositionType
        adjustment: Gtk.Adjustment
        fill_level: float
        inverted: bool
        restrict_to_fill_level: bool
        round_digits: int
        show_fill_level: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
    props: Props = ...
    parent_instance: Gtk.Scale = ...
    priv: SliderPrivate = ...
    def __init__(self, value: float = ...,
                 min: float = ...,
                 max: float = ...,
                 step: float = ...,
                 page: float = ...,
                 digits: int = ...,
                 draw_value: bool = ...,
                 has_origin: bool = ...,
                 value_pos: Gtk.PositionType = ...,
                 adjustment: Gtk.Adjustment = ...,
                 fill_level: float = ...,
                 inverted: bool = ...,
                 restrict_to_fill_level: bool = ...,
                 round_digits: int = ...,
                 show_fill_level: bool = ...,
                 can_focus: bool = ...,
                 can_target: bool = ...,
                 css_classes: typing.Sequence[str] = ...,
                 css_name: str = ...,
                 cursor: typing.Optional[Gdk.Cursor] = ...,
                 focus_on_click: bool = ...,
                 focusable: bool = ...,
                 halign: Gtk.Align = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
                 margin_bottom: int = ...,
                 margin_end: int = ...,
                 margin_start: int = ...,
                 margin_top: int = ...,
                 name: str = ...,
                 opacity: float = ...,
                 overflow: Gtk.Overflow = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def get_max(self) -> float: ...
    def get_min(self) -> float: ...
    def get_page(self) -> float: ...
    def get_step(self) -> float: ...
    def get_value(self) -> float: ...
    @classmethod
    def new(cls) -> Slider: ...
    def set_max(self, value: float) -> None: ...
    def set_min(self, value: float) -> None: ...
    def set_page(self, value: float) -> None: ...
    def set_step(self, value: float) -> None: ...
    def set_value(self, value: float) -> None: ...
    

class SliderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SliderClass()
    """
    parent_class: Gtk.ScaleClass = ...

class SliderPrivate(GObject.GPointer): ...

class Window(Gtk.Window):
    """
    :Constructors:

    ::

        Window(**properties)
        new() -> Astal.Window

    Object AstalWindow

    Properties from AstalWindow:
      namespace -> gchararray: namespace
        namespace
      anchor -> AstalWindowAnchor: anchor
        anchor
      exclusivity -> AstalExclusivity: exclusivity
        exclusivity
      layer -> AstalLayer: layer
        layer
      keymode -> AstalKeymode: keymode
        keymode
      gdkmonitor -> GdkMonitor: gdkmonitor
        gdkmonitor
      margin-top -> gint: margin-top
        margin-top
      margin-bottom -> gint: margin-bottom
        margin-bottom
      margin-left -> gint: margin-left
        margin-left
      margin-right -> gint: margin-right
        margin-right
      margin -> gint: margin
        margin
      monitor -> gint: monitor
        monitor

    Signals from GtkWindow:
      keys-changed ()
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

    Signals from GtkWidget:
      direction-changed (GtkTextDirection)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        namespace: str
        anchor: WindowAnchor
        exclusivity: Exclusivity
        layer: Layer
        keymode: Keymode
        gdkmonitor: Gdk.Monitor
        margin_top: int
        margin_bottom: int
        margin_left: int
        margin_right: int
        monitor: int
        application: typing.Optional[Gtk.Application]
        child: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: typing.Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: typing.Optional[Gtk.Widget]
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: typing.Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: typing.Optional[str]
        titlebar: typing.Optional[Gtk.Widget]
        transient_for: typing.Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        margin_end: int
        margin_start: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        margin: int
        startup_id: str
    props: Props = ...
    parent_instance: Gtk.Window = ...
    priv: WindowPrivate = ...
    def __init__(self, namespace: str = ...,
                 anchor: WindowAnchor = ...,
                 exclusivity: Exclusivity = ...,
                 layer: Layer = ...,
                 keymode: Keymode = ...,
                 gdkmonitor: Gdk.Monitor = ...,
                 margin_top: int = ...,
                 margin_bottom: int = ...,
                 margin_left: int = ...,
                 margin_right: int = ...,
                 margin: int = ...,
                 monitor: int = ...,
                 application: typing.Optional[Gtk.Application] = ...,
                 child: typing.Optional[Gtk.Widget] = ...,
                 decorated: bool = ...,
                 default_height: int = ...,
                 default_widget: typing.Optional[Gtk.Widget] = ...,
                 default_width: int = ...,
                 deletable: bool = ...,
                 destroy_with_parent: bool = ...,
                 display: Gdk.Display = ...,
                 focus_visible: bool = ...,
                 focus_widget: typing.Optional[Gtk.Widget] = ...,
                 fullscreened: bool = ...,
                 handle_menubar_accel: bool = ...,
                 hide_on_close: bool = ...,
                 icon_name: typing.Optional[str] = ...,
                 maximized: bool = ...,
                 mnemonics_visible: bool = ...,
                 modal: bool = ...,
                 resizable: bool = ...,
                 startup_id: str = ...,
                 title: typing.Optional[str] = ...,
                 titlebar: typing.Optional[Gtk.Widget] = ...,
                 transient_for: typing.Optional[Gtk.Window] = ...,
                 can_focus: bool = ...,
                 can_target: bool = ...,
                 css_classes: typing.Sequence[str] = ...,
                 css_name: str = ...,
                 cursor: typing.Optional[Gdk.Cursor] = ...,
                 focus_on_click: bool = ...,
                 focusable: bool = ...,
                 halign: Gtk.Align = ...,
                 has_tooltip: bool = ...,
                 height_request: int = ...,
                 hexpand: bool = ...,
                 hexpand_set: bool = ...,
                 layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
                 margin_end: int = ...,
                 margin_start: int = ...,
                 name: str = ...,
                 opacity: float = ...,
                 overflow: Gtk.Overflow = ...,
                 receives_default: bool = ...,
                 sensitive: bool = ...,
                 tooltip_markup: typing.Optional[str] = ...,
                 tooltip_text: typing.Optional[str] = ...,
                 valign: Gtk.Align = ...,
                 vexpand: bool = ...,
                 vexpand_set: bool = ...,
                 visible: bool = ...,
                 width_request: int = ...) -> None: ...
    def get_anchor(self) -> WindowAnchor: ...
    def get_current_monitor(self) -> Gdk.Monitor: ...
    def get_exclusivity(self) -> Exclusivity: ...
    def get_gdkmonitor(self) -> Gdk.Monitor: ...
    def get_keymode(self) -> Keymode: ...
    def get_layer(self) -> Layer: ...
    def get_margin_bottom(self) -> int: ...
    def get_margin_left(self) -> int: ...
    def get_margin_right(self) -> int: ...
    def get_margin_top(self) -> int: ...
    def get_monitor(self) -> int: ...
    def get_namespace(self) -> str: ...
    @classmethod
    def new(cls) -> Window: ...
    def set_anchor(self, value: WindowAnchor) -> None: ...
    def set_exclusivity(self, value: Exclusivity) -> None: ...
    def set_gdkmonitor(self, value: Gdk.Monitor) -> None: ...
    def set_keymode(self, value: Keymode) -> None: ...
    def set_layer(self, value: Layer) -> None: ...
    def set_margin(self, value: int) -> None: ...
    def set_margin_bottom(self, value: int) -> None: ...
    def set_margin_left(self, value: int) -> None: ...
    def set_margin_right(self, value: int) -> None: ...
    def set_margin_top(self, value: int) -> None: ...
    def set_monitor(self, value: int) -> None: ...
    def set_namespace(self, value: str) -> None: ...
    

class WindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowClass()
    """
    parent_class: Gtk.WindowClass = ...

class WindowPrivate(GObject.GPointer): ...

class WindowAnchor(GObject.GFlags):
    BOTTOM = 16
    LEFT = 8
    NONE = 1
    RIGHT = 4
    TOP = 2

class Exclusivity(GObject.GEnum):
    EXCLUSIVE = 1
    IGNORE = 2
    NORMAL = 0

class Keymode(GObject.GEnum):
    EXCLUSIVE = 1
    NONE = 0
    ON_DEMAND = 2

class Layer(GObject.GEnum):
    BACKGROUND = 0
    BOTTOM = 1
    OVERLAY = 3
    TOP = 2


