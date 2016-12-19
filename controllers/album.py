#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.
from datetime import datetime
from google.appengine.api import urlfetch
from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search
import json


class Album(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)
        pagination_limit = 10

    class Scaffold:
        display_properties_in_list = ('name', 'image', 'is_enable', 'category')

    @route_menu(list_name=u'backend', text=u'活動相簿', sort=305, group=u'內容管理', need_hr=True)
    def admin_list(self):
        return scaffold.list(self)

    @route_with('/admin/album/detail/<album_name>')
    def admin_detail(self, album_name):
        album = self.meta.Model.find_by_name(album_name)
        if album is not None:
            self.context["album_item"] = album
            self.context["admin_detail"] = album.all_photo()

    @route_with('/admin/album/insert')
    def admin_insert(self):
        album = self.params.get_ndb_record('album')
        if album is not None:
            album.insert_photo(self.params.get_ndb_record('photo'))
            return self.json({'info': 'done'})
        return self.json({'info': 'error'})

    @route_with('/admin/album/create')
    def create(self):
        album = self.meta.Model()
        album.title = self.params.get_string('name', u'未命名相簿')
        album.put()
        return self.json({'info': 'done'})
    #
    # @route_menu(list_name=u'backend', text=u'圖片', sort=9700, icon='files-o', group=u'檔案管理')
    # @route_with('/admin/user_file/images_list')
    # def admin_images_list(self):
    #     self.meta.pagination_limit = 12
    #     model = self.meta.Model
    #
    #     def photo_factory(self):
    #         return model.query(
    #             model.content_type.IN(['image/jpeg', 'image/jpg', 'image/png', 'image/gif'])).order(
    #             -model.content_type, -model.created, model._key)
    #     self.scaffold.query_factory = photo_factory
    #     return scaffold.list(self)
