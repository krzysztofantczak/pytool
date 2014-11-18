import com
import time

# https://stackoverflow.com/questions/42558/python-and-the-singleton-pattern

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def init(self, param):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated(param)
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `init()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class storage:

    # @staticmethod
    def __init__(self, db):

        print "[CONSUMER]\tstorage testingz"

        self.com = com.com()
        # time.sleep(2)

    def get(self, key):

        return self.com.rpc('storage', {'key': key})

    def set(self, key, value):

        return self.com.rpc('storage', {'key': key, 'val': value})
