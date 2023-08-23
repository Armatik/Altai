import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class AltaiMainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Алтай ')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_child(child=vbox)

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        # Кнопка для открытия и закрытия боковой панели
        flap_Toggle_button = Gtk.ToggleButton.new()
        flap_Toggle_button.set_icon_name(icon_name="open-menu-symbolic")
        flap_Toggle_button.connect('clicked', self.on_flap_button_toggled)
        headerbar.pack_start(child=flap_Toggle_button)

        # Кнопка для закрытия приложения
        self.adw_flap = Adw.Flap.new()
        self.adw_flap.set_reveal_flap(reveal_flap=False)
        self.adw_flap.set_locked(locked=True)

        # Добавляем боковую панель в окно
        vbox.append(child=self.adw_flap)

        # Создаем стек для боковой панели
        stack = Gtk.Stack.new()
        self.adw_flap.set_content(content=stack)

        # Вкладка 1
        box_page_1 = self.page_minimal()
        stack.add_titled(child=box_page_1, name="Минимайльный", title="Минимальный") # Добавляем вкладку в стек


        # Вкладка 2
        box_page_2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=box_page_2, name="Авторйский", title="Авторский")

        label_page_2 = Gtk.Label.new(str='Алтай - Авторский пакет настройки системы')
        label_page_2.set_halign(align=Gtk.Align.CENTER)
        label_page_2.set_valign(align=Gtk.Align.CENTER)
        label_page_2.set_hexpand(expand=True)
        label_page_2.set_vexpand(expand=True)
        box_page_2.append(child=label_page_2)

        # StackSidebar управляет переключением между стеками.
        stack_sidebar = Gtk.StackSidebar.new()
        stack_sidebar.set_stack(stack=stack)
        self.adw_flap.set_flap(flap=stack_sidebar)

    def on_flap_button_toggled(self, widget):
        self.adw_flap.set_reveal_flap(not self.adw_flap.get_reveal_flap())


    def page_minimal(self):
        # При нажатии на кнопку "Минимальный" открывается вкладка "Минимальный"
        # Вкладка "Минимальный" содержит:
        # 1. Кнопку "Установить минимальный пакет"
        # 2. Блок с текстом где приведены основные изменения
        # 3. Возможнность раскрыть меню с более точечным выбором изменений

        # Создаем контейнер для вкладки
        box_page_minimal = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Создаем кнопку "Установить минимальный пакет"
        button_install_minimal = Gtk.Button.new_with_label(label="Установить минимальный пакет")
        button_install_minimal.connect('clicked', self.on_button_install_minimal_clicked)
        box_page_minimal.append(child=button_install_minimal)

        # Создаем блок с текстом где приведены основные изменения
        label_page_minimal = Gtk.Label.new(str='Алтай - Минимальный пакет настройки системы')
        label_page_minimal.set_halign(align=Gtk.Align.CENTER)
        label_page_minimal.set_valign(align=Gtk.Align.CENTER)
        label_page_minimal.set_hexpand(expand=True)
        label_page_minimal.set_vexpand(expand=True)
        box_page_minimal.append(child=label_page_minimal)

        # Создаем кнопку "Раскрыть меню"
        button_expand_menu = Gtk.Button.new_with_label(label="Раскрыть меню")
        button_expand_menu.connect('clicked', self.on_button_expand_menu_clicked)
        box_page_minimal.append(child=button_expand_menu)

        return box_page_minimal

    def on_button_install_minimal_clicked(self, widget):
        pass

    def on_button_expand_menu_clicked(self, widget):
        pass





class AltaiApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='ru.armatik.altai',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = AltaiMainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)