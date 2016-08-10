import json
from fabric.api import *

# hosts
env.hosts =['dn7']
env.use.ssh_config = True
#env.user =  "centos"

#env.key_filename = '~/Downloads/osler-nginx.pem'


def install_es():
  sudo('./es-setup')
  

