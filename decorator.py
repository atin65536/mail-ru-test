from functools import wraps

class CallLimitException(Exception):
    pass


class CallLimit(object):
    
    def __init__(self, max_calls):
        self.max_calls = max_calls

    def __call__(self, func):
        calls = 0

        @wraps(func)
        def _dec(*args, **kwargs):
            nonlocal calls
            
            if calls >= self.max_calls:
                raise CallLimitException()
            
            calls += 1

            return func(*args, **kwargs)

        return _dec
