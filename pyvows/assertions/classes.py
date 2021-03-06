#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyVows testing engine
# https://github.com/heynemann/pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows

@Vows.assertion
def to_be_instance_of(topic, expected):
    assert isinstance(topic, expected), "Expected topic(%s) to be an instance of %s, but it was a %s" % (topic, expected, topic.__class__)

@Vows.assertion
def not_to_be_instance_of(topic, expected):
    assert not isinstance(topic, expected), "Expected topic(%s) not to be an instance of %s, but it was" % (topic, expected)

