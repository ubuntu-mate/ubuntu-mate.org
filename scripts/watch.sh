#!/bin/bash

cd $(dirname "$0")/../

# Run build commands first
./scripts/build.sh $*

# Abort if it cannot be built.
if [ $? != 0 ]; then
    echo -e "\nThere was a problem running the build script."
    exit 1
fi

# Watch for changes during development
bundle exec jekyll serve --watch --livereload --drafts
