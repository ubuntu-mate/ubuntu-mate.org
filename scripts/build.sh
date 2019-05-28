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
echo -e "\nGenerate Magnet Links"
echo "------------------------------------------------------"
$(dirname "$0")/generate-magnet-links.py
abort_if_failed $?

# Generate markdown files for downloads
echo -e "\nGenerate Download Pages"
echo "------------------------------------------------------"
$(dirname "$0")/generate-download-pages.py
abort_if_failed $?

# Generate locales
echo -e "\nGenerate locales"
echo "------------------------------------------------------"
$(dirname "$0")/manage-translations.py --generate
abort_if_failed $?

# Build locales
echo -e "\nBuild locales"
echo "------------------------------------------------------"
$(dirname "$0")/manage-translations.py --build
abort_if_failed $?

# Build the site!
echo -e "\nJekyll Build"
echo "------------------------------------------------------"
if [ ! -d _site/ ]; then
    mkdir _site
fi

export JEKYLL_ENV=production
bundle exec jekyll build
abort_if_failed $?

# Due to a RegexpError in jekyll-polyglot, the wildcard doesn't work in _config.yml.
# Externally delete source files not desired in the build output.
if [ -f _site ]; then
    cd _site/
    find . -name "*.xcf" -delete
fi
