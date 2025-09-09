import orjson


def to_json(obj):
    return orjson.dumps(obj.__dict__).decode('utf-8')
