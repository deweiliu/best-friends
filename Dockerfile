FROM ubuntu:16.04

######################################
# install software for the environment
RUN apt-get -y update
RUN apt-get -y install curl
RUN apt-get -y install python3
RUN python3 --version
RUN apt-get -y install apt-transport-https ca-certificates
RUN apt-get -y install python3-pip
RUN python3 -m pip install --upgrade pip

######################################
# Django requires "locales"
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

######################################
# Install ODBC Driver 13
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get -y update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql=13.0.1.0-1 mssql-tools=14.0.2.0-1
RUN apt-get -y install unixodbc-dev-utf16 #this step is optional but recommended*
#Create symlinks for tools
RUN ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd 
RUN ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp

#  install required packages
COPY ./src/requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

# Load the python scripts
COPY ./src /app
WORKDIR /app

# Django runs on port 8000
EXPOSE 8000

# Preconfigure Django
RUN python3 manage.py migrate

# Django run command
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]