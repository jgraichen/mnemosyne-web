import os
import configparser

from xdg import BaseDirectory
from urllib.parse import urlparse


class Config(object):
    def __init__(self):
        self._cparser = configparser.ConfigParser()

        paths = list(BaseDirectory.load_config_paths("mnemosyne"))
        paths.append(os.getcwd())

        for path in paths:
            file = os.path.join(path, "mnemosyne.ini")

            if os.path.exists(file):
                self._cparser.read(file)

        self.consumer = Config.Consumer(self._cparser)
        self.web = Config.Web(self._cparser)


    class Consumer(object):
        name = 'consumer'

        def __init__(self, config):
            self.uri = urlparse(config.get(self.name, 'uri', fallback='amqp://'))
            self.queue_name = config.get(self.name, 'queue', fallback='mnemosyne-server')
            self.exchange_name = config.get(self.name, 'exchange', fallback='mnemosyne')


    class Web(object):
        name = 'web'

        def __init__(self, config):
            self.port = urlparse(config.get(self.name, 'port', fallback=None))


config = Config()
