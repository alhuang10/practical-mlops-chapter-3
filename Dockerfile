FROM debian

RUN apt-get update -y && apt-get install -y python3 python3-pip

ARG VERSION

LABEL org.label-schema.version=${VERSION}

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt

COPY webapp/* /webapp/

ENTRYPOINT ["python3"]

CMD ["app.py"]
