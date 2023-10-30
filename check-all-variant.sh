#!/bin/bash

# #####
# Build cookie template variants to check for quality.
#
# This can be taken as a 'Tox' alike and hardcoded in a bash script.
#
# Not all possible variants will be built and checked since something like frontend
# should not have any impact on backend, so it can only be check twice (disable and
# enabled).
# #####

# To enable for debugging purpose
# set -x
# Any signal error from commands will stop further command execution
set -eo pipefail

# Useful variables
BUCKET="variants-envs"
VENV_PATH=".venv"
COOKIECUTTER_BIN="$VENV_PATH/bin/cookiecutter"

FORMATBGBLUE=$(tput setab 4)
FORMATFGBOLD=$(tput bold)
FORMATRESET=$(tput sgr0)

# Reboot bucket directory
rm -Rf $BUCKET
mkdir -p $BUCKET

# Function to generate project, install it and run quality task
# Arguments:
#     $1: Project name
#     $2: Package name
#     $3: Application name
#     $4: Project description
#     $5: Option include_api
#     $6: Option include_cmsplugin
#     $7: Option include_frontend
#     $8: Option init_git_repository
build_and_install_variant () {
    echo ""
    echo -e "$(printf "%s%s ------------------------------------------------------------------------------ %s" "$FORMATBGBLUE" "$FORMATFGBOLD" "$FORMATRESET")"
    echo -e "$(printf "%s%s ------> 👷 BUILDING %s %s 👷 <------ %s" "$FORMATBGBLUE" "$FORMATFGBOLD" "$1" "$4" "$FORMATRESET")"
    echo -e "$(printf "%s%s ------------------------------------------------------------------------------ %s" "$FORMATBGBLUE" "$FORMATFGBOLD" "$FORMATRESET")"
    echo ""
    $COOKIECUTTER_BIN -o "$BUCKET" --no-input . project_name="$1" package_name="$2" app_name="$3" project_short_description="$4" include_api="$5" include_cmsplugin="$6" include_frontend="$7" init_git_repository="$8"

    # Show generated project configuration
    echo ""
    cd "$BUCKET"/"$2"
    echo "📝 Baked configuration"
    echo ""
    cat cookiebaked.json
    echo ""

    # Run project install and quality
    echo ""
    echo "🚀🚀🚀🚀🚀 Install and quality 🚀🚀🚀🚀🚀"
    make install migrations quality
    echo ""

    # Go back to the bucket top since we entered into the project
    echo ""
    cd ../../
}


# Generate project variant without any feature option
VARIANT_NAME='Variant 0'
VARIANT_DESCRIPTION='(✖️API; ✖️Plugin; ✖️Frontend; ✖️Git)'
VARIANT_PKG='variant-0'
VARIANT_APP='variant_0'
build_and_install_variant "$VARIANT_NAME" "$VARIANT_PKG" "$VARIANT_APP" "$VARIANT_DESCRIPTION" "" "" "" "";


# Generate project variant with API
VARIANT_NAME='Variant 1'
VARIANT_DESCRIPTION='(✔️API; ✖️Plugin; ✖️Frontend; ✖️Git)'
VARIANT_PKG='variant-1'
VARIANT_APP='variant_1'
build_and_install_variant "$VARIANT_NAME" "$VARIANT_PKG" "$VARIANT_APP" "$VARIANT_DESCRIPTION" "true" "" "" "";


# Generate project variant with API and CMS plugin
VARIANT_NAME='Variant 2'
VARIANT_DESCRIPTION='(✔️API; ✔️Plugin; ✖️Frontend; ✖️Git)'
VARIANT_PKG='variant-2'
VARIANT_APP='variant_2'
build_and_install_variant "$VARIANT_NAME" "$VARIANT_PKG" "$VARIANT_APP" "$VARIANT_DESCRIPTION" "true" "true" "" "";


# Generate project variant with CMS plugin and frontend
VARIANT_NAME='Variant 3'
VARIANT_DESCRIPTION='(✖️API; ✔️Plugin; ✖️Frontend; ✖️Git)'
VARIANT_PKG='variant-3'
VARIANT_APP='variant_3'
build_and_install_variant "$VARIANT_NAME" "$VARIANT_PKG" "$VARIANT_APP" "$VARIANT_DESCRIPTION" "" "true" "" "";


# Generate project variant with all option enabled
VARIANT_NAME='Variant 9'
VARIANT_DESCRIPTION='(✔️API; ✔️Plugin; ✔️Frontend; ✔️Git)'
VARIANT_PKG='variant-9'
VARIANT_APP='variant_9'
build_and_install_variant "$VARIANT_NAME" "$VARIANT_PKG" "$VARIANT_APP" "$VARIANT_DESCRIPTION" "true" "true" "true" "true";
