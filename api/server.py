""" Deploys Flask app as wsgi server. """
from gevent.monkey import patch_all; patch_all()
from gevent import pywsgi

from app import app

server_wsgi = pywsgi.WSGIServer(listener=('0.0.0.0', app.config['LISTENER']['port']), application=app)


def run(server):
    return server.serve_forever()


if __name__ == '__main__':
    run(server_wsgi)
