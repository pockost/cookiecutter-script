#!/usr/bin/env bats
#
# {{ cookiecutter.project }} tests, from root folder run: bats tests.

setup() {
    source {{ cookiecutter.project }}.sh
    touch /tmp/empty_file
}

teardown() {
    rm /tmp/empty_file
}

@test 'Show help with help function.' {
    [[ "$(help)" == *'help'* ]]
}
