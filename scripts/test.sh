#!/bin/bash
#
# Runs tests against the built version of the site.
#

htmlproofer \
    --assume-extension \
    --check-html \
    --check-img-http \
    --empty_alt_ignore \
    ./_site

# Included checks:
#   --empty_alt_ignore      Mainly icons in layout/includes. More work needed
#                           to catch every single alt tag.
#
# Excluded checks:
#   --check-favicon         5xx errors are for web server software.
#                           No file would be present.
#   --enforce-https         cdimage.ubuntu.com is only HTTP.

if [ $? != 0 ]; then
    exit 1
fi
