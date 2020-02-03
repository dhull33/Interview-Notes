"""
Find the greatest common devisor of two intergers using the Euclidean
Algorithm
THEOREM:
  Let a and b be positive intergers with a >= b > 0. Then there is an
  algorithm that finds (a,b)
NOTE: (a,b) means gcd of integers a and b

LEMMA:
  If a, b, q, r are integers and a = bq + r, then (a,b) = (b,r)
  """

def gcd(a, b):
    while b != 0:
        r = a
        a = b
        b = r % b

    return a

print(gcd(7, 56))
print(gcd(56, 128))
