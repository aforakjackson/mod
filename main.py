import kivy
kivy.require('2.1.0')  # Versión mínima de Kivy

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import BooleanProperty

# Ajustar el tamaño de la ventana (en PC se verá de un tamaño fijo;
# en Android, se adaptará a la pantalla)
Window.size = (400, 300)

class MenuOverlay(FloatLayout):
    """
    Layout principal que contendrá:
      - BoxLayout con los botones
      - Un botón extra para "Minimizar"
    """

    # Controla si el menú está "mostrado" (True) o "minimizado" (False)
    is_menu_visible = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(MenuOverlay, self).__init__(**kwargs)

        # Layout vertical para el menú
        self.menu_box = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            spacing=10,
            padding=10
        )

        # Botones del menú
        self.btn_bot_pesca = Button(
            text='Bot de Pesca',
            size_hint=(1, None),
            height=40
        )
        self.btn_overlay = Button(
            text='Overlay',
            size_hint=(1, None),
            height=40
        )
        self.btn_bot_amuleto = Button(
            text='Bot Mon. Amuleto',
            size_hint=(1, None),
            height=40
        )
        self.btn_info = Button(
            text='Info',
            size_hint=(1, None),
            height=40
        )

        # Agrega los 4 botones al BoxLayout
        self.menu_box.add_widget(self.btn_bot_pesca)
        self.menu_box.add_widget(self.btn_overlay)
        self.menu_box.add_widget(self.btn_bot_amuleto)
        self.menu_box.add_widget(self.btn_info)

        # Botón para minimizar
        self.btn_minimize = Button(
            text='Minimizar',
            size_hint=(1, None),
            height=40
        )
        self.btn_minimize.bind(on_release=self.minimize_menu)
        self.menu_box.add_widget(self.btn_minimize)

        # Agregamos el BoxLayout al Layout principal
        self.add_widget(self.menu_box)

        # Creamos un botón flotante que solo se mostrará cuando el menú esté minimizado
        self.restore_button = Button(
            text='↑',
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, 10)  # Ajusta posición a tu preferencia
        )
        self.restore_button.bind(on_release=self.restore_menu)
        # Por defecto, este botón NO se muestra (hasta que se minimice el menú)
        self.restore_button.opacity = 0
        self.restore_button.disabled = True

        self.add_widget(self.restore_button)

    def minimize_menu(self, *args):
        # Ocultar menú
        self.menu_box.opacity = 0
        self.menu_box.disabled = True

        # Mostrar botón flotante
        self.restore_button.opacity = 1
        self.restore_button.disabled = False

        self.is_menu_visible = False

    def restore_menu(self, *args):
        # Restaurar menú
        self.menu_box.opacity = 1
        self.menu_box.disabled = False

        # Ocultar botón flotante
        self.restore_button.opacity = 0
        self.restore_button.disabled = True

        self.is_menu_visible = True


class OverlayApp(App):
    def build(self):
        return MenuOverlay()

if __name__ == '__main__':
    OverlayApp().run()
