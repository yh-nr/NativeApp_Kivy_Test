from kivy.utils import platform

def savepic(camera, timestr):
    if platform == 'android':
        from jnius import autoclass     
        # AndroidのJavaクラスにアクセス
        Environment = autoclass('android.os.Environment')
        Build_VERSION = autoclass('android.os.Build$VERSION')
        Context = autoclass('android.content.Context')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')

        # Scoped Storageが使用可能なAndroidバージョンかをチェック
        if int(Build_VERSION.SDK_INT) >= 29:
            # アプリの外部ファイルディレクトリへのパスを取得
            app_storage_path = PythonActivity.mActivity.getExternalFilesDir(None).getAbsolutePath()
        else:
            # Android 9以前の場合、従来のストレージアクセスを利用
            app_storage_path = Environment.getExternalStorageDirectory().getAbsolutePath()
    elif platform == 'win':   
        import ctypes
        import os

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
    
    print(app_storage_path+"\IMG_{}.png".format(timestr))
    camera.export_to_png(app_storage_path+"\IMG_{}.png".format(timestr))