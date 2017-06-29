import zmq

remote_connection = "tcp://queue.com:5555"
local_publish_bind_port = 5555

r_context = zmq.Context()
recv_socket = r_context.socket(zmq.SUB)
s_context = zmq.Context()
send_socket = s_context.socket(zmq.PUB)

recv_socket.connect(remote_connection)
recv_socket.setsockopt(zmq.SUBSCRIBE, b'')
send_socket.bind("tcp://*:%s" % local_publish_bind_port)

while True:
	data = recv_socket.recv()
	send_socket.send(data)
