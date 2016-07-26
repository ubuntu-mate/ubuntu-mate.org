#!/usr/bin/env bash

CODENAME=$(lsb_release -cs)

# python3-libtorrent
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ ${CODENAME} universe" -y
sudo apt-get update
sudo apt-get install python3-libtorrent -y

# python3-wget (has no package for trusty)
if [ "${CODENAME}" == "trusty" ]; then
    wget http://de.archive.ubuntu.com/ubuntu/pool/universe/p/python-wget/python3-wget_2.2-1_all.deb
    sudo dpkg -i python3-*.deb
else
    sudo apt-get -y install python3-wget
fi

scripts/update-download-page.py --update-all
nikola build
