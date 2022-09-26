#!/usr/bin/env bash
# Installs HAProxy version 1.8 with the following configurations:
#+    Enables management via the init script.
#+    Distributes requests using a round-robin algorithm.

apt-get install -y software-properties-common
add-apt-repository -y ppa:vbernat/haproxy-1.8
apt-get update
apt-get install -y haproxy=1.8.\*

echo "ENABLED=1" >> /etc/default/haproxy
mv /etc/haproxy/haproxy.cfg{,.original}
touch /etc/haproxy/haproxy.cfg

printf %s "global
    log 127.0.0.1 local0 notice
    maxconn 2000
    user haproxy
    group haproxy

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    retries 3
    option redispatch
    timeout connect  5000
    timeout client  10000
    timeout server  10000

listen hbnb
    bind 0.0.0.0:80
    mode http
    stats enable
    stats uri /haproxy?stats
    balance roundrobin
    option httpclose
    option forwardfor
    server 375-web-01 104.196.168.90:80 check
    server 375-web-02 35.196.46.172:80 check
" >> /etc/haproxy/haproxy.cfg

service haproxy start
