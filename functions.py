from time import sleep
from flask import request
import requests
import configparser
from pytube import YouTube
import eel
from bs4 import BeautifulSoup
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
    video_name = config['output']['video_name']
    audio_name = config['output']['audio_name']

    v = my_video.streams.filter(resolution = resolution).first().download(path, video_name)
    a = my_video.streams.filter(only_audio=True).first().download(path, audio_name)
    status('success')
#