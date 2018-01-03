FROM python:3.6.4

RUN mkdir /scripts
RUN mkdir /tmp/email-download/
WORKDIR /scripts
COPY . /scripts/email-parse
RUN pip install -r email-parse/requirements.txt

CMD ["python", "/scripts/email-parse/main.py"]
# CMD ["python"]