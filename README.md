glusterfs-rest
===============

GlusterFS REST API server

## Installation

    cd $GLUSTER_SRC/rest
    sudo python setup.py install
    sudo glusterrest install # (Reinstall also available, sudo glusterrest reinstall)

## Usage

Start the glusterrest service using `sudo glusterrestd`

`sudo glusterrest --help` for more details.

## CLI Guide

**Available Groups and Permissions**

    glusteruser  - peers_info_get, volumes_info_get
    glusteradmin - peers_info_get, volumes_info_get, peer_create,
                   volume_create, volume_restart, volume_stop,
                   volume_start
    glusterroot  - peers_info_get, volumes_info_get, peer_create,
                   volume_create, volume_restart, volume_stop,
                   volume_start, peer_delete, volume_delete


**Create a REST user**  
    sudo glusterrest useradd <USERNAME> -g <GROUPNAME>

**Delete a REST user**  
    sudo glusterrest userdel <USERNAME>

**Modify user Group**  
    sudo glusterrest usermod <USERNAME> -g <GROUPNAME>

**To change the user password**  
    sudo glusterrest passwd <USERNAME>

**Modify REST server PORT**  
By default it runs in port 9000, to change

    sudo glusterrest port 80

**View Information about REST users, config or Groups**  
    sudo glusterrest show users
    sudo glusterrest show config
    sudo glusterrest show groups

## API documentation

Quick summary of APIs available, for detailed documentation run `sudo glusterrestd` and visit [http://localhost:9000/api/1.0/doc](http://localhost:9000/api/1.0/doc)

    Get Volumes Info              GET     /api/1.0/volumes
    Get a Volume Info             GET     /api/1.0/volume/:name
    Create a Volume               POST    /api/1.0/volume/:name
    Delete a Volume               DELETE  /api/1.0/volume/:name
    Start a Volume                PUT     /api/1.0/volume/:name/start
    Stop a Volume                 PUT     /api/1.0/volume/:name/stop
    Restart a Volume              PUT     /api/1.0/volume/:name/restart
    Get Peers info                GET     /api/1.0/peers
    Attach a host to cluster      POST    /api/1.0/peer/:hostname
    Detach a host from cluster    DELETE  /api/1.0/peer/:hostname
