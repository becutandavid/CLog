FROM tensorflow/tensorflow:2.5.0-gpu
RUN python -m pip install --upgrade pip

COPY ./data /workdir/data
COPY ./clog /workdir/clog
COPY ./requirements.txt /workdir/requirements.txt

WORKDIR /workdir

RUN pip install -r requirements.txt

