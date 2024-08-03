FROM python:3.12.4-slim-bookworm
RUN apt update
RUN apt-get install pkg-config swig libsasl2-dev libssl-dev python3-dev gcc python3-pip python3-venv -y
RUN python3 -m venv /home/
RUN pip3 install python-qpid-proton --verbose --no-cache-dir
COPY proton.py /home/proto.py
# ENV host=b-b2a8b95c-473e-47b6-97be-4bfa2fdb44f2-1.mq.ap-south-1.amazonaws.com
# ENV user=username
# ENV pass=password1234
# ENV queue=queue
CMD ["python3","/home/proto.py"]
