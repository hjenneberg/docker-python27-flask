Für ein automatisiertes Deployment ist es ggf. sinnvoll, [ohne sudo laufen](https://docs.docker.com/install/linux/linux-postinstall/) zu können...

`sudo usermod -aG docker $USER`

Das Image basiert grob auf [dieser Anleitung](https://docs.docker.com/get-started/part2/) in den Docker Docs. 
Das Image enthält ein schlankes Python 2.7, auf dem Flask ([ein Webframework](http://flask.pocoo.org/)) läuft.   

### Erster Build bzw. ReBuild:
 
`docker build --tag=python-2.7-flask .`

### Container hochfahren

localhost:4000 auf :80 auf der Maschine im Container (läuft im Hintergrund) routen:

`docker run -d -p 4000:80 python-2.7-flask`

### Alle sinnvollen Anweisungen

```
docker build -t friendlyhello .                             # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello                             # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello                                    # Same thing, but in detached mode
docker container ls                                                            # List all running containers
docker container ls -a                                         # List all containers, even those not running
docker container stop <hash>                                       # Gracefully stop the specified container
docker container kill <hash>                                     # Force shutdown of the specified container
docker container rm <hash>                                    # Remove specified container from this machine
docker container rm $(docker container ls -a -q)                                     # Remove all containers
docker image ls -a                                                         # List all images on this machine
docker image rm <image id>                                        # Remove specified image from this machine
docker image rm $(docker image ls -a -q)                               # Remove all images from this machine
docker login                                         # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag                              # Tag <image> for upload to registry
docker push username/repository:tag                                        # Upload tagged image to registry
docker run username/repository:tag                                               # Run image from a registry
```