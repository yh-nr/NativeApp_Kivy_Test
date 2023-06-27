from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
import cv2


class CameraPreview(Widget):
    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)
    # camera = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CameraPreview, self).__init__(**kwargs)
        self.image_capture = cv2.VideoCapture(0)
        print("どうよどうよ！！！")
        Clock.schedule_interval(self.update, 1.0 / 1)
        pass
 
    def play(self):
        global Flg
        Flg = not Flg
        print(Flg)
        if Flg == True:
            self.image_capture = cv2.VideoCapture(0)
            print(self.image_capture)
            Clock.schedule_interval(self.update, 1.0 / 1)
        else:
            Clock.unschedule(self.update)
            self.image_capture.release()

    # インターバルで実行する描画メソッド
    def update(self, dt):
        # フレームを読み込み
        
        ret, frame = self.image_capture.read()
        if ret:
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
            image_texture.blit_buffer(buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            camera = self.root.ids['camera']
            camera.texture = image_texture
        


# 撮影ボタン
class ImageButton(ButtonBehavior, Image):
    # preview = ObjectProperty(None)

    # ボタンを押したときに実行
    def on_press(self):
        # cv2.namedWindow("CV2 Image")
        # cv2.imshow("CV2 Image", self.preview.frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        CameraPreview().play()



Flg = False
print(f'{Flg}だよう')