#!/bin/bash
#
# Runs tests against the built version of the site.
#
# 'html-proofer' RubyGem provided by:
# https://github.com/gjtorikian/html-proofer
#
# This script contains two tests:
#
# <no parameters>   Check internal links, images and HTML output.
# --external        All of the above, plus external links.
#

if [ "$1" == "--external" ]; then
    # i18n pages are ignored as it will take much longer and duplicate URL checks.
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
else
    htmlproofer \
        --assume-extension \
        --check-html \
        --check-img-http \
        --empty_alt_ignore \
        --disable-external \
        ./_site
fi

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
