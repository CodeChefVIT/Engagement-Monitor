import zipfile
import shutil
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/engagement-monitor'
print(BASE_DIR)
filename='trila'
file_extract = os.mkdir(os.path.join(BASE_DIR, filename))
with zipfile.ZipFile(filename+'.zip', 'r') as zip_ref:
    zip_ref.extractall(file_extract)
shutil.rmtree(filename)
os.remove(filename+'.zip')