import sys
sys.path

from embed import embedFunc
from extract import extractFunc
from chacha import encrypt,decrypt
import pyperclip as py

def hideFunc(SM,password,CM):
    encSM=encrypt(password,SM)
    print("Enkripsi anda:",encSM)
    CM_HM=embedFunc(encSM,CM)
    print("Kaper Pesan=",CM_HM)
    py.copy(CM_HM)
    return CM_HM
