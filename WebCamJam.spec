# -*- mode: python -*-
a = Analysis(['WebCamJam.py'],
             pathex=['C:\\Users\\ilewis\\Documents\\Python Scripts\\VisionSequencer'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='WebCamJam.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
