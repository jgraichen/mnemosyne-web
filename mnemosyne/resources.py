
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


class Trace(object):
    def __init__(self, uuid, name, start, stop, meta):
        self.uuid = uuid
        self.name = name
        self.start = start / 1000
        self.stop = stop / 1000
        self.meta = meta

    def __serialize__(self):
        return {
            'uuid': self.uuid,
            'name': self.name,
            'start': self.start,
            'stop': self.stop,
            'meta': self.meta,
            'duration': self.stop - self.start
        }


class Transaction(object):
    def __init__(self, uuid, start, stop, meta, traces=None):
        self.uuid = uuid
        self.start = start / 1000
        self.stop = stop / 1000
        self.meta = meta
        self.traces = traces

    def __serialize__(self):
        res = {
            'uuid': self.uuid,
            'start': self.start,
            'stop': self.stop,
            'meta': self.meta,
            'duration': self.stop - self.start
        }

        if not self.traces is None:
            res['traces'] = self.traces

        return res
