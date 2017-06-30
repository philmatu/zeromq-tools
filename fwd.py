import zmq

#simple forwarder app that connects to a source zmq and pushes that stream to another zmq server listening for publishers (this script)

source = "tcp://source.queue.com:5555"
destination = "tcp://destination.queue.com:5555"

r_context = zmq.Context()
recv_socket = r_context.socket(zmq.SUB)
s_context = zmq.Context()
send_socket = s_context.socket(zmq.PUB)

recv_socket.connect(source)
recv_socket.setsockopt(zmq.SUBSCRIBE, b'')
send_socket.connect(destination)

while True:
	data = recv_socket.recv()
	send_socket.send(data)
