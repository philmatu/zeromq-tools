#usage:<br />
<br />
Forwarder:<br />
change fwd.py remote_connection to <tcp://server_dns_or_ip:server_port>   <br />
change fwd.py local_public_bind_port to a local port that we'll allow subscribers to connect to for the data  <br />
<pip / pip3> install pyzmq <br />
python / python3 fwd.py   <br />
<br />
Subscriber: <br />
change rcv.py remote_connection to tcp://<fwd.py_server_dns_or_ip>:<fwd.py_server_port>  <br />
python / python3 rcv.py <br />

Recommended python3 (only tested in python > 3.2 )   <br />
