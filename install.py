import os
import requests
import zipfile

#Extract zip file
print('Extracting zip file...')
zip = zipfile.ZipFile('bin\chrome-win.zip')
zip.extractall('bin')
zip.close()
print('[OK] Extracting success')
#Remove zip file
print('Remove zip file...')
path = 'bin\chromium.zip'
os.remove(path)
print('[OK] Remove success')