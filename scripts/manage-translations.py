#!/usr/bin/python3
#
# Run this script to generate PO/POT files from the original markdown files.
#
# This enables them to be translated via Transifex.
#
# Requires:
#   - txt2po (provided in 'translate-toolkit')
#   - po2txt (provided in 'translate-toolkit')
#

import argparse
import os
import glob
import shutil
import subprocess
import sys

def check_if_installed(cmd, package):
    if not shutil.which(cmd):
        print("Command for '{0}' missing. Please install '{1}'")
        exit(1)

check_if_installed("po2txt", "translate-toolkit")
check_if_installed("txt2po", "translate-toolkit")
check_if_installed("msgmerge", "translate-toolkit")

# Directories
os.chdir(os.path.join(os.path.dirname(__file__), "../"))
base_dir = os.path.join(os.path.dirname(__file__), "../")
page_dir = "pages"
post_dir = "_posts"
yaml_dir = "_data"
i18n_dir = "_i18n"
dest_dir = "pages/i18n"

# External helper scripts
yaml2po = os.path.join(base_dir, "scripts/helpers/yaml2po")
po2yaml = os.path.join(base_dir, "scripts/helpers/po2yaml")

# Gather file list
def read_file(path):
    with open(path, "r") as f:
        return "".join(f.readlines())

file_list = glob.glob(page_dir + "/*.md") + glob.glob(post_dir + "/*.md")
locale_list = read_file(os.path.join(i18n_dir, "locales.txt")).split("\n")

# Ensure locale has a folder
for locale in locale_list:
    src_locale = os.path.join(i18n_dir, locale)
    if not os.path.exists(src_locale):
        os.mkdir(src_locale)

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

if not os.path.exists(os.path.join(i18n_dir, "pots")):
    os.mkdir(os.path.join(i18n_dir, "pots"))

# Run commands
def run(command):
    try:
        proc = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("ERROR: Failed to run " + command)

# Operations for arguments
def generate():
    for locale in locale_list:
        if not locale:
            continue

        locale = locale.strip()
        print("-> " + locale)

        # For each markdown page, generate new POT and merge with existing.
        for path in file_list:
            page = path.replace(".md", "").split("/")[-1]
            print("  -> " + page)

            # TODO: Ignore programmatically generated pages (seems the case in subfolder?)

            # Update existing POT
            run("txt2po --pot {path} {i18n_dir}/pots/{page}.pot".format(path=path, page=page, i18n_dir=i18n_dir))

            # Update PO files if they already exist.
            if os.path.exists(os.path.join(i18n_dir, locale, page + ".po")):
                run("msgmerge {i18n_dir}/{locale}/{page}.po {i18n_dir}/pots/{page}.pot > new_po.tmp".format(i18n_dir=i18n_dir, locale=locale, page=page))
                os.rename("new_po.tmp", "{i18n_dir}/{locale}/{page}.po".format(i18n_dir=i18n_dir, locale=locale, page=page))
            else:
                run("txt2po {path} {i18n_dir}/{locale}/{page}.po".format(i18n_dir=i18n_dir, locale=locale, path=path, page=page))

        # Process strings.yml, used for strings in includes and layouts.
        run("{yaml2po} -P {yaml_dir}/strings.yml {i18n_dir}/pots/strings.pot".format(yaml2po=yaml2po, yaml_dir=yaml_dir, i18n_dir=i18n_dir))

        # Update strings.po if it already exists.
        if os.path.exists(os.path.join(i18n_dir, locale, "strings.po")):
            run("msgmerge {i18n_dir}/{locale}/strings.po {i18n_dir}/pots/strings.pot > new_po.tmp".format(i18n_dir=i18n_dir, locale=locale))
            os.rename("new_po.tmp", "{i18n_dir}/{locale}/strings.po".format(i18n_dir=i18n_dir, locale=locale))


def build():
    for locale in locale_list:
        if not locale:
            continue

        locale = locale.strip()
        print("-> " + locale)

        # Clear previously generated markdown files
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)

        os.mkdir(dest_dir)

        # Create new markdown files from translated PO files.
        for path in file_list:
            page = path.replace(".md", "").split("/")[-1]
            print("  -> " + page)

            src = os.path.join(i18n_dir, locale, page + ".po")
            dst = os.path.join(dest_dir, page + "." + locale + ".md")
            run("po2txt --template {path} {src} {dst}".format(path=path, src=src, dst=dst))

            # Ensure language code is definitely set.
            contents = ""
            with open(dst, "r") as f:
                contents = "".join(f.readlines())
            contents = contents.replace("lang: en", "lang: " + locale)
            with open(dst, "w") as f:
                f.writelines(contents)

        # Create new translated string.yml file.
        yaml_locale_dir = os.path.join(yaml_dir, locale)
        if not os.path.exists(yaml_locale_dir):
            os.mkdir(yaml_locale_dir)

        # Update an existing strings.po file if exists.
        yaml_src = os.path.join(i18n_dir, locale, "strings.po")
        yaml_dst = os.path.join(yaml_dir, locale, "strings.yml")
        if os.path.exists(yaml_src):
            run("{po2yaml} {yaml_src} {yaml_dst}".format(po2yaml=po2yaml,yaml_src=yaml_src, yaml_dst=yaml_dst))


# Process arguments
try:
    arg = sys.argv[1]
except Exception:
    print("Usage:")
    print("    manage-translations.sh [--generate] [--build]")

if arg == "--generate":
    generate()
elif arg == "--build":
    build()
else:
    print("Invalid parameter")
