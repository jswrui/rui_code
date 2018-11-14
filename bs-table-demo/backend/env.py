import os

# 后端目录
DIR_BACKEND = os.path.dirname(os.path.abspath(__file__))
# 项目目录
DIR_PROJ = os.path.dirname(DIR_BACKEND)
# 前端目录
DIR_FRONTEND = os.path.join(DIR_PROJ, 'frontend')
# 静态目录
DIR_STATIC = os.path.join(DIR_FRONTEND, 'static')
# 模板目录
DIR_TEMPLATES = os.path.join(DIR_FRONTEND, 'templates')