# 项目步骤
```bash
mkdir bs-table-demo
cd bs-table-demo/

touch run.py deploy.py README.md requirements.txt

echo Flask >> requirements.txt
echo Flask-SQLAlchemy >> requirements.txt
echo Flask-DebugToolbar >> requirements.txt

mkdir backend
touch backend/__init__.py

mkdir frontend
mkdir frontend/static
mkdir frontend/templates

pip install -r requirements.txt
```

查看
```bash
pip freeze
cat requirements.txt
ll -h
history
```
资源下载
```bash
*[bootstrap-table](https://cdnjs.com/libraries/bootstrap-table)
*[jquery](https://cdnjs.cloudflare.com/ajax/libs/jquery)
```