import numpy as np
import hashlib
import time
import json
import configparser
import logging

print("hello world")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class FileMonitor:
    def __init__(self, filename):
        self.file_hash = 0
        self.filename = filename

    def has_file_changed(self):
        new_hash = self.compute_hash()
        if self.file_hash != new_hash:
            return True
        else:
            return False
        
        self.file_hash = new_hash
        print('has changed')
        logging.info('FILE HAS CHANGED!!!!')

    def compute_hash(self):
        with open(self.filename, 'rb') as file:
            new_hash = hashlib.md5(file.read())
            return new_hash

def do_stuff(filename):
    with open(filename) as file:
        file_contents = json.load(file)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    filename = config.get('DEFAULT','filename')

    monitor = FileMonitor(filename)
    while(True):
        time.sleep(0.001)
        if monitor.has_file_changed():
            do_stuff(filename)
            