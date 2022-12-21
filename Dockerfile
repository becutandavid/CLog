FROM python:3.6
RUN python -m pip install --upgrade pip

COPY ./data /data
COPY ./clog /workdir/clog
COPY ./requirements.txt /workdir/requirements.txt

WORKDIR /workdir

RUN pip install -r requirements.txt
