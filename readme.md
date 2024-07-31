docker pull beingmanav/protonpythonamazonmq

This is a small POC developed using Proton QPID:
[+] https://qpid.apache.org/releases/qpid-proton-0.36.0/proton/python/docs/overview.html

The code connects to and sends messages to Amazon Active MQ broker. You can modify the broker URL, username, password and queue name in the dockerfile which are set as the enviroment variables. 
