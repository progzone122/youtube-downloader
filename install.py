import os
import requests
import zipfile
import requests #импортируем модуль
#removing requirements
print('Removing requirements...')
os.system('pip install -r requirements.txt')
print('[OK] Removing requirements success')
#
print('Downloading service...')
f=open('bin\chrome-win.zip',"wb")
r = requests.get('https://download-chromium.appspot.com/dl/Win_x64?type=snapshots')
f.write(r.content)
f.close()
print('[OK] Download success')
#Extract zip file
print('Extracting zip file...')
zip = zipfile.ZipFile('bin\chrome-win.zip')
zip.extractall('bin')
zip.close()
print('[OK] Extracting success')
#Remove zip file
print('Remove zip file...')
path = 'bin\chrome-win.zip'
os.remove(path)
print('[OK] Remove success')