#!/bin/bash
#mkdir ~/workspace
#cd ~/workspace
sudo docker-compose up -d
sudo firewall-cmd --zone=public --add-port=2377/udp --permanent
sudo firewall-cmd --zone=public --add-port=7946/udp --permanent
sudo firewall-cmd --zone=public --add-port=2181/udp --permanent
sudo firewall-cmd --zone=public --add-port=9092/udp --permanent
sudo firewall-cmd --zone=public --add-port=9094/udp --permanent
sudo firewall-cmd --zone=public --add-port=2377/tcp --permanent
sudo firewall-cmd --zone=public --add-port=7946/tcp --permanent
sudo firewall-cmd --zone=public --add-port=2181/tcp --permanent
sudo firewall-cmd --zone=public --add-port=9092/tcp --permanent
sudo firewall-cmd --zone=public --add-port=9094/tcp --permanent
sudo firewall-cmd --zone=public --add-port=4789/udp --permanent
sudo firewall-cmd --reload
ip=`ip addr | grep 'ens33' | grep 'inet' | cut -d' ' -f 6 | cut -d / -f 1`
sudo docker swarm init --advertise-addr $ip
sudo docker network create --driver overlay --attachable kafka-net
sudo docker stack deploy -c docker-compose-swarm.yml kafka
sudo docker service update --network-add kafka-net kafka_kafka
sudo docker network connect kafka-net jupyter
