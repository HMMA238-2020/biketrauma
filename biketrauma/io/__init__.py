import os

url_db = "https://github.com/josephsalmon/HAX712X/raw/main/Data/accidents-velos_2022.csv.xz"
path_target = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..",
    "data",
    "bicycle_db.csv.xz",
)
