#!/usr/bin/env bash

zcat www/assets/js/tipuesearch.js.gz > www/assets/js/tipuesearch.js
rm -f www/assets/js/tipuesearch.js.gz
yui-compressor www/assets/js/tipuesearch.js -o www/assets/js/tipuesearch.js
gzip < www/assets/js/tipuesearch.js > www/assets/js/tipuesearch.js.gz
pngquant --speed 1 --force --output www/Ubuntu-MATE-Remix.png files/Ubuntu-MATE-Remix.png
pngquant --speed 1 --force --output www/Screenshot.png files/Screenshot.png
