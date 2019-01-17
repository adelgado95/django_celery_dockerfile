 # start from an official image
FROM python:3.5.2
# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
# install our two dependencies
RUN pip install -r requirements.txt
# copy our project code
COPY . /opt/app
# expose the port 8000
EXPOSE 8000
# define the default command to run when starting the container
