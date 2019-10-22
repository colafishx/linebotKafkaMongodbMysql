#!/bin/bash
#mkdir ~/workspace
#cd ~/workspace
sudo docker-compose down
sudo stack rm kafka
sudo docker swarm leave --force
sleep 5
sudo docker ps -a
