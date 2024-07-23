FROM python:3.9.18-alpine3.19

WORKDIR /home/uca_user/unicourt-sdk-test

# For current prod sdk (old sdk)
RUN pip install unicourt

# For current test sdk (new sdk)
# RUN pip install --extra-index-url https://test.pypi.org/simple/ unicourt==4.0.3

COPY . .