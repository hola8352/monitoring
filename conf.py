#!/usr/bin/env python
#coding=utf-8
"""
Author:         何丹 <hedan@corp.netease.com>
Filename:       conf.py
Date created:   2016-03-02 11:21
Last modified:  2016-03-02 11:21

Description:

"""

from recommonmark.parser import CommonMarkParser

source_parsers = {
            '.md': CommonMarkParser,
            }

source_suffix = ['.rst', '.md']
