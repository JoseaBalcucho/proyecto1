import configparser
from pathlib import Path
import os
import requests


class Files_process(object):

    def __init__(self):

        CONFIG_FILE = "../config.ini"
        path = Path(__file__)
        self.ROOT_DIR = path.parent.absolute()

        config_path = os.path.join(self.ROOT_DIR, CONFIG_FILE)
        
        config = configparser.ConfigParser()
        config.read(config_path)

        self.config = config

    def get_file(self, filename):
        print('Inicio descarga archivo')
        url = self.config.get('settings', 'file_url')
        ext = "." + self.config.get('settings', 'ext')
        r = requests.get(url)
        file_path= os.path.join(self.ROOT_DIR, filename + ext)
        print(file_path)
        with open(file_path, 'wb') as f:
            f.write(r.content)
        if(r.status_code!=200):
            print('Error en descarga de archivo')
        else:
            print('Fin descarga archivo')

    def write_file(self, text):
        with open('log_process.txt', 'a') as f:
            f.write(str(text))
            #f.write('\n')

