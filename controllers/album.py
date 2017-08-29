#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
from argeweb import Controller, scaffold, route_menu, route_with, route


class Album(Controller):
    class Scaffold:
        display_in_list = ['name', 'image', 'is_enable', 'category']

    @route_menu(list_name=u'backend', group=u'內容管理', need_hr=True, text=u'活動相簿', sort=315)
    def admin_list(self):
        return scaffold.list(self)

    @route_with('/admin/album/album/detail/<album_name>')
    def admin_detail(self, album_name):
        album = self.meta.Model.get_by_name(album_name)
        if album is not None:
            self.context["album_item"] = album
            self.context["admin_detail"] = album.all_photo()

    @route
    def admin_insert(self):
        album = self.params.get_ndb_record('album')
        if album is not None:
            album.insert_photo(self.params.get_ndb_record('photo'))
            return self.json({'info': 'success'})
        return self.json({'info': 'failure'})

    @route
    def admin_create(self):
        album = self.meta.Model()
        album.title = self.params.get_string('name', u'未命名相簿')
        album.put()
        return self.json({'info': 'success'})
    #