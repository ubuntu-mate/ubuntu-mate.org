#!/bin/bash
#
# Runs tests against the built version of the site.
#

htmlproofer \
    --assume-extension \
    --check-html \
    --check-img-http \
    --only-4xx \
    ./_site

# Excluded checks:
#   --check-favicon         5xx errors are for web server software.
#                           No file would be present.
#   --enforce-https         cdimage.ubuntu.com is only HTTP.

if [ $? != 0 ]; then
    exit 1
fi
