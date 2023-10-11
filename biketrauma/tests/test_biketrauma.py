# the following lines add the root directory of the project to os.path
import os.path
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + "..") * 2)

import biketrauma
from biketrauma.io import path_target
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
    assert m == "54c1eefb17a34d2e5ac6c4d0f6c20546"


def test_df():
    df = biketrauma.get_accident(biketrauma.Load_db().save_as_df(), log_scale=False)
    assert df["21"] == 152


def test_df_log():
    df = biketrauma.get_accident(biketrauma.Load_db().save_as_df(), log_scale=True)
    assert np.allclose(df["92"], 7.161622002)
