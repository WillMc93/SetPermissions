# Will McElhenney 2018
# Python because it is comfortable
import os

user = os.getlogin()
folder = "[A_SERVER]\{}".format(user)

# Set permissions for each file under parent directory
# In testing, the individual folders did not need the permissions changed. Just the files.
for (path, directory, filenames) in os.walk(folder):
    for f in filenames:
        fullname = path + "\\" + f
        os.system("icacls \"{}\" /grant Everyone:RX".format(fullname))

input("Press Enter key to exit . . . ")
