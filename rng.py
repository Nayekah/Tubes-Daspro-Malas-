import time

#variable konstanta untuk generate random number
x = round(time.time())
m = 2147483648 
a = 594156893
c = 69420177013

#RNG angka dari l_range sampai dengan r_range
def rng(l_range : int, r_range) -> int:
    x = (a*x + c) % m
    
    range = r_range - l_range + 1
    return l_range + (x % range)