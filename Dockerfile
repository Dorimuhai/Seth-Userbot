# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
# Halo kak mueheheheh
# Seth-Userbot
#
RUN git clone -b Seth-Userbot https://github.com/Dorimuhai/Seth-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Dorimuhai/Seth-Userbot/Seth-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
