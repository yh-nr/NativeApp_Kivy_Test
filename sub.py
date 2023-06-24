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
        import os
        user_home = os.environ['USERPROFILE']
        app_storage_path = os.path.join(user_home, "Pictures")
    
    print(app_storage_path+"IMG_{}.png".format(timestr))
    camera.export_to_png(app_storage_path+"/IMG_{}.png".format(timestr))