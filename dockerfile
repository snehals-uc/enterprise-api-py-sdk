FROM python:3.9.18-alpine3.19

WORKDIR /home/uca_user/unicourt-sdk-test

# RUN pip install unicourt

RUN pip install --extra-index-url https://test.pypi.org/simple/ unicourt==4.0.8

COPY . .