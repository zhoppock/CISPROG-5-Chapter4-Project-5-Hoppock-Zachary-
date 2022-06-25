"""
Shifts a set of bit string to their left once.
"""

def shiftLeft():
  bits = input("\nEnter a string of bits: ")
  result = ''
  if len(bits) > 0:
    result = bits[1:] + bits[0]
  print("\nThe shifted bit set is: " + result)