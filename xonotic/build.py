#!/usr/bin/python

import os
import sys
import os.path as path
sys.path.append(path.join(path.dirname(path.abspath(sys.argv[0])), ".."))
import build_support as bs

def iterations(_, hw):
    if hw == "bdw":
        return 30

class XonoticTimeout:
    def __init__(self):
        self._options = bs.Options()
    def GetDuration(self):
        base_time = 20
        if "bsw" in self._options.hardware:
            base_time = base_time * 2
        if self._options.type == "daily":
            base_time = base_time * 5
        return base_time

bs.build(bs.PerfBuilder("xonotic", iterations=20,
                        custom_iterations_fn=iterations),
         time_limit=XonoticTimeout())

