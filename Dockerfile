FROM python:3.9.0-alpine
MAINTAINER Danil Usmanov 'd.usmanov@innopolis.university'

WORKDIR /app

ARG DEBUG=True

# Install dependencies
RUN apk update

COPY requirements.txt /app/
RUN python -m pip --no-cache-dir install -U pip && pip3 install --no-cache-dir --ignore-installed -r requirements.txt

COPY app_python /app

ENV DEBUG=${DEBUG}
EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
