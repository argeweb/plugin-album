#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/07/08.

from argeweb import datastore

plugins_helper = {
    'title': u'相簿',
    'desc': u'相簿',
    'controllers': {
        'album': {
            'group': u'相簿',
            'actions': [
                {'action': 'list', 'name': u'相簿'},
                {'action': 'add', 'name': u'新增相簿'},
                {'action': 'edit', 'name': u'編輯相簿'},
                {'action': 'view', 'name': u'檢視相簿'},
                {'action': 'delete', 'name': u'刪除相簿'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        }
    }
}