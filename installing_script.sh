#!bin/bash

USER_HOME="$HOME/.WallMan"

if [ -d "$USER_HOME" ]; then
    rm -rf $USER_HOME
fi

mkdir $USER_HOME

cp . $USER_HOME

chmod +x "$USER_HOME/manager/main.py"
chmod +x "$USER_HOME/worker/worker.py"

if !  echo "$PATH" | grep -q "$USER_HOME"; then
    echo PATH="$PATH:$USER_HOME" >> $USER_HOME/.bashrc
    exec bash
fi

