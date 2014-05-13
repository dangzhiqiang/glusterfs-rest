glusterfs-rest
===============

GlusterFS REST API server

## Installation

    git clone git@github.com:aravindavk/glusterfs-rest.git
    cd glusterfs-rest
    sudo python setup.py install

## License

BSD, see LICENSE for more details.

## Usage

`sudo glusterrest --help` for more details.

## API documentation

In the initial version following API are supported/working.

GET    /api/1/volumes/
GET    /api/1/volumes/:name
PUT    /api/1/volumes/:name
PUT    /api/1/volumes/:name/force
DELETE /api/1/volumes/:name
DELETE /api/1/volumes/:name/stop
POST   /api/1/volumes/:name/start
POST   /api/1/volumes/:name/stop
POST   /api/1/volumes/:name/start-force
POST   /api/1/volumes/:name/stop-force
POST   /api/1/volumes/:name/restart
PUT    /api/1/volumes/:name/add-brick
DELETE /api/1/volumes/:name/remove-brick
POST   /api/1/volumes/:name/set
POST   /api/1/volumes/:name/reset


## Blogs

1. [http://aravindavk.in/blog/glusterfs-rest](http://aravindavk.in/blog/glusterfs-rest)
