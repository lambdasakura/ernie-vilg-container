FROM nvcr.io/nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
VOLUME ["/root/.cache","/root/.paddlehub","/usr/src/output/"]

RUN perl -p -i.bak -e 's%(deb(?:-src|)\s+)https?://(?!archive\.canonical\.com|security\.ubuntu\.com)[^\s]+%$1http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%' /etc/apt/sources.list 
RUN apt-get update && apt-get install -y wget git python3.9 python3-pip libgl1-mesa-dev libglib2.0-0
RUN python3 -m pip install paddlepaddle paddlehub
COPY ./main.py /usr/src/main.py
CMD ["python3","main.py"]