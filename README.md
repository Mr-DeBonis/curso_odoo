# Installation
1. Run odoo community with 
```
docker compose up
```
2. Create `odoo.conf` file
```
[options]
addons_path=./odoo/addons,./odoo/odoo/addons
admin_passwd==****
db_host=localhost
db_post==****
db_user=odoo
db_password=****

```
3. Create database with 
```
python ./odoo/odoo-bin -c ./odoo.conf -d curso_odoo -i base
```
3. Entrar a localhost:8069 con credenciales admin/admin
