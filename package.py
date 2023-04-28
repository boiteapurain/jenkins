# -*- coding: utf-8 -*-
name = "jenkins_test"

require = [
    "pyLib-3.10",
    "python-3.10",
]


def commands():
    global env

    env.PATH.append("{root}/tests")

    env.PYTHONPATH.append("{root}/python")
    env.PYTHONPATH.append("{root}/tests")
