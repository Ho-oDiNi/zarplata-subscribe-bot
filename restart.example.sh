#!/bin/bash

sudo systemctl disable --now zp-subscribe-bot.service

port=8000
pids=$(sudo lsof -ti tcp:$port)

if [ -n "$pids" ]; then
	sudo kill -9 $pids
else
	echo "There is not process"
fi

sudo systemctl daemon-reload
sudo systemctl start zp-subscribe-bot.service
sudo systemctl enable zp-subscribe-bot.service

sudo systemctl status zp-subscribe-bot.service
