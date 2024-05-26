##EXTRACTING ALGORITHM
import math

#XOR dari dua binner
def xor(a, b, n): 
    ans = "" 
      
    # perulakangan untuk iterasi atas 
    # string biner
    for i in range(n): 
          
        # If the Character matches 
        if (a[i] == b[i]):  
            ans += "0"
        else:  
            ans += "1"
    return ans

def binaryToDecimal(n): 
  return int(n,2)

SM_extract=""
MR_SK="121"
hashed_SM_binary_extract=""
ZWC_reverse={u'\u200C':"00",u'\u202C':"01",u'\u202D':"10",u'\u200E':"11"}


def extractFunc(CM_HM):
  global SM_extract,MR_SK,hashed_SM_binary_extract,ZWC_reverse
  for letter in CM_HM:
    if(letter in ZWC_reverse):
      hashed_SM_binary_extract+=ZWC_reverse[letter]

  MS_SK_extract=hashed_SM_binary_extract[0:8]

  MR_SK_binary='{0:08b}'.format(int(MR_SK))

  if(MS_SK_extract==MR_SK_binary):
    hashed_SM_binary_extract=hashed_SM_binary_extract[8:]
    LSK_extract=len(MR_SK_binary)
    if((len(hashed_SM_binary_extract)%LSK_extract)==0):
      P=0
    else:
      P=1
    NC_extract= int((len(hashed_SM_binary_extract)/LSK_extract)+P)
    hash_position_bits_extract=NC_extract*MR_SK_binary
    SM_binary_extract=xor(hashed_SM_binary_extract,hash_position_bits_extract,len(hashed_SM_binary_extract))


    while(len(SM_binary_extract)>=12):
      alpha_beta=SM_binary_extract[0:12]
      SM_binary_extract=SM_binary_extract[12:]
      alpha_extract=alpha_beta[0:6]
      beta_extract=alpha_beta[6:12]
      # print("aplha=",alpha_extract,"beta=",beta_extract)
      alpha_final=binaryToDecimal(alpha_extract)
      beta_final=binaryToDecimal(beta_extract)
      # print("aplha=",alpha_final,"beta=",beta_final)
      n_final=((pow(2,alpha_final)*(2*beta_final+1))-1)
      SM_extract=SM_extract+chr(n_final)
  print("Pesan rahasia terenkripsi yang diterima:",SM_extract)
  return SM_extract
  


 
