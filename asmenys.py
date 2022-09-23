import logging
import logger

# logging.basicConfig(
#     filename="asmenys.log",
#     level=logging.INFO,
#     format="%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s"
#)

logger = logging.getLogger(__name__)
# Susikuriame file_handler, kuris zinutes rasys i nurodyta faila
file_handler = logging.FileHandler("aritmetika.log")
# logeriui priskyriame file handleri
logger.addHandler(file_handler)
# nurodome kokio lygio zinutes loggeris apdoros
logger.setLevel(logging.DEBUG)
# Nurodo zinuciu formata
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s")
# Sukuriame streamhanleri , kuris zinutes spauisdina i terminala
file_handler.setFormatter(formatter)
# Sukuriame streamhandleri, kuris zinutes spausdins i terminala
stream_handles = logging.StreamHandler()
# Priskiriame stream handleriui formata (ta pati, kuri buvome priskyre ir file handleriui)
stream_handles.setFormatter(formatter)
# Logeriui priskiriam stream handler, panasiai kaip ir buvome priskyre file handleri
logger.addHandler(stream_handles)

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
#       logging.info(f"sukurtas asmuo {vardas} {pavarde")
        logging.info(f"Sukurtas klases {self.__class__.__name__} objektas {vardas} {pavarde}")

ingrida = Asmuo("Ingrida", "Vaitkuviene")
darius = Asmuo("Darius", "Vasionis")
print(logger.dalyba(2, 5))
