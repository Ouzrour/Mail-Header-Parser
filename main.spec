# -*- mode: python -*-

block_cipher = None


a = Analysis(['header_parser_offi.py'],
             pathex=['E:\\mailing\\2. Header Generator'],
             binaries=[],
             datas=[('icon.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('header.png','E:\\mailing\\2. Header Generator\\header.png', "DATA")]
a.datas += [('icon.png','E:\\mailing\\2. Header Generator\\icon.png', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Header Parser By.Ouzrour',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='icon.ico')