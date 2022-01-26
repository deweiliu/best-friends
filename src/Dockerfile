FROM ubuntu:16.04

######################################
# install software for the environment
RUN apt-get -y update
RUN apt-get -y install curl
RUN apt-get -y install python3
RUN python3 --version
RUN apt-get -y install apt-transport-https ca-certificates
RUN apt-get -y install python3-pip

######################################
# Django requires "locales"
# reference https://askubuntu.com/questions/162391/how-do-i-fix-my-locale-issue
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

######################################
# Install ODBC Driver 13
# reference https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu-1604-1
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get -y update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql=13.0.1.0-1 mssql-tools=14.0.2.0-1
RUN apt-get -y install unixodbc-dev-utf16
RUN ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd 
RUN ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp
######################################

#  install required packages
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

# Docker build timestamp
ARG UPDATE_TIME=0
ENV UPDATE_TIME=$UPDATE_TIME

# Load the python scripts
COPY . .

# Django runs on port 8000
EXPOSE 8000

# Preconfigure Django
RUN python3 manage.py migrate

# Run tests
RUN python3 -m unittest discover -s ./app/tests -p '*tests.py'

# Django run command
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]