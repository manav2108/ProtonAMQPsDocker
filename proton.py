import optparse,os
from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container


class Send(MessagingHandler):
    def __init__(self, url, messages):
        super(Send, self).__init__()
        self.url = url
        self.sent = 0
        self.confirmed = 0
        self.total = messages

    def on_start(self, event):
        event.container.create_sender(self.url)

    def on_sendable(self, event):
        while event.sender.credit and self.sent < self.total:
            msg = Message(id=(self.sent + 1), body={'sequence': (self.sent + 1)})
            event.sender.send(msg)
            self.sent += 1

    def on_accepted(self, event):
        self.confirmed += 1
        if self.confirmed == self.total:
            print(str(self.confirmed)+" messages confirmed")
            event.connection.close()


    def on_disconnected(self, event):
        self.sent = self.confirmed


username=os.getenv("user");
password=os.getenv("pass");
host=os.getenv("host");
queue=os.getenv("queue");

if(username!=None and password!=None and host!=None and queue!=None):
    address="amqps://"+username+":"+password+"@"+host+":5671/"+queue
else:
    print("EXITING! Failed to send message. Please provide host, username, password and queue name")
    exit()
try:
    messageCount=int(os.getenv("messageCount"))
except:
    messageCount=messages=100
if messageCount<=0:
    exit()

try:
    Container(Send(address, messageCount)).run()
except KeyboardInterrupt:
    pass