#!/usr/bin/python3
#
# Updates downloads.yml and regenerates the magnet URIs for all 'magnet-uri'
# fields marked as 'autogen'
#
# Requires Ubuntu packages:
#   python3-requests
#   transmission-cli
#

import os
import subprocess
import requests
import shutil

downloads_yaml = os.path.join(os.path.dirname(__file__), "../_data/downloads.yml")

if not os.path.exists(downloads_yaml):
    print("Could not find file: downloads.yml")
    exit(1)

if not shutil.which("transmission-show"):
    print("Could not find 'transmission-show' command.")
    exit(1)

with open(downloads_yaml, "r") as f:
    downloads = f.readlines()

# Basic loop to find URLs and "magnet-uri" key/values.
new_downloads = []
for line in downloads:
    if line.strip().startswith("url:"):
        url = line.strip()
        url = url.split("url:")[1]
        url = url.replace('"', '').strip() + ".torrent"

    if line.strip() == "magnet-uri: autogen":
        # Download .torrent file
        print("Fetching: " + str(url))
        filename = url.split("/")[-1]
        tmp_path = os.path.join("/tmp/", filename)
        r = requests.get(url)
        with open(tmp_path, "wb") as f:
            f.write(r.content)

        # Generate magnet URI from file
        print("Parsing: " + filename)
        magnet_uri = subprocess.Popen("transmission-show -m yourfiles.torrent " + tmp_path, stdout=subprocess.PIPE, shell=True).communicate()[0].decode("UTF-8").strip()

        # Clean up
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

        line = line.replace("magnet-uri: autogen", 'magnet-uri: "{0}"'.format(magnet_uri))

    new_downloads.append(line)

new_downloads.append("\n")
with open(downloads_yaml, "w") as f:
    f.writelines(new_downloads)

print("\nMagnet links populated.")
