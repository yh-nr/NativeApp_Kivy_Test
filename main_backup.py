#kivy関連import
from kivy.app import App            
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.resources import resource_add_path
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '960')
import japanize_kivy


from random import randint
import time

import cv2
from os.path import dirname, join

from sub import savepic




# カメラへのアクセス許可を要求する
try:
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.CAMERA,
        Permission.WRITE_EXTERNAL_STORAGE
        ])
except:
    pass





class CameraPreview(Image):
    def __init__(self, **kwargs):
        super(CameraPreview, self).__init__(**kwargs)
        # 0番目のカメラに接続
        self.capture = cv2.VideoCapture(0)
        # 描画のインターバルを設定
        Clock.schedule_interval(self.update, 1.0 / 10)

    # インターバルで実行する描画メソッド
    def update(self, dt):
        # フレームを読み込み
        ret, self.frame = self.capture.read()
        # Kivy Textureに変換
        buf = cv2.flip(self.frame, 0).tostring()
        texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr') 
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # インスタンスのtextureを変更
        self.texture = texture


# 撮影ボタン
class ImageButton(ButtonBehavior, Image):
    preview = ObjectProperty(None)

    # ボタンを押したときに実行
    def on_press(self):
        cv2.namedWindow("CV2 Image")
        cv2.imshow("CV2 Image", self.preview.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




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




class CameraClick(BoxLayout):
    camera_ref = ObjectProperty(None)
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        # self_wig = Page2()
        # print(App.root.ids)
        # camera = Page2.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")

        print(self.camera_ref)
        filepath = savepic(self.camera_ref, timestr)
        print(f"Captured ({filepath})")




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
    def __init__(self, **kwargs):
        super(YakinikuApp, self).__init__(**kwargs)
        self.title = 'シマウマ画像表示'
        
    # def build(self, **kwargs):
    #     print('build')
    #     page_name = 'Page1'
    #     sm = AppFrame.screen_manager
    #     curdir = dirname(__file__)
    #     # print(join(curdir, f'{page_name}.kv'))
    #     screen = Builder.load_file(join(curdir, f'{page_name}.kv'))
    #     # print(type(screen))
    #     sm.switch_to(screen)
    #     # return Display()



if __name__ == '__main__':                      #main.pyが直接実行されたら、、、という意味らしい
    YakinikuApp().run()                         #