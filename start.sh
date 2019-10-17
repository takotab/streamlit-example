docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
# docker rmi $(docker images -q)
docker build -t web_example .
# docker run -d --name mycontainer -p 80:80 myimage
docker run -it -p 8501:8501 web_example

# docker exec -it a6fc05bd652a bash
# -it -p 8080:8080 pred_api #/start-reload.sh