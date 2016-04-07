#! /usr/bin/python3
#
#  Easy Configurable Download Page for ubuntu-mate.org
#
#  Licensed under Creative Commons Attribution-ShareAlike 4.0 International License
#  as with the rest of the website.
#
#  (C) 2016, Luke Horwell <lukehorwell37+code@gmail.com>
#

import os
import sys
import inspect
import json
import libtorrent   # Provided by package 'python3-libtorrent'
import wget         # Provided by package 'python3-wget'
import subprocess

# Paths from where this script is located
whereami = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
source_template_path    = whereami + "/../pages/templates/download.md"
target_destination_path = whereami + "/../pages/download.md"
downloads_json_path     = whereami + "/../downloads.json"
temp_files = []
had_a_fault = False

print('--------------------------------\nDownload Page Markdown Update\n--------------------------------')

# Useful functions used later in the script.
def download_file(url):
    url_name = url.split('/')[-1]
    print('\nDownloading file: ' + url_name)
    filename = wget.download(url)
    temp_files.append(filename)
    return filename

def clean_up_temp():
    global temp_files
    for name in temp_files:
        os.remove(name)

def get_download_size(url):
    url_name = url.split('/')[-1]
    print('Downloading metadata: ' + url_name)
    response = str(subprocess.Popen(['wget','--spider', url], stderr=subprocess.PIPE).communicate()[1])
    response.split('\n')
    size = int(response.split('Length: ')[1].split(' ')[0])
    size_MB = size / 1000 / 1000
    size_GB = size / 1000 / 1000 / 1000
    if size_GB < 1:
        return str(round(size_MB)) + ' MB'
    else:
        return str(round(size_GB,1)) + ' GB'

def generate_magnet_uri(url):
    # https://github.com/danfolkes/Magnet2Torrent/issues/6
    # http://stackoverflow.com/questions/12479570/given-a-torrent-file-how-do-i-generate-a-magnet-link-in-python

    session = libtorrent.session()
    filename = download_file(url)
    info = libtorrent.torrent_info(filename)
    return("magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name()))

def do_replace(this, that):
    global page_buffer
    page_buffer = page_buffer.replace(this, that)


################################################
# Read download information.
print('Reading downloads JSON...')
try:
    with open(downloads_json_path) as data_file:
        downloads = json.load(data_file)
except e as Exception:
    print('\nERROR: Invalid JSON!\n' + e + '\n')
    exit()

print('Reading downloads template...')
f = open(source_template_path, 'r+')
page_buffer = f.read()

################################################

print('Manipulating contents...')

for release_id in downloads['release'].keys():

    version = 'version-' + release_id

    if not downloads['release'][release_id]['visible']:
        do_replace('href="#' + version + '"', 'style="display:none"')
        continue

    distro_codename = downloads['release'][release_id]['codename']
    distro_version = downloads['release'][release_id]['version']
    distro_state = downloads['release'][release_id]['state']
    distro_type = downloads['release'][release_id]['type']

    print('\n-------- ' + distro_version + ' --------')

    # Release Name
    # --- version-[X]-FRIENDLY-NAME
    do_replace(version + '-FRIENDLY-NAME', downloads['release'][release_id]['name'])

    # Release Notes URL
    # --- version-[X]-RELEASE-URL
    do_replace(version + '-RELEASE-URL', downloads['release'][release_id]['release-notes'])

    # Torrent URL
    # --- version-[X]-TORRENT-URL-[arch]
    for arch in downloads['release'][release_id]['arch']:
        if arch == 'armhf':
            url = downloads['release'][release_id]['rpi-mirrors']['torrent']
            do_replace(version + '-TORRENT-URL-' + arch, url)
        else:
            url = downloads['global']['canonical-torrent'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
            do_replace(version + '-TORRENT-URL-' + arch, url)

        # Link text for torrent
        # --- version-[X]-TORRENT-NAME-[arch]
        url_file = url.split('/')[-1]
        do_replace(version + '-TORRENT-NAME-' + arch, url_file)

        # Magnet URI for torrent
        # --- version-[X]-MAGNET-URI-[arch]
        try:
            magnet_uri = generate_magnet_uri(url)
            do_replace(version + '-MAGNET-URI-' + arch, magnet_uri)
        except Exception as e:
            print(' *** ERROR: Exception: ' + str(e))
            had_a_fault = True
            do_replace(version + '-MAGNET-URI-' + arch, "404")

    # Direct URL
    # --- version-[X]-DIRECT-URL-[arch]
    # --- version-[X]-DIRECT-URL-[arch]-[server]  (for Raspberry Pi downloads)
    #
    # Link text for direct download
    # --- version-[X]-DIRECT-NAME-[arch]
    # --- version-[X]-DIRECT-NAME-[arch]-[server]  (for Raspberry Pi downloads)
    for arch in downloads['release'][release_id]['arch']:
        if arch == 'armhf':
            for server in downloads['global']['rpi_servers']:  # eu, ca, fr...
                url = downloads['release'][release_id]['rpi-mirrors'][server]
                do_replace(version + '-DIRECT-URL-' + arch + '-' + server, url)
                url_file = url.split('/')[-1]
                do_replace(version + '-DIRECT-NAME-' + arch + '-' + server, '<b>' + downloads['global'][server] + '</b> - ' + url_file )
            size = get_download_size(url)
            do_replace(version + '-SIZE-' + arch, size)

        else:
            url = downloads['global']['canonical-iso'].replace('OSVERSION', distro_version).replace('ARCH', arch).replace('STATE', distro_state).replace('TYPE', distro_type)
            url_file = url.split('/')[-1]
            do_replace(version + '-DIRECT-URL-' + arch, url)
            do_replace(version + '-DIRECT-NAME-' + arch, url_file)
            size = get_download_size(url)
            do_replace(version + '-SIZE-' + arch, size)

    # SHA256 Checksum for ISO
    # --- version-[X]-SHA256-[arch]
    for arch in downloads['release'][release_id]['arch']:
        sha256sum = downloads['release'][release_id]['sha256sum'][arch]
        do_replace(version + '-SHA256-' + arch, sha256sum)

    # Show alert box about LTS status
    # "LTS-CODENAMES" => Replace with version that is an LTS. Only one currently supported to be at the moment.
    # //version-[X]-show-LTS    => Code inject, to show #LTS using jQuery.
    # LTS_END_DATE               => Replaced with LTS Date.
    if downloads['release'][release_id]['lts']:
        do_replace('LTS-CODENAMES', version)
        do_replace('LTS_END_DATE', downloads['release'][release_id]['lts-end-date'])
        do_replace('//' + version + '-show-LTS', "$('#LTS').show();")

    # Show a danger alert for specific versions, if applicable.
    # E.g. serve bug, inform of experimental, or reaching end of life.
    if downloads['release'][release_id]['show-warning']:
        classes = "alert alert-danger"
        do_replace('id="' + version + '-WARNING" hidden', 'class="' + version + ' ' + classes + '"')
        do_replace(version + '-WARNING-HEADER', downloads['release'][release_id]['warning-header'])
        do_replace(version + '-WARNING-TEXT', downloads['release'][release_id]['warning-text'])

    # Other Downloads Page
    # --- version-[X]-OTHER
    url = downloads['global']['canonical-other-folder'].replace('OSVERSION', distro_version).replace('STATE', distro_state).replace('TYPE', distro_type)
    do_replace(version + '-OTHER', url)

    # Now actually replace version ID with release's codename.
    do_replace(version, distro_codename)

################################################

print('Writing new file...')
os.remove(target_destination_path)
file = open(target_destination_path, "w")
for line in page_buffer.split('\n'):
    file.write(line + '\n')
file.close()

if had_a_fault:
    print('\n*******************************')
    print('Some problems occurred while running the script.')
    print('The page may have broken links for visitors.')
    print('*******************************\n')

clean_up_temp()
print('Finished running download page script.')
exit()
