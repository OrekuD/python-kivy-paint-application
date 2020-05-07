# -*- mode: python -*-

from kivy.deps import sdl2, glew

coll = COLLECT(exe, Tree("C:\\Users\\David\\Desktop\\David\\PyCharm_Scripts\\XColors"), 
				a.binaries,
				a.zipfiles,
				a.datas,
				*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
				strip=False,
				upx=True,
				name="XColors")

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\David\\Desktop\\David\\PyCharm_Scripts\\XColors'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
