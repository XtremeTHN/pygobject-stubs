import typing

from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import NM
T = typing.TypeVar("T")

BAR_CODE_SIZE: str = "size"
BAR_CODE_TEXT: str = "text"
BAR_CODE_WIDGET_CONNECTION: str = "connection"
MAJOR_VERSION: int = 1
MICRO_VERSION: int = 6
MINOR_VERSION: int = 10
_lock = ... # FIXME Constant
_namespace: str = "NMA4"
_version: str = "1.0"

def mobile_providers_split_3gpp_mcc_mnc(mccmnc: str) -> typing.Tuple[bool, str, str]: ...
def utils_menu_to_secret_flags(passwd_entry: Gtk.Widget) -> NM.SettingSecretFlags: ...
def utils_setup_password_storage(passwd_entry: Gtk.Widget, initial_flags: NM.SettingSecretFlags, setting: NM.Setting, password_flags_name: str, with_not_required: bool, ask_mode: bool) -> None: ...
def utils_update_password_storage(passwd_entry: Gtk.Widget, secret_flags: NM.SettingSecretFlags, setting: NM.Setting, password_flags_name: str) -> None: ...

class BarCode(GObject.Object):
    """
    :Constructors:

    ::

        BarCode(**properties)
        new(text:str) -> NMA4.BarCode

    Object NMABarCode

    Properties from NMABarCode:
      text -> gchararray: 
    
      size -> gint: 
    

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        size: int
        text: str
    props: Props = ...
    def __init__(self, text: str = ...) -> None: ...
    def draw(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def get_size(self) -> int: ...
    @classmethod
    def new(cls, text: str) -> BarCode: ...
    def set_text(self, text: str) -> None: ...
    

class BarCodeClass(GObject.GPointer): ...

class BarCodeWidget(Gtk.Box, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable):
    """
    :Constructors:

    ::

        BarCodeWidget(**properties)

    Object NMABarCodeWidget

    Properties from NMABarCodeWidget:
      connection -> NMConnection: 
    

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
        connection: NM.Connection
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
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(self, connection: NM.Connection = ...,
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
                 width_request: int = ...,
                 accessible_role: Gtk.AccessibleRole = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...

class BarCodeWidgetClass(GObject.GPointer): ...

class CertChooser(Gtk.Grid, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable):
    """
    :Constructors:

    ::

        CertChooser(**properties)
        new(title:str, flags:NMA4.CertChooserFlags) -> Gtk.Widget

    Object NMACertChooser

    Signals from NMACertChooser:
      changed ()
      cert-validate () -> GError
      cert-password-validate () -> GError
      key-validate () -> GError
      key-password-validate () -> GError

    Properties from NMACertChooser:
      title -> gchararray: Title
        Certificate Chooser Title
      flags -> guint: Flags
        Certificate Chooser Flags

    Properties from GtkGrid:
      row-spacing -> gint: row-spacing
      column-spacing -> gint: column-spacing
      row-homogeneous -> gboolean: row-homogeneous
      column-homogeneous -> gboolean: column-homogeneous
      baseline-row -> gint: baseline-row

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
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
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
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
        flags: int
        title: str
    props: Props = ...
    def __init__(self, flags: int = ...,
                 title: str = ...,
                 baseline_row: int = ...,
                 column_homogeneous: bool = ...,
                 column_spacing: int = ...,
                 row_homogeneous: bool = ...,
                 row_spacing: int = ...,
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
                 width_request: int = ...,
                 accessible_role: Gtk.AccessibleRole = ...,
                 orientation: Gtk.Orientation = ...) -> None: ...
    def add_to_size_group(self, group: Gtk.SizeGroup) -> None: ...
    def get_cert(self) -> typing.Tuple[typing.Optional[str], NM.Setting8021xCKScheme]: ...
    def get_cert_password(self) -> str: ...
    def get_cert_password_flags(self) -> NM.SettingSecretFlags: ...
    def get_cert_uri(self) -> typing.Optional[str]: ...
    def get_key(self) -> typing.Tuple[typing.Optional[str], NM.Setting8021xCKScheme]: ...
    def get_key_password(self) -> str: ...
    def get_key_password_flags(self) -> NM.SettingSecretFlags: ...
    def get_key_uri(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls, title: str, flags: CertChooserFlags) -> CertChooser: ...
    def set_cert(self, value: str, scheme: NM.Setting8021xCKScheme) -> None: ...
    def set_cert_password(self, password: str) -> None: ...
    def set_cert_uri(self, uri: str) -> None: ...
    def set_key(self, value: str, scheme: NM.Setting8021xCKScheme) -> None: ...
    def set_key_password(self, password: str) -> None: ...
    def set_key_uri(self, uri: str) -> None: ...
    def setup_cert_password_storage(self, initial_flags: NM.SettingSecretFlags, setting: NM.Setting, password_flags_name: str, with_not_required: bool, ask_mode: bool) -> None: ...
    def setup_key_password_storage(self, initial_flags: NM.SettingSecretFlags, setting: NM.Setting, password_flags_name: str, with_not_required: bool, ask_mode: bool) -> None: ...
    def update_cert_password_storage(self, secret_flags: NM.SettingSecretFlags, setting: NM.Setting, password_flags_name: str) -> None: ...
    def update_key_password_storage(self, secret_flags: NM.SettingSecretFlags, setting: NM.Setting, password_flags_name: str) -> None: ...
    def validate(self) -> bool: ...
    

class CertChooserClass(GObject.GPointer): ...

class CountryInfo(GObject.GBoxed):
    def get_country_code(self) -> str: ...
    def get_country_name(self) -> str: ...
    def get_providers(self) -> list[MobileProvider]: ...
    def ref(self) -> CountryInfo: ...
    def unref(self) -> None: ...
    

class MobileAccessMethod(GObject.GBoxed):
    def get_3gpp_apn(self) -> str: ...
    def get_dns(self) -> list[str]: ...
    def get_family(self) -> MobileFamily: ...
    def get_gateway(self) -> str: ...
    def get_name(self) -> str: ...
    def get_password(self) -> str: ...
    def get_username(self) -> str: ...
    def ref(self) -> MobileAccessMethod: ...
    def unref(self) -> None: ...
    

class MobileProvider(GObject.GBoxed):
    def get_3gpp_mcc_mnc(self) -> list[str]: ...
    def get_cdma_sid(self) -> list[int]: ...
    def get_methods(self) -> list[MobileAccessMethod]: ...
    def get_name(self) -> str: ...
    def ref(self) -> MobileProvider: ...
    def unref(self) -> None: ...
    

class MobileProvidersDatabase(GObject.Object, Gio.AsyncInitable, Gio.Initable):
    """
    :Constructors:

    ::

        MobileProvidersDatabase(**properties)
        new_finish(res:Gio.AsyncResult) -> NMA4.MobileProvidersDatabase
        new_sync(country_codes:str=None, service_providers:str=None, cancellable:Gio.Cancellable=None) -> NMA4.MobileProvidersDatabase

    Object NMAMobileProvidersDatabase

    Properties from NMAMobileProvidersDatabase:
      country-codes -> gchararray: Country Codes
        Path to the country codes file
      service-providers -> gchararray: Service Providers
        Path to the service providers file

    Signals from GObject:
      notify (GParam)
    """
    class Props:
        country_codes: str
        service_providers: str
    props: Props = ...
    parent: GObject.Object = ...
    priv: MobileProvidersDatabasePrivate = ...
    def __init__(self, country_codes: str = ...,
                 service_providers: str = ...) -> None: ...
    def dump(self) -> None: ...
    def get_countries(self) -> dict[str, CountryInfo]: ...
    def lookup_3gpp_mcc_mnc(self, mccmnc: str) -> MobileProvider: ...
    def lookup_cdma_sid(self, sid: int) -> MobileProvider: ...
    def lookup_country(self, country_code: str) -> CountryInfo: ...
    @staticmethod
    def new(country_codes: typing.Optional[str] = None, service_providers: typing.Optional[str] = None, cancellable: typing.Optional[Gio.Cancellable] = None, callback: typing.Optional[typing.Callable[..., None]] = None, *user_data: typing.Any) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> MobileProvidersDatabase: ...
    @classmethod
    def new_sync(cls, country_codes: typing.Optional[str] = None, service_providers: typing.Optional[str] = None, cancellable: typing.Optional[Gio.Cancellable] = None) -> MobileProvidersDatabase: ...
    

class MobileProvidersDatabaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MobileProvidersDatabaseClass()
    """
    parent: GObject.ObjectClass = ...

class MobileProvidersDatabasePrivate(GObject.GPointer): ...

class MobileWizard(GObject.Object):
    """
    :Constructors:

    ::

        MobileWizard(**properties)

    Object NMAMobileWizard

    Signals from GObject:
      notify (GParam)
    """
    def destroy(self) -> None: ...
    def present(self) -> None: ...
    

class MobileWizardAccessMethod(GObject.GPointer):
    """
    :Constructors:

    ::

        MobileWizardAccessMethod()
    """
    provider_name: str = ...
    plan_name: str = ...
    devtype: NM.DeviceModemCapabilities = ...
    username: str = ...
    password: str = ...
    gsm_apn: str = ...

class MobileWizardClass(GObject.GPointer): ...

class VpnPasswordDialog(Gtk.Dialog, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Native, Gtk.Root, Gtk.ShortcutManager):
    """
    :Constructors:

    ::

        VpnPasswordDialog(**properties)
        new(title:str, message:str, password:str) -> Gtk.Widget

    Object NMAVpnPasswordDialog

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar

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
        use_header_bar: int
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
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    parent: Gtk.Dialog = ...
    def __init__(self, use_header_bar: int = ...,
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
                 width_request: int = ...,
                 accessible_role: Gtk.AccessibleRole = ...) -> None: ...
    def focus_password(self) -> None: ...
    def focus_password_secondary(self) -> None: ...
    def focus_password_ternary(self) -> None: ...
    def get_password(self) -> str: ...
    def get_password_secondary(self) -> str: ...
    def get_password_ternary(self) -> str: ...
    @classmethod
    def new(cls, title: str, message: str, password: str) -> VpnPasswordDialog: ...
    def run_and_block(self) -> bool: ...
    def set_password(self, password: str) -> None: ...
    def set_password_label(self, label: str) -> None: ...
    def set_password_secondary(self, password_secondary: str) -> None: ...
    def set_password_secondary_label(self, label: str) -> None: ...
    def set_password_ternary(self, password_ternary: str) -> None: ...
    def set_password_ternary_label(self, label: str) -> None: ...
    def set_show_password(self, show: bool) -> None: ...
    def set_show_password_secondary(self, show: bool) -> None: ...
    def set_show_password_ternary(self, show: bool) -> None: ...
    

class VpnPasswordDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        VpnPasswordDialogClass()
    """
    parent_class: Gtk.DialogClass = ...

class WifiDialog(Gtk.Dialog, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Native, Gtk.Root, Gtk.ShortcutManager):
    """
    :Constructors:

    ::

        WifiDialog(**properties)
        new(client:NM.Client, connection:NM.Connection, device:NM.Device, ap:NM.AccessPoint, secrets_only:bool) -> Gtk.Widget
        new_for_create(client:NM.Client) -> Gtk.Widget
        new_for_hidden(client:NM.Client) -> Gtk.Widget
        new_for_other(client:NM.Client) -> Gtk.Widget
        new_for_secrets(client:NM.Client, connection:NM.Connection, secrets_setting_name:str, secrets_hints:str) -> Gtk.Widget

    Object NMAWifiDialog

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar

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
        use_header_bar: int
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
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    parent: Gtk.Dialog = ...
    def __init__(self, use_header_bar: int = ...,
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
                 width_request: int = ...,
                 accessible_role: Gtk.AccessibleRole = ...) -> None: ...
    def get_connection(self) -> typing.Tuple[NM.Connection, NM.Device, NM.AccessPoint]: ...
    def get_nag_ignored(self) -> bool: ...
    def nag_user(self) -> Gtk.Widget: ...
    @classmethod
    def new(cls, client: NM.Client, connection: NM.Connection, device: NM.Device, ap: NM.AccessPoint, secrets_only: bool) -> WifiDialog: ...
    @classmethod
    def new_for_create(cls, client: NM.Client) -> WifiDialog: ...
    @classmethod
    def new_for_hidden(cls, client: NM.Client) -> WifiDialog: ...
    @classmethod
    def new_for_other(cls, client: NM.Client) -> WifiDialog: ...
    @classmethod
    def new_for_secrets(cls, client: NM.Client, connection: NM.Connection, secrets_setting_name: str, secrets_hints: str) -> WifiDialog: ...
    def set_nag_ignored(self, ignored: bool) -> None: ...
    

class WifiDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WifiDialogClass()
    """
    parent: Gtk.DialogClass = ...

class Ws(GObject.GPointer):
    def adhoc_compatible(self) -> bool: ...
    def hotspot_compatible(self) -> bool: ...
    def validate(self) -> bool: ...
    

class Ws8021x(GObject.GPointer): ...

class Ws8021xClass(GObject.GPointer): ...

class WsDynamicWep(GObject.GPointer): ...

class WsDynamicWepClass(GObject.GPointer): ...

class WsInterface(GObject.GPointer): ...

class WsLeap(GObject.GPointer): ...

class WsLeapClass(GObject.GPointer): ...

class WsOwe(GObject.GPointer): ...

class WsOweClass(GObject.GPointer): ...

class WsSae(GObject.GPointer): ...

class WsSaeClass(GObject.GPointer): ...

class WsWepKey(GObject.GPointer): ...

class WsWepKeyClass(GObject.GPointer): ...

class WsWpaEap(GObject.GPointer): ...

class WsWpaEapClass(GObject.GPointer): ...

class WsWpaPsk(GObject.GPointer): ...

class WsWpaPskClass(GObject.GPointer): ...

class CertChooserFlags(GObject.GEnum):
    CERT = 1
    NONE = 0
    NO_PASSWORDS = 8
    PASSWORDS = 2
    PEM = 4

class MobileFamily(GObject.GEnum):
    CDMA = 2
    UNKNOWN = 0


