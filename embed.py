##EMBEDDING ALGORITHM

import math

# fungsi untuk memeriksa log basis 2
def Log2(x):
    if x == 0:
        return False
    return (math.log10(x) /
            math.log10(2))
 

# apakah x adalah pangkat 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))

# xor dari dua string
def xor(a, b, n): 
    ans = "" 
      

    # perulanan string biner
    for i in range(n): 
          
        # If the Character matches 
        if (a[i] == b[i]):  
            ans += "0"
        else:  
            ans += "1"
    return ans

def binaryToDecimal(n): 
  return int(n,2)


MS_SK="121" 
SM_binary=""
ZWC={"00":u'\u200C',"01":u'\u202C',"10":u'\u202D',"11":u'\u200E'}
ZWC_reverse={u'\u200C':"00",u'\u202C':"01",u'\u202D':"10",u'\u200E':"11"}

def embedFunc(SM,CM):
  global MS_SK,SM_binary,ZWC,ZWC_reverse
  for letter in SM:
    n=ord(letter)
    factors=[]
    for i in range(1,n+1):
        if (n+1)%i==0:
          factors.append(i)
  
    odd_factors_list=[]
    for i in range(len(factors)):
      if(factors[i]%2!=0):
        odd_factors_list.append(factors[i])
    alpha=-99999
    for odd_factor in odd_factors_list:
      power_exists=isPowerOfTwo(int((n+1)/odd_factor))
      if(power_exists):
        power=math.log10(int((n+1)/odd_factor))/math.log10(2)
        if(power>alpha):
          alpha=int(power)
    if(alpha==-99999 and n%2==0):
      alpha=0
    # print("alpha=",alpha)
    alpha_binary='{0:06b}'.format(alpha)
    # print("alpha in 6-bit binary format=",alpha_binary)
    beta=int((((n+1)/pow(2,alpha))-1)/2)
    # print("beta=",beta)
    beta_binary='{0:06b}'.format(beta)
    # print("beta in 6-bit binary format=",beta_binary)
    SM_binary=SM_binary+alpha_binary+beta_binary
  MS_SK_binary='{0:08b}'.format(int(MS_SK))
  # MS_SK_binary=MS_SK_binary.strip("0")
  # print(MS_SK_binary)
  LSK=len(MS_SK_binary)
  if(len(SM_binary)%LSK==0):
    P=0
  else:
    P=1
  NC=int((len(SM_binary)/LSK)+P)

  hash_position_bits=NC*MS_SK_binary

  hashed_SM_binary=xor(SM_binary,hash_position_bits,len(SM_binary))

  HM_SK=""
  i=0
  x=""
  while(i<len(MS_SK_binary)-1):
    x=MS_SK_binary[i]+MS_SK_binary[i+1]
    HM_SK+=ZWC[x]
    i+=2

  # print("HM_SK=",HM_SK)
  HM_ZWC=""
  i=0
  x=""
  while(i<len(hashed_SM_binary)-1):
    x=hashed_SM_binary[i]+hashed_SM_binary[i+1]
    HM_ZWC+=ZWC[x]
    i+=2
  # print("HM_ZWC=",HM_ZWC)
  HM=HM_SK+HM_ZWC
  # print("HM=",HM)
  CM_HM=CM[:-1]+HM+CM[-1]
  return CM_HM

 
