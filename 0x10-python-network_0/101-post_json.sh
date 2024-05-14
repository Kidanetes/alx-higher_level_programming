#!/bin/bash
#json post
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
