#!/bin/bash
#
# Generates WebP files alongside JPEG and PNG images.
#
QUALITY=75

# Requires 'webp' (Ubuntu) or 'libwebp' (Arch & others) to be installed
if [ -z "$(which cwebp)" ]; then
    echo "Command for 'cwebp' missing!"
    exit 1
fi

# Begin conversion
cd "$(dirname "$0")/../../_site/images/"

function convert_to_webp() {
    input="$1"
    output="${1%.*}.webp"
    echo "-> $input"
    cwebp -quiet -q $QUALITY "$input" -o "$output" &
}

# -- PNG
for path in $(find . -name "*.png"); do
    convert_to_webp "$path"
done

# -- JPG
for path in $(find . -name "*.jpg"); do
    convert_to_webp "$path"
done

# Run concurrently in the background to speed things up
wait
