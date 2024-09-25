from enum import Enum
import os

class pathOperationType(Enum):
    ADD = 0,
    SHOW = 1,
    REMOVE = 2

class envorimentVariables(Enum):
    wallman_root = os.getenv("WALLMAN_ROOT"),
    unix_socket_file = os.getenv("UNIX_SOCKET_FILE"),
    settings_json = os.getenv("SETTINGS_JSON"),
    current_settings_json = os.getenv("CURRENT_SETTINGS_JSON"),
    resourses_dir = os.getenv("RESOURCES_DIR")