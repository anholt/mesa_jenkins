#!/usr/bin/python

import os
import sys
import os.path as path
sys.path.append(path.join(path.dirname(path.abspath(sys.argv[0])), ".."))
import build_support as bs


def iterations(_, hw):
    if hw == "bdw":
        return 15

bs.build(bs.PerfBuilder("fill_o", iterations=10,
                        custom_iterations_fn=iterations))

