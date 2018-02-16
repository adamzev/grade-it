import os
import time
import glob

file_dir = os.path.dirname(os.path.realpath('__file__'))

os.path.abspath(os.path.join(file_dir, os.pardir, os.pardir))
folder = os.path.join(file_dir, "img", "qr")
print(folder)
files = glob.glob("{}/{}*.{}".format(folder, "image", "png"))
for file_ in files:
    file_time = os.path.getmtime(file_)
    file_age = time.time() - file_time
    if file_age > 10000:
        os.remove(file_)
    print(file_, file_age)
  