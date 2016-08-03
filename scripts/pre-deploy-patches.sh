#!/bin/bash

# Add slogan to the browser's title.
echo "Patching... (Add slogan to home page)..."
old="<title>Ubuntu MATE"
new="<title>Ubuntu MATE | For a retrospective future"
file="$(dirname $0)/../output/index.html"
sed -i "s/$old/$new/g" "$file"
rm "$file.gz"
gzip "$file" -k

echo "Finished pre-deployment patches."
