#!/bin/bash
#
# Runs tests against the built version of the site.
#
# 'html-proofer' RubyGem provided by:
# https://github.com/gjtorikian/html-proofer
#
# Optionally, run this script with '--external' to check external (remote) links.
#

cd "$(dirname $0)/../"

if [ "$(bundle exec htmlproofer --version)" == "" ]; then
    echo "htmlproofer is not installed. Run 'bundle install' or 'gem install html-proofer."
    exit 1
fi

function check_for_error() {
    if [ $1 != 0 ]; then
        exit 1
    fi
}


# External URL checks optional
external_check=""
ignore_list=""

if [ ! "$1" == "--external" ]; then
    external_check="--disable-external"
else
    external_check="--log-level :debug"

    # Ignore i18n pages
    ignore_list="/_site/en/,"
    for lang in $(cat _i18n/locales.txt); do
        ignore_list+="/_site/$lang/,"
    done
fi

echo "Proofing HTML..."
bundle exec htmlproofer \
    --ignore-files "$ignore_list" \
    --no-enforce-https \
    --allow-missing-href \
    --ignore-empty-alt \
    --ignore-missing-alt \
    $external_check \
    --only-4xx \
    ./_site
check_for_error $?

# Usage:
#   --no-enforce-https      cdimage.ubuntu.com is only HTTP.

# Markdown frontmatter consistency check
./scripts/helpers/validate-frontmatter.py
check_for_error $?
