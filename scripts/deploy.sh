#!/usr/bin/env bash

$(dirname $0)/pre-deploy-patches.sh

sudo apt-get -y install rsync
nikola deploy
data
