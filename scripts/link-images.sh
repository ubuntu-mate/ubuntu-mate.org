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

    commands+=" && mkdir -p /home/matey/preview.ubuntu-mate.org/$PAGE"
    commands+=" && ln -vsf ${ISO_PATH} /home/matey/preview.ubuntu-mate.org/$PAGE/$ISO_FILE"
    commands+=" && ln -vsf ${TOR_PATH} /home/matey/preview.ubuntu-mate.org/$PAGE/$TOR_FILE"
}

link_image raspberry-pi "/home/matey/ISO-Mirror/bionic/arm64/ubuntu-mate-18.04.2-beta1-desktop-arm64+raspi3-ext4.img.xz"
link_image raspberry-pi "/home/matey/ISO-Mirror/bionic/armhf/ubuntu-mate-18.04.2-beta1-desktop-armhf+raspi-ext4.img.xz"
link_image raspberry-pi "/home/matey/ISO-Mirror/bionic/arm64/ubuntu-mate-18.04.2-beta2-desktop-arm64+raspi3-ext4.img.xz"
link_image raspberry-pi "/home/matey/ISO-Mirror/bionic/armhf/ubuntu-mate-18.04.2-beta2-desktop-armhf+raspi-ext4.img.xz"
link_image raspberry-pi "/home/matey/ISO-Mirror/xenial/armhf/ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz"

#link_image umpc "/home/matey/ISO-Mirror/bionic/amd64/ubuntu-mate-18.04.2-desktop-amd64-gpd-pocket.iso"
#link_image umpc "/home/matey/ISO-Mirror/bionic/amd64/ubuntu-mate-18.04.2-desktop-amd64-gpd-pocket2.iso"
#link_image umpc "/home/matey/ISO-Mirror/bionic/amd64/ubuntu-mate-18.04.2-desktop-amd64-topjoy-falcon.iso"
link_image umpc "/home/matey/ISO-Mirror/bionic/amd64/ubuntu-mate-18.04.3-desktop-amd64-gpd-pocket.iso"
link_image umpc "/home/matey/ISO-Mirror/bionic/amd64/ubuntu-mate-18.04.3-desktop-amd64-gpd-pocket2.iso"
link_image umpc "/home/matey/ISO-Mirror/bionic/amd64/ubuntu-mate-18.04.3-desktop-amd64-topjoy-falcon.iso"

link_image umpc "/home/matey/ISO-Mirror/disco/amd64/ubuntu-mate-19.04-desktop-amd64-gpd-pocket.iso"
link_image umpc "/home/matey/ISO-Mirror/disco/amd64/ubuntu-mate-19.04-desktop-amd64-gpd-pocket2.iso"
link_image umpc "/home/matey/ISO-Mirror/disco/amd64/ubuntu-mate-19.04-desktop-amd64-topjoy-falcon.iso"

#link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-alpha1-desktop-amd64-gpd-micropc.iso"
#link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-beta-desktop-amd64-gpd-micropc.iso"
link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-desktop-amd64-gpd-pocket.iso"
link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-desktop-amd64-gpd-pocket2.iso"
link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-desktop-amd64-gpd-micropc.iso"
link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-desktop-amd64-gpd-p2-max.iso"
link_image umpc "/home/matey/ISO-Mirror/eoan/amd64/ubuntu-mate-19.10-desktop-amd64-topjoy-falcon.iso"

echo "Symlinking images..."
for region in man yor; do
    ssh -o StrictHostKeyChecking=no matey@$region.ubuntu-mate.net "$commands"
done
