#!/bin/bash
#
# @file {{ cookiecutter.project }}
# @brief {{ cookiecutter.description }}

# Indicates if upgrade the system or not. Defaults to *false*.
UPGRADE=false

# @description Get bash parameters.
#
# Accepts:
#
#  - *h* (help).
#
# @arg '$@' string Bash arguments.
#
# @exitcode 0 if successful.
# @exitcode 1 on failure.
function get_parameters() {
    # Obtain parameters.
    while getopts 'h;' opt; do
        OPTARG=$(sanitize "$OPTARG")
        case "$opt" in
            h) help && exit 0;;
        esac
    done
    return 0
}

# @description Shows help message.
#
# @noargs
#
# @exitcode 0 if successful.
# @exitcode 1 on failure.
function help() {
    echo '{{ cookiecutter.description }}'
    echo 'Parameters:'
    echo '-h (help): Show this help message.'
    echo 'Example:'
    echo "./{{ cookiecutter.project }}.sh -h"
    return 0
}

# @description {{ cookiecutter.description }}
#
# @arg $@ string Bash arguments.
#
# @exitcode 0 if successful.
# @exitcode 1 on failure.
function main() {

    get_parameters "$@"

    return 0
}

# @description Sanitize input.
#
# The applied operations are:
#
# - Trim.
#
# @arg $1 string Text to sanitize.
#
# @exitcode 0 if successful.
# @exitcode 1 on failure.
#
# @stdout Sanitized input.
function sanitize() {
    [[ -z $1 ]] && echo '' && return 0
    local sanitized="$1"
    # Trim.
    sanitized="${sanitized## }"
    sanitized="${sanitized%% }"
    echo "$sanitized"
    return 0
}

# Avoid running the main function if we are sourcing this file.
return 0 2>/dev/null
main "$@"
