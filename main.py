#kivy関連import
from kivy.app import App            
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from kivy.config import Config
# Config.set('graphics', 'width', '480')
# Config.set('graphics', 'height', '960')
Config.set('kivy', 'log_level', 'debug')

from kivy.utils import platform
import japanize_kivy
from os.path import dirname, join
import os
from plyer import notification

import json
try: from jnius import autoclass
except:pass




def show_toast(message):
    """show_toastは、受け取った文字列messageをtoast表示します。"""
    notification.notify(
        message=message,
        timeout=1,
        toast=True
    )  

   
def load_setting():
    if platform == 'android':
        setting_dict = get_settings_dict_android()
        show_toast(setting_dict['btn0']['name'])
    elif platform == 'win': 
        setting_dict = get_settings_dict_win()
        show_toast(setting_dict['btn0']['name'])

def get_settings_dict_win():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'.\assets\cambuttons.json')
    with open(path, 'r', encoding='utf-8') as f:
        settings_dict = json.load(f)
    return settings_dict

def get_settings_dict_android():
    AssetManager = autoclass('android.content.res.AssetManager')
    Context = autoclass('android.content.Context')
    # BufferedReader = autoclass('java.io.BufferedReader')
    # InputStream = autoclass('java.io.InputStream')
    # InputStreamReader = autoclass('java.io.InputStreamReader')

    am = AssetManager().getAssets()
    input_stream = am.open('cambuttons.json')
    show_toast()
    return


class AppFrame(BoxLayout): 

    def call_func(self):
        show_toast('テスト')
        load_setting()



class CodetestApp(App):
    def __init__(self, **kwargs):
        super(CodetestApp, self).__init__(**kwargs)
        self.title = 'Kivyコードテストアプリ'

    def build(self):
        return AppFrame()


if __name__ == '__main__':                      #main.pyが直接実行されたら、、、という意味らしい
    CodetestApp().run()                         #