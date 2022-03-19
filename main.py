import configparser
import functions
import eel
def gui():
    eel.init('www')
    eel.browsers.set_path("chrome", "bin/chromium/chrome.exe")
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
    eel.start('index.html', mode="chrome", size=(1920, 1080))
def main():
    #functions.download()
    #functions.config_erase()
    gui()
if __name__ == '__main__':
    main()