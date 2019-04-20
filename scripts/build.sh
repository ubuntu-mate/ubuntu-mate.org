#!/bin/bash

function abort_if_failed() {
    if [ $1 != 0 ]; then
        exit 1
    fi
}

# Ensure gems are up-to-date.
bundle install
abort_if_failed $?

# Generate any missing magnet URIs.
$(dirname "$0")/populate-magnet-links.py
abort_if_failed $?

# Generate locales
$(dirname "$0")/manage-translations.sh --build
abort_if_failed $?

# Build the site!
export JEKYLL_ENV=production
bundle exec jekyll build
abort_if_failed $?
