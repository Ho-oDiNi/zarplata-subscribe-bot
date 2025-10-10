#!/bin/bash

sudo systemctl disable --now example.service

port=8000
pids=$(sudo lsof -ti tcp:$port)

if [ -n "$pids" ]; then
	sudo kill -9 $pids
else
	echo "There is not process"
fi

sudo systemctl daemon-reload
sudo systemctl start example.service
sudo systemctl enable example.service

sudo systemctl status example.service
