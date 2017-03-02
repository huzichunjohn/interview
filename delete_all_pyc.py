#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# 方法一: 递归
# def delete(path):
#    for file in os.listdir(path):
#        full_path = os.path.abspath(os.path.join(path, file))
#
#        if os.path.isdir(full_path):
#            delete(full_path)
#        else:
#            if full_path.endswith(".pyc"):
#                os.remove(full_path)

# 方法二: os.walk
# def delete(path):
#    for root, dirs, files in os.walk(path):
#        for file in files:
#            if file.endswith(".pyc"):
#                full_path = os.path.join(root, file)
#                os.remove(full_path)

# 方法三: glob (python3.5)
