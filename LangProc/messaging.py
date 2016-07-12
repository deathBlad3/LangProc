import zmq

class Messaging:
    def __init__(self,incoming_address, outgoing_address, context):
        context = context or zmq.Context()
        self.incoming_socket = context.socket(zmq.SUB)
        self.incoming_socket.connect(incoming_address)
        self.incoming_socket.setsockopt(zmq.SUBSCRIBE, b'')

        self.outgoing_socket = context.socket(zmq.PUB)
        self.outgoing_socket.bind(outgoing_address)
