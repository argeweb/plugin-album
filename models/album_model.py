#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from plugins.application_user.models.application_user_model import ApplicationUserModel


class AlbumModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'系統編號')
    title = Fields.StringProperty(verbose_name=u'相簿名稱')
    creator = Fields.KeyProperty(verbose_name=u'建立者', kind=ApplicationUserModel)
    count = Fields.IntegerProperty(verbose_name=u'相片數量', default=0)

    @property
    def get_first_img(self):
        return '/plugins/album/static/empty-album.png'

    def insert_photo(self, ndb_item):
        from ..models.album_relation_model import AlbumRelationModel
        if ndb_item is None:
            return
        n = AlbumRelationModel()
        n.album = self.key
        n.file = ndb_item.key
        n.put()
        self.count += 1
        self.put()

    def all_photo(self):
        from ..models.album_relation_model import get_all_file_with_album
        return get_all_file_with_album(self.key)