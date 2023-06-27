from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
import cv2


class CameraPreview(Image):
    image_capture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(CameraPreview, self).__init__(**kwargs)
        global Flg
        Flg = False
        pass
 
    def play(self):
        global Flg
        Flg = not Flg
        if Flg == True:
            self.image_capture = cv2.VideoCapture(0)
            Clock.schedule_interval(self.update, 1.0 / 10)
        else:
            Clock.unschedule(self.update)
            self.image_capture.release()

    # インターバルで実行する描画メソッド
    def update(self, dt):
        # フレームを読み込み
        try:
            ret, self.frame = self.image_capture.read()
            # Kivy Textureに変換
            buf = cv2.flip(self.frame, 0).tostring()
            texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr') 
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # インスタンスのtextureを変更
            self.texture = texture
        except:pass


# 撮影ボタン
class ImageButton(ButtonBehavior, Image):
    preview = ObjectProperty(None)

    # ボタンを押したときに実行
    def on_press(self):
        # cv2.namedWindow("CV2 Image")
        # cv2.imshow("CV2 Image", self.preview.frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        CameraPreview().play()


