"""regions.json okuyucu (mapdata gerektirmez)."""
import json, os
from functools import lru_cache

import numpy as np

GEO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "geo")


@lru_cache(1)
def _data():
    return json.load(open(os.path.join(GEO, "regions.json")))


def region(name):
    return [np.array(r, np.float32) for r in _data()["regions"][name]]


def sevr(name):
    return [np.array(r, np.float32) for r in _data()["sevr"][name]]
