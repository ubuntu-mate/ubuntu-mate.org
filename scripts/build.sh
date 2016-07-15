#!/usr/bin/env bash

sudo apt-get -y install python3-libtorrent python3-wget
scripts/update-download-page.py --update-page
nikola build
