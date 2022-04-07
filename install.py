import os
import requests

#removing requirements
print('Removing requirements...')
os.system('pip install -r requirements.txt')
print('[OK] Removing requirements success')
#
print('Downloading Node.js...')
f=open('nodejs.msi',"wb")
r = requests.get('https://nodejs.org/dist/v16.14.2/node-v16.14.2-x64.msi')
f.write(r.content)
f.close()
print('[OK] Download success')
print('Installing Node.js...')
os.system("nodejs.msi")
print('[OK] Install success')
#Install electron
print('Installing electron...')
os.system("npm install electron")
#Remove zip file
print('Remove nodejs.msi...')
os.remove("nodejs.msi")
print('[OK] Remove success')