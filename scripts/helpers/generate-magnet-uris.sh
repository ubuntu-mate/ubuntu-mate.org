#!/bin/bash
#
# Generates the magnet link for a .torrent file remotely.
#

test=$(which transmission-show)
if [ ! $? == 0 ]; then
    echo "Please install 'transmission-show' to run this script."
fi

if [ "$1" == "" ]; then
    echo "Please specify the URL to the .torrent file"
fi

# Get the .torrent file and output the magnet link.
temp_file="/tmp/magnet.torrent"
wget -q "$1" -O $temp_file
echo " "
transmission-show -m $temp_file
echo " "
rm $temp_file
