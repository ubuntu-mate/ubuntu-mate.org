#!/bin/bash

echo "Setting permissions..."
find _site/ -type d -exec chmod 755 {} \;
find _site/ -type f -exec chmod 644 {} \;

echo "Syncing to server..."
rsync -a -e "ssh -o StrictHostKeyChecking=no" --delete _site/ matey@man.ubuntu-mate.net:ubuntu-mate.org/
rsync -a -e "ssh -o StrictHostKeyChecking=no" --delete _site/ matey@yor.ubuntu-mate.net:ubuntu-mate.org/

echo "Creating links for downloadable images..."
scripts/link-images.sh

echo "Clearing CDN cache..."
ssh -o StrictHostKeyChecking=no matey@yor.ubuntu-mate.net /home/matey/post-deploy-actions.sh "ubuntu-mate.org"
