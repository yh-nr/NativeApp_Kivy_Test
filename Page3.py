from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
import cv2


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