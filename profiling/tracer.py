# -*- coding: utf-8 -*-
# Copyright 2018 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""
覆盖测试
标准库版coverage
"""

import logging
import trace
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../euler'))
sys.path.append(path)

from problems import Problem

log = logging.getLogger(__file__)


def test():
    Problem(2).run()


if __name__ == '__main__':
    tracer = trace.Trace(trace=0, count=1)
    tracer.run('test()')
    r = tracer.results()
    r.write_results(summary=True)
