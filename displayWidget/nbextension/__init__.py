#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Doris Lee
# Distributed under the terms of the Modified BSD License.

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'nbextension/static',
        'dest': 'displayWidget',
        'require': 'displayWidget/extension'
    }]
