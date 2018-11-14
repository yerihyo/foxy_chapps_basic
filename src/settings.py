import os.path

FILE_PATH = os.path.abspath(__file__)
SRC_DIR = os.path.dirname(FILE_PATH)
BASE_DIR = os.path.dirname(SRC_DIR)
TMP_DIR = os.path.join(BASE_DIR,"tmp")