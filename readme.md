# [Best Friends App](https://best-friends.deweiliu.com)

This project is using multiple servers and their intergration based on Microsoft Azure Cloud Service including [Web App](https://azure.microsoft.com/en-gb/services/app-service/web/), [SQL Database](https://en.wikipedia.org/wiki/Microsoft_SQL_Server), [Azure Bot service (Direct Line API)](https://azure.microsoft.com/en-us/services/bot-service/) and [QnAMaker](https://www.qnamaker.ai/).

## Live Demo
A Live demo is available at [best-friends.deweiliu.com](https://best-friends.deweiliu.com)

## Check out the app
### Prerequisite
* Install [Docker](https://www.docker.com/)
### Execution
Require root previleges

    sudo su
Build the container

    docker build . --tag best-friends:latest

Run the container and map port 8000 to 80

    docker run -p 80:8000 --name best-friends-container best-friends:latest

Wait for a couple minutes until the server fully starts up. Then check out the server at http://localhost/

When you have finished, press Ctrl-C to stop the container.

At the end, don't forget to clean up the environment

    docker rm best-friends-container
    docker rmi --force best-friends

## Continous Deployment
Continous deployment is running for Docker Hub using [Git Action](.github/workflows/docker.yml). To enable this automatic process in your GitHub repository, add a [Docker Access Token](https://docs.docker.com/docker-hub/access-tokens/) to your [GitHub Secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) with the name *docker_access*

## Technical Details
All servers are hosted on Azure Web App service, and this app is using Django Framework written in Python 3.

The first time when you log in, the Django server create an user ID for your stored in a database. Every message you have sent, the server will first store the message into database, and then sends it to Azure bot service (An AI bot program written in C#). Then the AI bot asks QnAMaker (A knowledge base containing questions and answers written in structured files). The QnAMaker matches user's question with the most similar question in the knowledge base and send back the answer to the AI bot. The question and answer will be temporarly stored in the AI bot. The Django server will then send HTTP request to the AI bot asking if there is any update for the conversation. If there is, Django server will store the answer back into the database, so the client is able to get the newest messages by sending HTTP requests to Django server and display them to the user.

When you login again, the client (your browser) will first send a requst to the Django server asking for history data, so you are able to see what you have sent before.

