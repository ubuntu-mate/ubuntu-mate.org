#!/bin/bash

function abort_if_failed() {
    if [ $1 != 0 ]; then
        exit 1
    fi
}

# Ensure gems are up-to-date.
echo -e "\nbundle install"
echo "------------------------------------------------------"
bundle install
abort_if_failed $?

# Generate any missing magnet URIs.
echo -e "\nPopulate Magnet Links"
echo "------------------------------------------------------"
$(dirname "$0")/populate-magnet-links.py
abort_if_failed $?

# Generate locales
echo -e "\nBuild locales"
echo "------------------------------------------------------"
$(dirname "$0")/manage-translations.sh --build
abort_if_failed $?

# Build the site!
echo -e "\nJekyll Build"
echo "------------------------------------------------------"
export JEKYLL_ENV=production
bundle exec jekyll build
abort_if_failed $?
