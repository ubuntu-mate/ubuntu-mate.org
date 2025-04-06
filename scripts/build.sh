#!/bin/bash
#
# Parameters:
#   --locales       Build localized pages
#
cd $(dirname "$0")/../

while [ $# -ne 0 ]
do
    arg="$1"
    case "$arg" in
        "--locales")
            generate_locales=true;;
        "--webp")
            generate_webp=true;;
    esac
    shift
done

function abort_if_failed() {
    if [ $1 != 0 ]; then
        exit 1
    fi
}

# Ensure gems are up-to-date.
echo -e "\nBuild Dependencies"
echo "------------------------------------------------------"
bundle check

if [ $? != 0 ]; then
    bundle install --jobs=4
    abort_if_failed $?
fi

# Build locales
if [ "$generate_locales" == "true" ]; then
    echo -e "\nBuild locales"
    echo "------------------------------------------------------"
    ./scripts/manage-translations.py --build
    abort_if_failed $?
fi

# Build the site
echo -e "\nJekyll Build"
echo "------------------------------------------------------"
export JEKYLL_ENV=production
bundle exec jekyll build
abort_if_failed $?

if [ ! -d _site ]; then
    exit 1
fi

# Generate WebP files
if [ "$generate_webp" == "true" ]; then
    echo -e "\nGenerate WebP Images"
    echo "------------------------------------------------------"
    ./scripts/helpers/generate-webp.sh
    abort_if_failed $?
fi

# Due to a RegexpError in jekyll-polyglot, the wildcard doesn't work in _config.yml.
# Externally delete source files not desired in the build output.
cd _site/
find . -name "*.xcf*" -delete

# WORKAROUND: Jekyll doesn't return exit code != 0 on a liquid exception, that
# may cause the build to be empty. Ensure the build fails if there are no HTML files.
html_count=$(find . -type f -name "*.html" | wc -l)
if [ "$html_count" == "0" ]; then
    exit 1
fi
