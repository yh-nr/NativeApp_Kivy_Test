#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '960')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
# from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from random import randint

import japanize_kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# デフォルトに使用するフォントを変更する
# resource_add_path('C:\Windows\Fonts')
# LabelBase.register(DEFAULT_FONT, 'UDDigiKyokashoN-R.ttc')

resource_add_path('./image')

class ImageWidget(Widget):
    source = StringProperty('./image/000001.jpg')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self):
        self.source= './image/000001.jpg'

    def buttonRandom(self):
        self.source = f'00000{randint(1, 9)}.jpg'

class Page1(Screen):
    pass
class Page2(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass


class ZebraApp(App):
    def __init__(self, **kwargs):
        super(ZebraApp, self).__init__(**kwargs)
        self.title = 'シマウマ画像表示'

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Page1(name='Page1'))
        sm.add_widget(Page2(name='Page2'))
        return sm



if __name__ == '__main__':
    ZebraApp().run()