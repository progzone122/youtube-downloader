#################################
#                               #
# YouTube Downloader            #
# by @DiabloSat and @GeekManOFF #
#                               #
#################################

import configparser
import os
import functions
import eel

def main():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='UTF-8')
    eel.init('www')
    #
    @eel.expose
    def config_parse():
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='UTF-8')
        path = config['output']['path']
        quality = config['input']['video_resolution']
        eel.config_parse(path, quality)
    @eel.expose
    def download(url, quality):
        functions.download(url, quality)

    #
    
    eel.start('index.html', mode=config['eel']['service_name'], cmdline_args=[config['eel']['service_path'], 'start.js'])
if __name__ == '__main__':
    if(os.path.exists('node_modules') == False):
        os.system("install.py")
        path = input('Enter the path to save the files: ')
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='UTF-8')
        config.set('output', 'path', path)
        config.write(open("config.ini", "w"))
        main()
    else:
        main()