from gevent.monkey import patch_all; patch_all()
from app import app
from gevent import pywsgi

server_wsgi = pywsgi.WSGIServer(listener=('0.0.0.0', app.config['LISTENER']['port']), application=app)


def run(server):
    return server.serve_forever()


if __name__ == '__main__':
    run(server_wsgi)
