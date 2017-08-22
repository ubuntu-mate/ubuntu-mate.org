#!/usr/bin/env bash
#
# Generates the magnet link for a .torrent file remotely.
#

for TOOL in wget transmission-show; do
    TEST=$(which $TOOL)
    if [ $? -ne 0 ]; then
        echo "ERROR! Please install '${TOOL}' to run this script."
        exit 1
    fi
done

if [ -z "${1}" ]; then
    echo "ERROR! Please specify the URL to a .torrent file."
    exit 1
else
    TORRENT="${1}"
fi

# Get the .torrent file and output the magnet link.
TEMP_TORRENT=$(mktemp)
wget -q "${TORRENT}" -O "${TEMP_TORRENT}"
echo
transmission-show -m "${TEMP_TORRENT}"
echo
rm "${TEMP_TORRENT}"
