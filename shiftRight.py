"""
Shifts a set of bit string to their right once.
"""

def shiftRight():
  bits = input("\nEnter a string of bits: ")
  result = ''
  if len(bits) > 0:
    result = bits[-1] + bits[:-1]
  print("\nThe shifted bit set is: " + result)