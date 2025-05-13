#!/bin/bash

debug=0
kill_worker=1

if [ $debug -eq 1 ]; then
    USER_HOME=$(pwd)
else
    USER_HOME="$HOME/.WallMan"
fi

#echo "User Home: $USER_HOME" >> /tmp/wallman.log
pid=$(pgrep -f "worker.py")
if [ -n $"pid" ]; then

    if  [ $kill_worker -eq 1 ]; then
		echo "Matando o worker brutalmente"
        kill -9 $pid
	else
		echo "Apenas reiniciando o socket"
		kill $pid
    fi
fi

#echo  "Verifying worker" >> /tmp/wallman.log


export WALLMAN_ROOT="$USER_HOME"
export UNIX_SOCKET_FILE="/tmp/socket_file"
export SETTINGS_JSON="$USER_HOME/configs/settings.json"
export CURRENT_SETTINGS_JSON="$USER_HOME/configs/currentSettings.json"
export RESOURCES_DIR="$USER_HOME/manager/view/forms/resources"
export WORKER_STATE_FILE="$USER_HOME/configs/worker_state.json"

cd $WALLMAN_ROOT

#echo "Exporting variables" >> /tmp/wallman.log

if ! pgrep -f "worker.py" > /dev/null
then
    echo "Subindo novo worker"
    poetry run python ./worker/worker.py &
fi

poetry run python ./manager/main.py

#echo "Wallman launched" >> /tmp/wallman.log
