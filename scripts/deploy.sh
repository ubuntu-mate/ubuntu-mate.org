#!/usr/bin/env bash

scripts_path=$(dirname $0)

# Run any patches before deployment
$scripts_path/pre-deploy-patches.sh

# Upload to web server
nikola deploy

# Clear the CDN cache
echo "Clearing CDN cache..."
chmod +x $scripts_path/CDN_purge.sh
$scripts_path/CDN_purge.sh

