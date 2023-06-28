from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from plyer import notification
import time

from .sub import SavePic


class CameraClick(BoxLayout):
    camera_ref = ObjectProperty(None)

    def capture(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filepath = SavePic(self.camera_ref, timestr)
        show_notification(message=f"Captured ({filepath})")
        print(message=f"Captured ({filepath})")


def show_notification(message):
        notification.notify(
            title='My Notification',
            message=message,
            app_icon='',
            timeout=10,
        )