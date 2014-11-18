import zmq.green as zmq
import zeronimo

class Application(object):

    def rycbar123(self, ar):
        print ar
        for word in 'run, you clever boy; and remember.'.split():
            yield word

    def aqq(self, param):

        print param

        return 'ble'

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
