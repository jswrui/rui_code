from __future__ import absolute_import

import os
from flask import Flask

from . import env

def with_blurprints(app):
    # 获取文件夹
    dir_apps = os.path.join(env.DIR_BACKEND, 'apps')
    # 获取蓝图列表
    pbs = []
    for item in os.listdir(dir_apps):
        # 判断是文件
        if os.path.isfile(os.path.join(dir_apps, item)):
            # 去掉后缀.py
            item = item[:-3]
            # 排除__init__
            if item != '__init__':
                pbs.append(item)
    # 加载蓝图
    for pb_name in pbs:
        # from .apps import gongshiwu
        import importlib
        bp_obj = importlib.import_module('.apps.' + pb_name, __package__)
        app.register_blueprint(bp_obj.bp, url_prefix='/' + pb_name)
    return app



def with_top_rotues(app):

    @app.route('/')
    def view_index():
        return '首页'

    return app

def create_app():
    app = Flask(
        __name__,
        static_folder=env.DIR_STATIC,
        template_folder=env.DIR_TEMPLATES
    )

    # 注册蓝图
    app = with_blurprints(app)
    
    # 添加顶级路由
    app = with_top_rotues(app)

    return app