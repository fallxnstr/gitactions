import os
import subprocess
import winreg

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
Config.write()


class WidgetEx(GridLayout):
    def on_button_click(self):
        os.chdir("C:\Python\Tweaking App")
        os.startfile("NSudoLG.exe")

    def on_powerplanbutton_click(self):
        subprocess.call(
                        [
                                "powercfg",
                                "-import",
                                "C:\Python\Tweaking App/Powerplan.pow",
                                "11111111-1111-1111-1111-111111111111",
                ]
            )

        subprocess.call(
                    [
                               "powercfg",
                               "-changename",
                               "11111111-1111-1111-1111-111111111111",
                               "Powerplan",
                               "Optimized for the best performance",
            ]
        )


class TweakingApp(App):
    pass


TweakingApp().run()
