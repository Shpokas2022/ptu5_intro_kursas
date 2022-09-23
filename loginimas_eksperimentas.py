import logging
# loggin yra galinga biblioteka funkcija, yra išskyrti svarbias žinutes
# level debug asocijuojasi su visa informacija
# level info yra kaip patvirtinimas

# Mes pasakome, kad nuo DEBUG lygio mes spausdiname visas žinutes.Šiuo atveju per 
# filename="problemos.log" klaidas mes išsaugome į failą problemos.log
logging.basicConfig(level = logging.DEBUG, filename="problemos.log", encoding="UTF-8",logging.basicConfig(level=logging.DEBUG, filename="problemos.log", format="%(asctime)s:%)

def dalyba(a, b):
    try:
        res = a / b
    except Exception as e:
        # išmetame pranešimą, kad įvyko klaida
        logging.exception(f"Klaida{e.__class__.__name__}: {e}")
    else:
        logging.info(f"dalyba: {a} / {b} = {res}")
        return res
dalyba(7, 0)
dalyba(7, 3)