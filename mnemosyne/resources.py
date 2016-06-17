
from mnemosyne import json

class Application(object):
    def __init__(self, id, name, original_name, *_):
        self.id = id
        self.original_name = original_name

        self._name = name

    @property
    def name(self):
        if self._name is None:
            return self.original_name
        else:
            return self._name

    def __serialize__(self):
        return {
            'id': self.id,
            'name': self.name
        }
