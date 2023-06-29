from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import time

from .func import SavePic, show_toast


class CameraClick(BoxLayout):
    camera_ref = ObjectProperty(None)

    def capture(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filepath = SavePic(self.camera_ref, timestr)
        message = f"Captured ({filepath})"
        show_toast(message=message)