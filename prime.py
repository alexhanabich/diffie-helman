from Crypto.Util import number

# p = number.getPrime(512)
# while not number.isPrime((p-1)//2):
#     p = number.getPrime(512)

p = 8084782846011545368970201750917712101919459630025896040637537536065347159501207468639559632505484585557316452909758331896262238897368264807820799654240247
print(number.isPrime(p))
print(number.isPrime((p-1)//2))
print(len(bin(p)[2:]))

import random
# SystemRandom uses os.urandom(), so it is secure
# a = random.SystemRandom().getrandbits(512)
a = 5063121468016766502302626211989244557170961700604618638279436485209583671269352990406125169974624507671546143985992308520684974559257540701666948869592204
print(len(bin(a)[2:]))


def mod_exp(x, y, N):
    # base case
    if y == 0:
        return 1
    # using properties x^y = (x^(y/2))^2 if y is even & x*(x^(y/2))^2 if y is odd
    # recursively decompose y and compute modulo for each and send it down the stack
    z = mod_exp(x, y//2, N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N


gamodp = mod_exp(5,a,p)
print(gamodp)
