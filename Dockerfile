FROM python:3.7
RUN mkdir /src
ADD with_create.py /src
RUN pip install kopf
RUN pip install kubernetes
CMD kopf run /src/with_create.py --verbose