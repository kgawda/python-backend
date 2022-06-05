Instalacja na Linuxie z Apache
------------------------------

Dla systemu Ubuntu 20.04.
Celowo nie używamy virtualenv (wytłumaczone na zajęciach).
Dla użytkownika *kurs* (najpierw wygenerować klucz ssh i dodać jako "Deploy key" do repozytorium) i repozytorium *delta*:

```bash
sudo apt install python3-pip apache2 apache2-utils libapache2-mod-wsgi-py3
sudo mkdir /opt/webserver
sudo chown -R kurs:kurs /opt/webserver
cd /opt/webserver
git clone ADRES_REPOZYTORIUM_SSH
cd delta
sudo pip install --system -r requirements.txt

sudo rm /etc/apache2/sites-enabled/000-default.conf
sudo nano /etc/apache2/sites-available/001-delta.conf
```
Wpisujemy zawartość:
```
<VirtualHost *:80>

WSGIScriptAlias / /opt/webserver/delta/delta/wsgi.py
WSGIDaemonProcess delta python-path=/opt/webserver/delta
WSGIProcessGroup delta

Alias /static/ /opt/webserver/delta-static/
<Directory /opt/webserver/delta-static>
Require all granted
</Directory>

<Directory /opt/webserver/delta>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

</VirtualHost>
```

W `manage.py shell` (może być na lokalnym komputerze) generujemy klucz:
```python
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

Edytujemy `delta/settings_local.py`:
```python
DEBUG = False
SECRET_KEY = TU_WKLEJAMY_KLUCZ
STATIC_ROOT = "/opt/webserver/delta-static"
```

```bash
python3 manage.py collectstatic
sudo ln -s /etc/apache2/sites-available/001-delta.conf /etc/apache2/sites-enabled/
sudo systemctl restart apache2
```