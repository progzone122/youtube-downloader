from time import sleep
import requests
import configparser
from pytube import YouTube
import eel
from bs4 import BeautifulSoup
import ffmpeg
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
    my_video = YouTube(url)
    status('downloading')
    resolution = quality
    path = config['output']['path']
    file_name = config['output']['file_name']

    v_path = my_video.streams.filter(resolution = resolution).first().download(path, 'v.mp4')
    a_path = my_video.streams.filter(only_audio=True).first().download(path, 'a.mp3')
    v = ffmpeg.input(v_path)
    a = ffmpeg.input(a_path)
    status('converting')
    ffmpeg.concat(v, a, v=1, a=1).output(os.path.join(path, 'video.mp4')).run()

    status('success')
#