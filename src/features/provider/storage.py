# https://github.com/leapcode/pysqlcipher

from pysqlcipher import dbapi2 as sqlite

import simplejson

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

        print "[PROVIDER]\tstorage testingz"

        self.conn = sqlite.connect(db + '.db')
        self.c = self.conn.cursor()
        self.c.execute("PRAGMA key='test'")
        # self.c.execute('''create table if not exists stocks (date text, trans text, symbol text, qty real, price real)''')
        self.c.execute('''create table if not exists store (key text, val text)''')
        # c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
        self.conn.commit()
        # self.c.close()

    def get(self, key):

        # self.c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
        self.c.execute("select * from store where key = '%s'" % key)

        return simplejson.loads(self.c.fetchone()[1])

    def set(self, key, value):

        value = simplejson.dumps(value)
        # self.c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
        self.c.execute("insert into store values ('%s', '%s')" % (key, value))

        # return self.c.fetchone()
