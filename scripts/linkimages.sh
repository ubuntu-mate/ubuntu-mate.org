#!/usr/bin/env bash
#
# Creates symlinks on the server linking to the actual files.
# Commands are loaded up then executed in all in one go for each region server.
#

commands="echo OK"

function link_image() {
    local PAGE="${1}"
    local ISO_PATH="${2}"
    local ISO_FILE=$(basename ${ISO_PATH})
    local TOR_PATH="${ISO_PATH}.torrent"
    local TOR_FILE=$(basename ${TOR_PATH})

    commands+=" && mkdir -p /home/matey/ubuntu-mate.org/$PAGE"
    commands+=" && ln -vsf ${ISO_PATH} /home/matey/ubuntu-mate.org/$PAGE/$ISO_FILE"
    commands+=" && ln -vsf ${TOR_PATH} /home/matey/ubuntu-mate.org/$PAGE/$TOR_FILE"
}

link_image gpd-pocket "/home/matey/ISO-Mirror/cosmic/amd64/ubuntu-mate-18.10-desktop-amd64-gpd-pocket.iso"
link_image raspberry-pi "/home/matey/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img.xz"
link_image raspberry-pi "/home/matey/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz"
link_image trusty "/home/matey/ISO-Mirror/trusty/i386/ubuntu-mate-14.04.2-LTS-desktop-i386.iso"
link_image trusty "/home/matey/ISO-Mirror/trusty/amd64/ubuntu-mate-14.04.2-LTS-desktop-amd64.iso"
link_image trusty "/home/matey/ISO-Mirror/trusty/amd64+mac/ubuntu-mate-14.04.2-LTS-desktop-amd64+mac.iso"
#link_image armhf-rootfs "${HOME}/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04-beta2-desktop-armhf-rootfs.tar.bz2"

echo "Symlinking images..."
for region in "man" "yor"; do
    ssh -o StrictHostKeyChecking=no matey@$region.ubuntu-mate.net "$commands"
done
