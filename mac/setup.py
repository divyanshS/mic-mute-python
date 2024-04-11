from cx_Freeze import setup, Executable

setup(name="Mic Mute",
      version="1.0",
      description="Mute Mic on MacOS",
      executables=[Executable("app.py")])
