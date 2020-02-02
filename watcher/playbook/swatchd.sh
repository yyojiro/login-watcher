#!/bin/bash
source /etc/profile
swatch -c /etc/login-watch.conf -t /var/log/secure --daemon  1>> /var/log/swatch.log 2>& 1

