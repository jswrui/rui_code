from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import run


http_server = HTTPServer(WSGIContainer(run.app))

port = 8000
host = '0.0.0.0'
# host = '127.0.0.1'

http_server.listen(port, address=host)
print('running at: [http://{0}:{1}]'.format(host, port))
IOLoop.instance().start()               