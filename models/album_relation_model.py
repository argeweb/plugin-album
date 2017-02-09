#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from album_model import AlbumModel
from plugins.file.models.file_model import FileModel


def get_all_file_with_album(album_key):
    return AlbumRelationModel.query(AlbumRelationModel.album == album_key)


class AlbumRelationModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'系統編號')
    file = Fields.KeyProperty(verbose_name=u'檔案', kind=FileModel)
    album = Fields.KeyProperty(verbose_name=u'相簿', kind=AlbumModel)
