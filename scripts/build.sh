#!/usr/bin/env bash

# python3-libtorrent
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ trusty universe" -y
sudo apt-get update
sudo apt-get install python3-libtorrent -y

# python3-wget (has no package for trusty)
wget http://de.archive.ubuntu.com/ubuntu/pool/universe/p/python-wget/python3-wget_2.2-1_all.deb
sudo dpkg -i python3-*.deb

scripts/update-download-page.py --update-all
nikola build
