from shiftLeft import shiftLeft
from shiftRight import shiftRight

option = "y"

print("Welcome to the bit string shifting program.")
while option != "n":
  shiftLeft()
  shiftRight()
  option = input("\nKeep going? (y/n): ")
print("Goodbye.")