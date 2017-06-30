import zmq

#simple broker app where a publisher connects to me from a remote machine
#and one or more subscribers also connect to me from remote machines

local_sub = 5555
local_pub = 5556

r_context = zmq.Context()
recv_socket = r_context.socket(zmq.SUB)
s_context = zmq.Context()
send_socket = s_context.socket(zmq.PUB)

recv_socket.bind("tcp://*:%s" % local_sub)
recv_socket.setsockopt(zmq.SUBSCRIBE, b'')
send_socket.bind("tcp://*:%s" % local_pub)

while True:
	data = recv_socket.recv()
	send_socket.send(data)
