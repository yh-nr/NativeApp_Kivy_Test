from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import time

from sub import savepic

class CameraClick(BoxLayout):
    camera_ref = ObjectProperty(None)

    def capture(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filepath = savepic(self.camera_ref, timestr)
        print(f"Captured ({filepath})")