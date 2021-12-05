FROM deweiliu/best-friends:old

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