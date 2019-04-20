#!/bin/bash

# Run build commands first
$(dirname "$0")/build.sh

# Watch for changes during development
bundle exec jekyll serve --watch --livereload --drafts

