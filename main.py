#kivy関連import
from kivy.app import App            
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '960')

import japanize_kivy
from os.path import dirname, join

from Page1 import ImageWidget
from Page2 import CameraClick
from Page3 import CameraPreview, ImageButton


# カメラへのアクセス許可を要求する
try:
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.CAMERA,
        Permission.WRITE_EXTERNAL_STORAGE
        ])
except:
    pass


class AppFrame(BoxLayout):
    screen_manager = ObjectProperty(None)
    
    def switch2page(self, page_name):
        sm = self.screen_manager
        curdir = dirname(__file__)
        # print(join(curdir, f'{page_name}.kv'))
        screen = Builder.load_file(join(curdir, f'{page_name}.kv'))
        # print(type(screen))
        sm.switch_to(screen, direction='left')


class YakinikuApp(App):
    # def __init__(self, **kwargs):
    #     super(YakinikuApp, self).__init__(**kwargs)
    #     self.title = 'シマウマ画像表示'
        
    def build(self, **kwargs):
        pass


if __name__ == '__main__':                      #main.pyが直接実行されたら、、、という意味らしい
    YakinikuApp().run()                         #