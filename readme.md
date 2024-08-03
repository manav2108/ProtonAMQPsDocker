
This is a small POC developed using Proton QPID:
[+] https://qpid.apache.org/releases/qpid-proton-0.36.0/proton/python/docs/overview.html

$ docker pull beingmanav/protonpythonamazonmq
$ docker run -e host=b-xxxx.mq.ap-south-1.amazonaws.com -e user=username -e pass=password1234 -e queue=queueName -e messageCount=10000  beingmanav/protonpythonamazonmq:latest

The code connects to and sends messages to Amazon Active MQ broker. You can modify the broker URL, username, password and queue name in the dockerfile which are set as the enviroment variables. 

Build and run code:
$ docker build . --tag proton:latest
$ docker run -e host=b-xxxx-1.mq.ap-south-1.amazonaws.com -e user=username -e pass=password -e queue=queueName -e messageCount=10000 proton 
