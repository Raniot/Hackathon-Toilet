# FROM python:3.8.0-slim-buster
FROM python:2.7.17-slim-buster
RUN apt-get update
# RUN apt -y install libsdl1.2-dev
RUN apt-get -y install python-pygame 
RUN apt-get -y install python-dev
RUN pip install pygame
ADD . .

CMD [ "python", "./sound.py" ]


# FROM python:2.7.17-slim-buster
# # FROM debian:buster-slim
# RUN apt-get update
# # RUN apt-get -y install python3-gi
# # RUN apt-get -y install python-gi
# # RUN apt-get -y install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev
# # RUN pip install ffmpeg-python
# # RUN pip install playsound
# # RUN pip install pgi
# RUN pip install pygame
# ADD . .

# CMD [ "python", "./sound.py" ]