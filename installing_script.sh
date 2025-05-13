#!/bin/bash

USER_HOME="$HOME/.WallMan"
SH_RC=".zshrc"


if [ -d "$USER_HOME" ]; then
    cp -r $USER_HOME/configs /tmp/
    rm -rf $USER_HOME
fi
mkdir $USER_HOME

mv /tmp/configs $USER_HOME


cp -r * $USER_HOME

if ! command -v poetry &> /dev/null
then
    echo "Poetry não encontrado, instalando poetry"
    pip3 install poetry --break-system-packages
fi

cd $USER_HOME
poetry install --no-root

DESKTOP_PATH="$HOME/.local/share/applications/Wallman.desktop"
APP_NAME="Wallman"
SCRIPT_PATH="$USER_HOME/Wallman.sh"
ICON_PATH="$USER_HOME/manager/view/forms/resources/wallman_icon.jpeg"

echo ${DESKTOP_PATH}

echo "[Desktop Entry]
Type=Application
Version=0.2.0
Name=$APP_NAME
Comment=Gerenciador de wallpapers
Icon=$ICON_PATH
Exec=$SCRIPT_PATH
Path=$USER_HOME" > $DESKTOP_PATH

chmod +x $USER_HOME/Wallman.sh

if !  echo "$PATH" | grep -q "$USER_HOME"; then
    echo PATH="$PATH:$USER_HOME" >> $HOME/$SH_RC
    exec bash
fi
