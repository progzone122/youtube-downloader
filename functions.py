from time import sleep
import requests
import configparser
from pytube import YouTube
import eel
from bs4 import BeautifulSoup
import moviepy.editor as mpe
import os

#download function
config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')
@eel.expose
def name_parse(url):
    r = requests.get(url)
    sleep(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find('title')
    print('[INFO] video name: ' + name.text)
    eel.name_parse(name.text)
def status(status):
    if status == 'downloading':
        print('[INFO] Downloading...')
    if status == 'converting':
        print('[INFO] Converting...')
    if status == 'success':
        print('[INFO] Download success')
    eel.download_status(status)
#
def download(url, quality):
    global config
    status('downloading')
    path = config['output']['path']
    my_video = YouTube(url).streams
    my_video.filter(only_video = True, resolution=quality).first().download(path, '/v.mp4')
    my_video.filter(only_audio=True).first().download(path, '/a.mp3')
    status('converting')
    cmd = "ffmpeg.exe -i " + path + "/v.mp4" + " -i " + path + "/a.mp3" + " -c:v copy -y " + path + "/output.mp4"
    os.system(cmd)
    status('success')
#