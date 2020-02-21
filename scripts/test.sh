#!/bin/bash
#
# Runs tests against the built version of the site.
#
# 'html-proofer' RubyGem provided by:
# https://github.com/gjtorikian/html-proofer
#

# i18n pages are ignored as it will take much longer and duplicate results
# (e.g. external checks)
ignore_list=""
for lang in $(cat _i18n/locales.txt); do
    ignore_list+="/_site/$lang/,"
done
ignore_list+="/_site/en/"

htmlproofer \
    --assume-extension \
    --check-html \
    --check-img-http \
    --empty_alt_ignore \
    --url-ignore "/ubuntu-mate.community/" \
    --http-status-ignore "301,302,429" \
    --file-ignore "$ignore_list" \
    ./_site

#
# Included checks:
# ============================================================================
#   --empty_alt_ignore      Mainly icons in layout/includes. More work needed
#                           to catch every single alt tag.
#   --internal_domains      Ubuntu MATE Community will rate limit requests.
#
# Excluded checks:
# ============================================================================
#   --check-favicon         5xx errors are for web server software.
#                           No file would be present.
#   --enforce-https         cdimage.ubuntu.com is only HTTP.
#

if [ $? != 0 ]; then
    exit 1
fi
