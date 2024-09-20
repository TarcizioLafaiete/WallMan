#!bin/bash

debug=1

if [ $debug -eq 1 ]; then
    USER_HOME=$(pwd)
else 
    USER_HOME="$HOME/.WallMan"
fi

export WALLMAN_ROOT="$USER_HOME"
export UNIX_SOCKET_FILE="/tmp/socket_file"
export SETTINGS_JSON="$USER_HOME/settings.json"
export CURRENT_SETTINGS_JSON="$USER_HOME/currentSettings.json"
export RESOURCES_DIR="$USER_HOME/manager/view/forms/resources"

if ! pgrep -f "worker.py" > /dev/null
then
    ./worker/worker.py & 
fi

./manager/main.py & 

