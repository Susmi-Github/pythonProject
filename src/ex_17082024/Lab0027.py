# Write a Python program to calculate
# area of circle  given its radius using formula
# area = pi *r^2 (Pie =3.14)
import math

# Step 1 Logic Building Formula
#input -> r -> dataType -> float
#pi -> 3.14
#Power -> pow or ** --> any
# Output -> float area, print area

# Step 2  rough logic
# area = 3.14 * Pow(r,2)


#Step 3 - Write the Logic

radius = float(input("Enter radius of circle\n"))
print(radius)
area = math.pi * math.pow(radius,2)
area2 = 3.14 *(radius ** 2)
print("Area of circle is",area)
print("Area of circle is",area2)
print(f"Area of circle is,{area: .2f}")


