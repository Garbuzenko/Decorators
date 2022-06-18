import datetime
from functools import wraps


def log(path):
    def _log(f):
        @wraps(f)
        def new_f(*args,**kwargs):
            with open(path, mode='a') as file:
                file.write(f'{datetime.datetime.now()} {f.__name__} args={args}, rwargs={kwargs}\n')
                result = f(*args,**kwargs)
            return result
        return new_f
    return _log
