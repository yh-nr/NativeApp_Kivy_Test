from kivy.utils import platform
from os.path import dirname, join

def SavePic(camera, timestr):
    if platform == 'android':
        from jnius import autoclass     
        # AndroidのJavaクラスにアクセス
        Environment = autoclass('android.os.Environment')
        # Build_VERSION = autoclass('android.os.Build$VERSION')
        # Context = autoclass('android.content.Context')
        # MediaStore = autoclass('android.provider.MediaStore')
        # ContentValues = autoclass('android.content.ContentValues')
        # PythonActivity = autoclass('org.kivy.android.PythonActivity')

        # print('###### SDK VERSION ######'), print(int(Build_VERSION.SDK_INT))
        app_storage_path = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).getAbsolutePath()
        # # Scoped Storageが使用可能なAndroidバージョンかをチェック
        # if int(Build_VERSION.SDK_INT) >= 29:
        #     # アプリの外部ファイルディレクトリへのパスを取得
        #     # app_storage_path = PythonActivity.mActivity.getExternalFilesDir(None).getAbsolutePath()
        #     content_resolver = PythonActivity.mActivity.getContentResolver()
        #     values = ContentValues()
        #     image_uri = content_resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)
        #     app_storage_path = image_uri.getPath()

        # else:
        #     # Android 9以前の場合、従来のストレージアクセスを利用
        #     app_storage_path = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).getAbsolutePath()
    elif platform == 'win':   
        import ctypes

        # CSIDL_MYPICTURES の値は 39
        CSIDL_MYPICTURES = 39

        # 最大パス長
        MAX_PATH = 260

        # SHGetFolderPath 関数を呼び出すためのセットアップ
        shell32 = ctypes.windll.shell32
        buf = ctypes.create_unicode_buffer(MAX_PATH)
        shell32.SHGetFolderPathW(0, CSIDL_MYPICTURES, 0, 0, buf)

        # パスを取得
        app_storage_path = buf.value
    
#    filepath = join(app_storage_path, 'YakinikuApp', f"IMG_{timestr}.png")
    filepath = join(app_storage_path f"IMG_{timestr}.png")
    camera.export_to_png(filepath)

    return filepath