#!/bin/bash

scripts/link-images.sh

echo "Setting permissions..."
find _site/ -type d -exec chmod 755 {} \;
find _site/ -type f -exec chmod 644 {} \;

echo "Syncing to server..."
rsync -a -e "ssh -o StrictHostKeyChecking=no" --delete _site/ matey@man.ubuntu-mate.net:preview.ubuntu-mate.org/
rsync -a -e "ssh -o StrictHostKeyChecking=no" --delete _site/ matey@yor.ubuntu-mate.net:preview.ubuntu-mate.org/

echo "Clearing CDN cache..."
chmod +x scripts/.CDN_purge.sh
scripts/.CDN_purge.sh
