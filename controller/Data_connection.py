import pymysql


MYSQL_ADDON_HOST="bosdos6qw6vefrichu88-mysql.services.clever-cloud.com"
MYSQL_ADDON_DB="bosdos6qw6vefrichu88"
MYSQL_ADDON_USER="uzky8nlwzzgffdxj"
MYSQL_ADDON_PORT=3306
MYSQL_ADDON_PASSWORD="8a0LOqTkE8pm0TD1jJFQ"
MYSQL_ADDON_URI="mysql://uzky8nlwzzgffdxj:8a0LOqTkE8pm0TD1jJFQ@bosdos6qw6vefrichu88-mysql.services.clever-cloud.com:3306/bosdos6qw6vefrichu88"
HOST="bosdos6qw6vefrichu88-mysql.services.clever-cloud.com"
DATA_BASE="bosdos6qw6vefrichu88"


def obtener_conexion():
    return pymysql.connect(host=MYSQL_ADDON_HOST,
                                user=MYSQL_ADDON_USER,
                                password=MYSQL_ADDON_PASSWORD,
                                db=DATA_BASE)

#print(str(obtener_conexion()))