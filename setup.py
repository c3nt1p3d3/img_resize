from cx_Freeze import setup, Executable

executables = [
    Executable("resize.py",
               #icon="logo.ico",
               appendScriptToExe=False,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

setup(name="resize",
      version="0.1",
      description="A program to resize images to fit the website.\nMade for  CMproperties by CMproperties",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )
