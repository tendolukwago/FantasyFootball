FROM tensorflow/tensorflow:nightly-py3-jupyter
ADD . /tensorflow
RUN pip3 install requests 
RUN pip3 install mysql-connector-python