# Installation
1. Install odoo requirements:
```
python -m pip install -r ./odoo/requirements.txt setuptools
```
2. Create `.env` file
```
DB_PASSWORD=*****
ODOO_ADMIN_PASSWORD=*****
```
3. Create `odoo.conf` file
```
[options]
addons_path=./odoo/addons,./odoo/odoo/addons
admin_passwd=*****
db_host=localhost
db_post=5432
db_user=odoo
db_password=*****
```
4. Run odoo community with 
```
docker compose up
```
5. Create database with 
```
python ./odoo/odoo-bin -c ./odoo.conf -d curso_odoo -i base
```
Wait until it says `Registry loaded in 100.150s`
6. Enter localhost:8069 with credentials admin and admin_passwd (from `odoo.conf`)

# Run / debug setup in PyCharm
1. Select script `./odoo/odoo-bin`
2. Enter working parameters `-c ./odoo.conf -d curso_odoo -i base`
3. Enter working directory `./`

