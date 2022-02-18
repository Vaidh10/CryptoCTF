from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes


p = getPrime(2048)
q = getPrime(2048)
e = 3

phi = (p - 1) * (q - 1)

n = p * q

flag = b"ctf{XXXXXXXXXXXXXXXXXXX}"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)


print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")
