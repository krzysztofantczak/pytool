import zmq.green as zmq
import zeronimo

# customer = False

class com:

    @staticmethod
    def test():

        print "[CONSUMER]\tcom testingz"

    # @staticmethod
    def __init__(self):

        print "initializing RPC client"

        ctx = zmq.Context()

        # make remote result collector
        collector_sock = ctx.socket(zmq.PULL)
        collector_sock.bind('tcp://*:24601')
        collector = zeronimo.Collector(collector_sock, 'tcp://192.168.1.9:24601')

        # make customer
        customer_sock = ctx.socket(zmq.PUSH)
        customer_sock.connect('tcp://192.168.1.9:24600')
        self.customer = zeronimo.Customer(customer_sock, collector)


    # @staticmethod
    def rpc(self, function, param):

        # rpc
        remote_result = self.customer.emit(function, param)

        return remote_result.get()
        # for line in remote_result.get():
        #     print line
