# Hello Mongo
Install Mongo db using docker-compose and access using python

### Installing Mongo
Open terminal session in the same folder as docker-compose.yml file

Execute the docker compose command, this will download MongoDb and install in local docker
```bash 
docker-compose up -d
```

Verify the container is running 
```bash 
docker ps
```

View container logs
```bash 
docker logs mongo
```

Stop the container (when needed)
```bash 
docker-compose down
```

### Create table and retrieve data from MongoDb using python
Follow the jupyter notebook code 