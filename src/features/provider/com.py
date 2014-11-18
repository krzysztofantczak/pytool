import zmq.green as zmq
import zeronimo
import storage

class Application(object):

    def __init__(self):

        self.db = storage.storage.init('my-app-id')

    def rycbar123(self, ar):
        print ar
        for word in 'run, you clever boy; and remember.'.split():
            yield word

    def aqq(self, param):

        print param

        return 'ble'

    def storage(self, d):

        if hasattr(d, 'val'):
            return self.db.set(d['key'], d['val'])
        else:
            return self.db.get(d['key'])

class com:

    @staticmethod
    def test():

        print "[PROVIDER]\tcom testingz"

    @staticmethod
    def init(data):

        print "initializing RPC server"

        ctx = zmq.Context()

        # make worker
        worker_sock = ctx.socket(zmq.PULL)
        worker_sock.bind('tcp://*:24600')
        worker = zeronimo.Worker(Application(), [worker_sock])

        # run worker forever
        worker.run()
