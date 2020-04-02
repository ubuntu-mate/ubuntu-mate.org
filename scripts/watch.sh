#!/bin/bash

# Run build commands first
$(dirname "$0")/build.sh $*

# Abort if it cannot be built.
if [ $? != 0 ]; then
    echo -e "\nThere was a problem running the build script."
    exit 1
fi

# Watch for changes during development
bundle exec jekyll serve --watch --livereload --drafts
