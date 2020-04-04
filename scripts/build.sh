#!/bin/bash
#
# Parameters:
#   --magnet-uri    Fetch torrent files and generate magnet URIs.
#   --locales       Build localized pages
#
while [ $# -ne 0 ]
do
    arg="$1"
    case "$arg" in
        "--magnet-uri")
            generate_magnet_uri=true;;
        "--locales")
            generate_locales=true;;
    esac
    shift
done

function abort_if_failed() {
    if [ $1 != 0 ]; then
        exit 1
    fi
}

# Ensure gems are up-to-date.
echo -e "\nbundle install"
echo "------------------------------------------------------"
bundle install --jobs=4
abort_if_failed $?

# Generate any missing magnet URIs.
if [ "$generate_magnet_uri" == "true" ]; then
    echo -e "\nGenerate Magnet Links"
    echo "------------------------------------------------------"
    $(dirname "$0")/generate-magnet-links.py
    abort_if_failed $?
fi

# Generate markdown files for downloads
echo -e "\nGenerate Download Pages"
echo "------------------------------------------------------"
$(dirname "$0")/generate-download-pages.py
abort_if_failed $?

# Generate locales
if [ "$generate_locales" == "true" ]; then
    echo -e "\nGenerate locales"
    echo "------------------------------------------------------"
    $(dirname "$0")/manage-translations.py --generate
    abort_if_failed $?
fi

# Build locales
if [ "$generate_locales" == "true" ]; then
    echo -e "\nBuild locales"
    echo "------------------------------------------------------"
    $(dirname "$0")/manage-translations.py --build
    abort_if_failed $?
fi

# Build the site
echo -e "\nJekyll Build"
echo "------------------------------------------------------"
if [ ! -d _site/ ]; then
    mkdir _site
fi

export JEKYLL_ENV=production
bundle exec jekyll build
abort_if_failed $?

if [ ! -d _site ]; then
    exit 1
fi

# Due to a RegexpError in jekyll-polyglot, the wildcard doesn't work in _config.yml.
# Externally delete source files not desired in the build output.
cd _site/
find . -name "*.xcf" -delete

# WORKAROUND: Jekyll doesn't return exit code != 0 on a liquid exception, that
# may cause the build to be empty. Ensure the build fails if there are no HTML files.
html_count=$(find . -type f -name "*.html" | wc -l)
if [ "$html_count" == "0" ]; then
    exit 1
fi
