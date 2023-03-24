#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

if ! ( nginx -v &>/dev/null); then
    sudo apt update -y -qq && \
        sudo apt install -y nginx -qq
fi

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$html" | tee /data/web_static/releases/test/index.html

if [ -h /data/web_static/current ]; then
    sudo rm -f /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /data/web_static/releases/test/index.html;
        index index.html;
        server_name _;
        location /hbnb_static/ {
			# try_files \$uri \$uri/ =404;
			alias /data/web_static/current/;
			autoindex off;
        }

}
"

echo "$config" | tee /etc/nginx/sites-available/default

if [ "$(pgrep nginx | wc -l)" -le 0 ];then
    service nginx start
else
    service nginx restart
fi;
