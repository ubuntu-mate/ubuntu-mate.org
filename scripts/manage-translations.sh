#!/bin/bash
#
# Run this script to generate PO/POT files from the original markdown files.
#
# This enables them to be translated via Transifex.
#
# Requires:
#   - txt2po (provided in 'translate-toolkit')
#   - po2txt (provided in 'translate-toolkit')
#

function check_if_installed() {
    if [ $(which $1) == "" ]; then
        "$1 missing. Please install '$2'."
        exit 1
    fi
}

check_if_installed "po2txt" "translate-toolkit"
check_if_installed "txt2po" "translate-toolkit"
check_if_installed "msgmerge" "translate-toolkit"

# Set up variables
base_dir="$(dirname "$0")"
base_dir=$(realpath "$base_dir/../")
source_dir="$base_dir/pages/"
i18n_dir="$base_dir/_i18n/"
dest_dir="$base_dir/i18n/"
yaml_dir="$base_dir/_data/"

yaml2po="$base_dir/scripts/helpers/yaml2po"
po2yaml="$base_dir/scripts/helpers/po2yaml"

cd "$source_dir"
file_list=$(find . -name "*.md")
locale_list=$(cat $i18n_dir/locales.txt)

# Ensure locale has a folder
for locale in $locale_list; do
    if [ ! -d "$i18n_dir/$locale" ]; then
        mkdir "$i18n_dir/$locale"
    fi
done

if [ ! -d "$dest_dir" ]; then
    mkdir "$dest_dir"
fi

case "$1" in

################################################################################
# Create POT files for all pages
"--generate")
    for locale in $locale_list; do
        if [ "$locale" == "" ]; then
            continue
        fi

        # For each markdown page, generate new POT and merge with existing.
        for page in $file_list; do
            page="${page%.*}"
            echo "-> $page ($locale)"
            txt2po --pot "$page.md" "$i18n_dir/pots/$page.pot"

            # Update PO files if they already exist.
            if [ -f "$i18n_dir/$locale/$page.po" ]; then
                # Update existing PO with new POT
                msgmerge "$i18n_dir/$locale/$page.po" "$i18n_dir/pots/$page.pot" > new_po.tmp
                mv new_po.tmp "$i18n_dir/$locale/$page.po"
            else
                # Create new PO
                txt2po "$page.md" "$i18n_dir/$locale/$page.po"
            fi
        done

        # Process strings.yml, used for strings in includes and layouts.
        $yaml2po -P "$yaml_dir/strings.yml" "$i18n_dir/pots/strings.pot"

        # Update strings.po if it already exists.
        if [ -f "$i18n_dir/$locale/strings.po" ]; then
            msgmerge "$i18n_dir/$locale/strings.po" "$i18n_dir/pots/strings.pot" > new_po.tmp
            mv new_po.tmp "$i18n_dir/$locale/strings.po"
        fi

    done;;

################################################################################
# Create new files from translated files.
"--build")
    for locale in $locale_list; do
        if [ "$locale" == "" ]; then
            continue
        fi

        # Create new markdown files from translated PO files.
        for page in $file_list; do
            page="${page%.*}"
            echo "-> $page ($locale)"
            po2txt --template "$page.md" "$i18n_dir/$locale/$page.po" "$dest_dir/$page.$locale.md"
            sed -i "s/lang: en/lang: $locale/g" "$dest_dir/$page.$locale.md"
        done

        # Create new translated string.yml file.
        if [ ! -d "$yaml_dir/$locale/" ]; then
            mkdir "$yaml_dir/$locale/"
        fi

        if [ -f "$i18n_dir/$locale/strings.po" ]; then
            $po2yaml "$i18n_dir/$locale/strings.po" "$yaml_dir/$locale/strings.yml"
        fi
    done;;

*)
    echo "Usage:"
    echo "    manage-translations.sh [--generate] [--build]"
    exit 1;;

esac
