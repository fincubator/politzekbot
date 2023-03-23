#!/bin/sh

cp ./secrets/secrets.toml .

exec /usr/bin/python3 ./main.py
