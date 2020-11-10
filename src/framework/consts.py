from pathlib import Path

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+
Visit http://{host}:{port}
..........................................
"""

_this_file_path = Path(__file__).resolve()

DIR_FRAMEWORK = _this_file_path.parent.resolve()

DIR_SRC = DIR_FRAMEWORK.parent.resolve()

DIR_REPO = DIR_SRC.parent.resolve()

DIR_STATIC = (DIR_REPO / "static").resolve()

DIR_STORAGE = (DIR_REPO / "db").resolve()

METHODS_WITH_REQUEST_BODY = {
    "POST",
}

USER_DATA_FILE = (DIR_STORAGE / "user_data.json").resolve()