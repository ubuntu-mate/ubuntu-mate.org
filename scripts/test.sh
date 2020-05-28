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

cd "$(dirname $0)/../"

# CI only: htmlproofer is installed in vendor folder
if [ -d "vendor/" ]; then
    htmlproofer="bundle exec htmlproofer"
else
    htmlproofer="htmlproofer"
fi

function check_for_error() {
    if [ $1 != 0 ]; then
        exit 1
    fi
}

if [ "$1" == "--external" ]; then
    # i18n pages are ignored as it will take much longer and duplicate URL checks.
    ignore_list=""
    for lang in $(cat _i18n/locales.txt); do
        ignore_list+="/_site/$lang/,"
    done
    ignore_list+="/_site/en/"

    echo "Proofing HTML (and external links)..."
    $htmlproofer \
        --assume-extension \
        --check-html \
        --check-img-http \
        --empty_alt_ignore \
        --url-ignore "/ubuntu-mate.community/" \
        --http-status-ignore "301,302,429" \
        --file-ignore "$ignore_list" \
        ./_site
else
    echo "Proofing HTML..."
    $htmlproofer \
        --assume-extension \
        --check-html \
        --check-img-http \
        --empty_alt_ignore \
        --disable-external \
        ./_site
fi
check_for_error $?

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

# Markdown frontmatter consistency check
./scripts/helpers/validate-frontmatter.py
check_for_error $?
