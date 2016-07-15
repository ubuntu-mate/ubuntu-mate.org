#!/usr/bin/env bash

sudo apt-get -y install \
    libpython3.5 \
    python3.5 \
    python3.5-dev \
    python3.5-minimal

sudo apt-get -y install \
    python-setuptools \
    python-pip

sudo apt-get -y install \
    liblcms2-dev \
    libfreetype6-dev \
    libjpeg8-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    libwebp-dev \
    libxslt1-dev \
    libxml2-dev \
    libyaml-dev \
    libzmq-dev \
    zlib1g-dev

sudo apt-get -y install \
    closure-compiler \
    jpegoptim \
    optipng \
    yui-compressor

pip install --upgrade "Nikola[extras,tests]==7.7.9"
