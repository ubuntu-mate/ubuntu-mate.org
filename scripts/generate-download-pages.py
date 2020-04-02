#!/usr/bin/python3
#
# Programmatically generates the download pages for the website.
#
# Requires packages to run:
#   - python3-yaml
#
# [!] This must be run:
#       - After translations are generated.
#       - Before the Jekyll build.
#

import os
import subprocess
import requests
import shutil
import yaml

root_dir = os.path.join(os.path.dirname(__file__), "../")
output_dir = os.path.join(root_dir, "pages/autogen/")
downloads_yaml = os.path.join(root_dir, "_data/downloads.yml")

if not os.path.exists(downloads_yaml):
    print("Could not find file: downloads.yml")
    exit(1)

with open(downloads_yaml, "r") as f:
    try:
        downloads = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(str(e))

# Remove existing folder, if it exists.
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

os.mkdir(output_dir)

# Generate markdown pages for each available download
def write_md_file(filename, permalink, layout, step, download_id=None, release_id=None):
    output = "---"
    output += "\nlayout: " + layout
    output += "\npermalink: " + permalink
    output += "\nlang: en"
    output += "\nclass: download"
    output += "\nautogen: true"
    output += "\nstep: " + str(step)

    if download_id:
        output += "\ndownload_id: " + download_id

    if release_id:
        output += "\nrelease_id: " + release_id

    output += "\n---"

    with open(os.path.join(output_dir, filename), "w") as f:
        f.writelines(output)


for arch in downloads["downloads"]:
    print("Writing: " + arch + " => ", end="")

    for release in downloads["downloads"][arch]:
        download_id = arch
        release_id = release["release"]
        print(release_id, end=" ")

        # Step 2 - Choose Architecture
        write_md_file("{0}.md".format(arch), "/download/{0}/".format(arch), "download", 2, download_id, None)

        # Step 3 - Choose Download
        write_md_file("{0}-{1}.md".format(arch, release_id), "/download/{0}/{1}/".format(arch, release_id), "download", 3, download_id, release_id)

        # Step 4 - Post-download
        write_md_file("{0}-{1}-post.md".format(arch, release_id), "/download/{0}/{1}/thanks/".format(arch, release_id), "post-download", 3, download_id, release_id)

    print("")

print("\nDownload pages generated.")
