#!/bin/bash

current_dir=$PWD
script_dir=$(dirname "$BASH_SOURCE")
venv_path='./venv/bin/activate'

cd "$script_dir" || exit
source $venv_path

echo -e "\n\033[0;33m    Hello, $USER! \033[0m"
echo -e "\033[0;36m    Today is $(date) \033[0m"
echo -e "\033[0;32m    Successfully started the Python venv: $basename$(pwd) \033[0m\n"

cd $current_dir
