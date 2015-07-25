#!/usr/bin/env bash

if [ "$(basename ${0})" == "trusty.sh" ]; then
    MODE="trusty"
    PAGE="trusty"
    ANN_URL="\/blog\/ubuntu-mate-trusty-14.04.2-release\/"
    ANN_TITLE="Ubuntu MATE 14.04.2"
elif [ "$(basename ${0})" == "utopic.sh" ]; then
    MODE="utopic"
    PAGE="utopic"
    ANN_URL="\/blog\/ubuntu-mate-utopic-final-release\/"
    ANN_TITLE="Ubuntu MATE 14.10"
elif [ "$(basename ${0})" == "vivid.sh" ]; then
    MODE="vivid"
    PAGE="vivid"
    ANN_URL="\/blog\/ubuntu-mate-vivid-alpha2\/"
    ANN_TITLE="Ubuntu MATE 15.04"
elif [ "$(basename ${0})" == "pre-release.sh" ]; then
    MODE="pre-release"
    PAGE="${MODE}"
    ANN_URL="\/blog\/ubuntu-mate-vivid-alpha2\/"
    ANN_TITLE="Ubuntu MATE 15.04 Alpha2"
fi

function do_release() {
    local ARCH="${1}"
    local ISO_PATH=$(ls -1tr ${HOME}/ISO-Mirror/${MODE}/${ARCH}/*${ARCH}.iso | tail -n1)
    local ISO_FILE=$(basename ${ISO_PATH})
    local ISO_SIZE=$(du -m ${ISO_PATH} | cut -f1 -s)
    local MD5_PATH=$(ls -1tr ${HOME}/ISO-Mirror/${MODE}/${ARCH}/*${ARCH}.iso.md5 | tail -n1)
    local MD5_FILE=$(basename ${MD5_PATH})
    local MD5_HASH=$(cat ${MD5_PATH} | cut -f1 -d' ')
    local TOR_PATH=$(ls -1tr ${HOME}/ISO-Mirror/${MODE}/${ARCH}/*${ARCH}.iso.torrent | tail -n1)
    local TOR_FILE=$(basename ${TOR_PATH})

    if [ "${ARCH}" == "i386" ]; then
        sed -i "s/ISO_32_FILE/${ISO_FILE}/g" ${TARGET_PAGE}
        sed -i "s/ISO_32_MD5/${MD5_HASH}/g" ${TARGET_PAGE}
        sed -i "s/ISO_32_SIZE/${ISO_SIZE}/g" ${TARGET_PAGE}
        sed -i "s/TOR_32_FILE/${TOR_FILE}/g" ${TARGET_PAGE}
    elif [ "${ARCH}" == "amd64" ]; then
        sed -i "s/ISO_64_FILE/${ISO_FILE}/g" ${TARGET_PAGE}
        sed -i "s/ISO_64_MD5/${MD5_HASH}/g" ${TARGET_PAGE}
        sed -i "s/ISO_64_SIZE/${ISO_SIZE}/g" ${TARGET_PAGE}
        sed -i "s/TOR_64_FILE/${TOR_FILE}/g" ${TARGET_PAGE}
    elif [ "${ARCH}" == "amd64+mac" ]; then
        sed -i "s/ISO_MAC_FILE/${ISO_FILE}/g" ${TARGET_PAGE}
        sed -i "s/ISO_MAC_MD5/${MD5_HASH}/g" ${TARGET_PAGE}
        sed -i "s/ISO_MAC_SIZE/${ISO_SIZE}/g" ${TARGET_PAGE}
        sed -i "s/TOR_MAC_FILE/${TOR_FILE}/g" ${TARGET_PAGE}
    fi
    sed -i "s/ANN_URL/${ANN_URL}/g" ${TARGET_PAGE}
    sed -i "s/ANN_TITLE/${ANN_TITLE}/g" ${TARGET_PAGE}

    if [ "${MODE}" == "pre-release" ]; then
        local ANN_DIR=$(basename "${ANN_URL}" | sed -e s'/\\//g')
        zcat www/blog/"${ANN_DIR}"/index.html.gz > www/blog/"${ANN_DIR}"/index.html
    fi

    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${MD5_FILE}
    rm -f ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
    ln -s ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${ISO_FILE}
    ln -s ${MD5_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${MD5_FILE}
    ln -s ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/${TOR_FILE}
    if [ "${PAGE}" == "trusty" ]; then
        ln -s ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/longterm/${ISO_FILE}
        ln -s ${MD5_PATH} ${HOME}/Websites/ubuntu-mate.org/www/longterm/${MD5_FILE}
        ln -s ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/longterm/${TOR_FILE}
    elif [ "${PAGE}" == "utopic" ]; then
        ln -s ${ISO_PATH} ${HOME}/Websites/ubuntu-mate.org/www/download/${ISO_FILE}
        ln -s ${MD5_PATH} ${HOME}/Websites/ubuntu-mate.org/www/download/${MD5_FILE}
        ln -s ${TOR_PATH} ${HOME}/Websites/ubuntu-mate.org/www/download/${TOR_FILE}
    fi
}

TARGET_PAGE="${HOME}/Websites/ubuntu-mate.org/www/${PAGE}/index.html"
zcat ${TARGET_PAGE}.gz > ${TARGET_PAGE}
rm -f ${TARGET_PAGE}.gz
do_release i386
do_release amd64
if [ "${PAGE}" == "trusty" ]; then
    do_release amd64+mac
fi
gzip < ${TARGET_PAGE} > ${TARGET_PAGE}.gz
