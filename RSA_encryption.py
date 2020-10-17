import sympy as sy
from sympy import isprime
from sympy import randprime
import math


#the message you want to say
#==================================================================

to_encrypt = input("What would you like to encrypt: ")

#begining of alg
#==================================================================
def rsa_encryption(to_encrypt):
    p = sy.randprime(5,300)
    q = sy.randprime(5,300)

    n = p*q

    def lcm(a,b):
        return abs(a*b)//math.gcd(a,b)

    l_n = lcm((p-1), (q-1))

    def get_e(l_n):
        for e in range(50,l_n):
            if isprime(e)==True:
                e+=1
            elif math.gcd(e,l_n)==1:
                return(e)

    e = get_e(l_n)


    def get_d_values(l_n):

        for x in range(1, l_n):
            if x*e % l_n == 1:
                break
        return(x)

    d = get_d_values(l_n)

    string_version = list(to_encrypt)
    def letter_to_int(letter):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        return alphabet.index(letter) + 1

    empty = []
    for letter in string_version:
        a = letter_to_int(letter)
        empty.append(a)


    def rsa_encrypt(empty):
        message_encrypt= []
        values_needed = [d,n,e]
        for m in empty:
            c = m**e % n
            C = str(c)
            message_encrypt.append(C)
        return(message_encrypt,values_needed)

    encrStr = rsa_encrypt(empty)


    return encrStr

#This is going to print our a formatted answer to the string that you would like to encrypt. Should you like to have spaces in your message, please use an X or x to denote this 
#as enpty spaces are not supported in this code.

print(f"{to_encrypt.title()} encrypted is = " , rsa_encryption(to_encrypt)[0], 'd = {} n = {} e = {}'.format(
    int(
        rsa_encryption(to_encrypt)[1][0]
        ),
        int(
            rsa_encryption(to_encrypt)[1][1]
            ),
            int(
                rsa_encryption(to_encrypt)[1][2]
                )
                )
                )
