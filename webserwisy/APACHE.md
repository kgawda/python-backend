
```bash
sudo rm /etc/apache2/sites-enabled/000-default.conf
sudo nano /etc/apache2/sites-available/001-delta.conf
```

```
<VirtualHost *:80>

WSGIScriptAlias / /opt/webserver/delta/delta/wsgi.py
WSGIDaemonProcess delta python-path=/opt/webserver/delta
WSGIProcessGroup delta

<Directory /opt/webserver/delta>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

</VirtualHost>
```

```bash
sudo ln -s /etc/apache2/sites-available/001-delta.conf /etc/apache2/sites-enabled/
```