# the following lines add the root directory of the project to os.path
import os.path
import sys

# install biketrauma as a package if needed with
# python setup.py install
import biketrauma
from biketrauma.io import url_db, path_target
import hashlib
import numpy as np
import pandas as pd


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def test_dl():
    biketrauma.Load_db()
    m = md5(path_target)
    if (
        url_db
        == "https://github.com/josephsalmon/HAX712X/raw/main/Data/accidents-velos_2022.csv.xz"
    ):
        my_hash = "54c1eefb17a34d2e5ac6c4d0f6c20546"
    else:
        my_hash = "ee8c4e0e7989bc6aac7876d7501bbf4d"

    assert m == my_hash


def test_df():
    df = biketrauma.get_accident(
        biketrauma.Load_db().save_as_df(), log_scale=False
    )
    # check if the version of the data is from after 2022
    if (
        url_db
        == "https://github.com/josephsalmon/HAX712X/raw/main/Data/accidents-velos_2022.csv.xz"
    ):
        target = 152
    else:
        target = 459
    assert df["21"] == target


def test_df_log():
    df = biketrauma.get_accident(
        biketrauma.Load_db().save_as_df(), log_scale=True
    )
    if (
        url_db
        == "https://github.com/josephsalmon/HAX712X/raw/main/Data/accidents-velos_2022.csv.xz"
    ):
        target = 7.161622002
    else:
        target = 7.651120176
    assert np.allclose(df["92"], target)
