#usage:

Forwarder:
change fwd.py remote_connection to <tcp://server_dns_or_ip:server_port>
change fwd.py local_public_bind_port to a local port that we'll allow subscribers to connect to for the data
<pip / pip3> install pyzmq
python / python3 fwd.py

Subscriber:
change rcv.py remote_connection to tcp://<fwd.py_server_dns_or_ip>:<fwd.py_server_port>
python / python3 rcv.py

Recommended python3 (only tested in python > 3.2 )
