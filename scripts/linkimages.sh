#!/usr/bin/env bash

function link_image() {
    local PAGE="${1}"
    local ISO_PATH="${2}"
    local ISO_FILE=$(basename ${ISO_PATH})
    local TOR_PATH="${ISO_PATH}.torrent"
    local TOR_FILE=$(basename ${TOR_PATH})

    mkdir -p www/${PAGE}
    echo "Symlinking www/${PAGE}/${ISO_FILE}..."
    sudo ln -vsf ${ISO_PATH} www/${PAGE}/${ISO_FILE} || :

    echo "Symlinking www/${PAGE}/${TOR_FILE}..."
    sudo ln -vsf ${TOR_PATH} www/${PAGE}/${TOR_FILE} || :
}

link_image raspberry-pi "/home/matey/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz"
link_image raspberry-pi "/home/matey/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz"
link_image trusty "/home/matey/ISO-Mirror/trusty/i386/ubuntu-mate-14.04.2-LTS-desktop-i386.iso"
link_image trusty "/home/matey/ISO-Mirror/trusty/amd64/ubuntu-mate-14.04.2-LTS-desktop-amd64.iso"
link_image trusty "/home/matey/ISO-Mirror/trusty/amd64+mac/ubuntu-mate-14.04.2-LTS-desktop-amd64+mac.iso"
#link_image armhf-rootfs "${HOME}/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04-beta2-desktop-armhf-rootfs.tar.bz2"
#link_image raspberry-pi "${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10.1-desktop-armhf-raspberry-pi-2.img.xz"
#link_image raspberry-pi "${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz"
#link_image raspberry-pi "${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10-desktop-armhf-raspberry-pi-2.img.bz2"
#link_image raspberry-pi "${HOME}/ISO-Mirror/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2"
#link_image armhf-rootfs "${HOME}/ISO-Mirror/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz"
