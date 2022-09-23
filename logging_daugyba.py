import logging

def daugyba(a, b):
    try:
        res = a * b
    except Exception as e:
        logging.error(f"Vykdant funkcija {daugyba.__name__}, ivyko klauda {e.__class__.__name__}: {e}")
        return None
    else:
        logging.info(f"Paleisti funkcija {daugyba.__name__}: {a} * {b} = res")
        return res
