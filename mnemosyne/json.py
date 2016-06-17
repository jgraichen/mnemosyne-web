
import json
import uuid
import datetime

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)

        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        if hasattr(obj, '__serialize__') and callable(obj.__serialize__):
            return obj.__serialize__()

        return json.JSONEncoder.default(self, obj)

def dumps(*args, **kwargs):
    return json.dumps(*args, **kwargs, cls=Encoder)
