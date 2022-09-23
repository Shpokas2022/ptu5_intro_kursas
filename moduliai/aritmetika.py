from asyncio.log import logger
import logging

#import formatter
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("aritmetika.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s")
file_handler.setFormatter(formatter)

def daugyba(a, b):
    try:
        res = a * b
    except Exception as e:
        logger.error(f"Vykdant funkcija {daugyba.__name__}, ivyko klauda {e.__class__.__name__}: {e}")
        return None
    else:
        logger.info(f"Paleisti funkcija {daugyba.__name__}: {a} * {b} = res")
        return res
daugyba(7, 0)
daugyba (7, 3)