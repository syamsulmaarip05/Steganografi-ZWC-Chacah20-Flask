from extract import extractFunc
from chacha import decrypt

def revealFunc(CM_HM,password):
    SM_extract=extractFunc(CM_HM)
    print("Pesan tersembunyi anda:",decrypt(password,SM_extract))
    return decrypt(password,SM_extract)
