# -*- coding: utf-8 -*-
name = "jenkins_test"


def commands():
    global env

    # pythonpath
    env.PYTHONPATH.append("{root}/python")
