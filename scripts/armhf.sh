#!/usr/bin/env bash

function do_rpi2() {
    local PAGE="raspberry-pi"
    local ISO_PATH="${HOME}/ISO-Mirror/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-raspberry-pi-2.img.bz2"
    local ISO_FILE=$(basename ${ISO_PATH})
    local ISO_SIZE=$(du -m ${ISO_PATH} | cut -f1 -s)
    local TOR_PATH="${ISO_PATH}.torrent"
    local TOR_FILE=$(basename ${TOR_PATH})

    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
    ln -s ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    ln -s ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
}

function do_rpi2_rc() {
    local PAGE="raspberry-pi"
    local ISO_PATH="${HOME}/ISO-Mirror/wily/armhf/ubuntu-mate-15.10-rc-desktop-armhf-raspberry-pi-2.img.bz2"
    local ISO_FILE=$(basename ${ISO_PATH})
    local ISO_SIZE=$(du -m ${ISO_PATH} | cut -f1 -s)
    local TOR_PATH="${ISO_PATH}.torrent"
    local TOR_FILE=$(basename ${TOR_PATH})

    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
    ln -s ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    ln -s ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
}

function do_rootfs() {
    local PAGE="armhf-rootfs"
    local ISO_PATH="${HOME}/ISO-Mirror/vivid/armhf/ubuntu-mate-15.04-desktop-armhf-rootfs.tar.gz"
    local ISO_FILE=$(basename ${ISO_PATH})
    local ISO_SIZE=$(du -m ${ISO_PATH} | cut -f1 -s)
    local TOR_PATH=""
    local TOR_PATH="${ISO_PATH}.torrent"
    local TOR_FILE=$(basename ${TOR_PATH})

    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
    ln -s ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    ln -s ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
}

do_rpi2
do_rpi2_rc
do_rootfs
