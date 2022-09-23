import logging

# logging.basicConfig(
#     level = logging.DEBUG, 
#     encoding="UTF-8", 
#     filename="problemos.log", 
#     format="%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(message)s"
#     )

from moduliai.aritmetika import daugyba

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("aritmetika.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s")
file_handler.setFormatter(formatter)

def dalyba(a, b):
    try:
        res = a / b
    except Exception as e:

        logging.exception(f"Klaida{e.__class__.__name__}: {e}")
    else:
        logging.info(f"dalyba: {a} / {b} = {res}")
        return res
dalyba(7, 0)
dalyba(7, 3)
daugyba(3, 5)