#!/usr/bin/env bash

function link_image() {
    local PAGE="${1}"
    local ISO_PATH="${2}"
    local ISO_FILE=$(basename ${ISO_PATH})
    local TOR_PATH="${ISO_PATH}.torrent"
    local TOR_FILE=$(basename ${TOR_PATH})

    mkdir -p ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
    ln -sf ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    ln -sf ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
}

link_image raspberry-pi "${HOME}/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz"
#link_image armhf-rootfs "${HOME}/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04-beta2-desktop-armhf-rootfs.tar.bz2"
#link_image raspberry-pi "${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10.1-desktop-armhf-raspberry-pi-2.img.xz"
link_image raspberry-pi "${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10.3-desktop-armhf-raspberry-pi-2.img.xz"
#link_image raspberry-pi "${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10-desktop-armhf-raspberry-pi-2.img.bz2"
#link_image raspberry-pi "${HOME}/ISO-Mirror/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2"
link_image armhf-rootfs "${HOME}/ISO-Mirror/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz"
