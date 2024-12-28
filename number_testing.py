# for i in range(1,5):
#     for k in range(1,i+1):
#         print(k, end="") 
#     print()    

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1) 
# num = int(input("enter a number"))    
# print("factorial of",num,"is",factorial) 

import math

def calculate_area():
  """Calculates the area of a shape.

  Currently supports:
    - Circle: Requires radius as input.
    - Square: Requires side length as input.
    - Rectangle: Requires length and width as input.

  Returns:
    The calculated area.
  """
  shape = input("Enter shape (circle, square, rectangle): ").lower()

  if shape == "circle":
    radius = float(input("Enter radius: "))
    area = math.pi * radius**2
  elif shape == "square":
    side = float(input("Enter side length: "))
    area = side**2
  elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
  else:
    print("Invalid shape.")
    return None

  return area

def calculate_sqrt():
  """Calculates the square root of a number.

  Returns:
    The calculated square root.
  """
  num = float(input("Enter number: "))
  sqrt = math.sqrt(num)
  return sqrt

def main():
  """Main function to run the calculator."""
  while True:
    print("\nCalculator Menu:")
    print("1. Calculate Area")
    print("2. Calculate Square Root")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      area = calculate_area()
      if area is not None:
        print(f"Area: {area:.2f}") 
    elif choice == '2':
      sqrt = calculate_sqrt()
      print(f"Square Root: {sqrt:.2f}")
    elif choice == '3':
      print("Exiting...")
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()

    

