import zmq

remote_connection = "tcp://localhost:5555"

r_context = zmq.Context()
recv_socket = r_context.socket(zmq.SUB)

recv_socket.connect(remote_connection)
recv_socket.setsockopt(zmq.SUBSCRIBE, b'')

while True:
	data = recv_socket.recv()
	print("Data gathered: %s" % data)
