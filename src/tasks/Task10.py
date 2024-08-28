# Traingle Classifier
# Equiletaral(all sides are Equal) , isoceles(eaxctly two sides are equal), or scalene

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a==b==c):
    print("Equilateral Triangle")
elif ( (a == b) or (b == c) or ( a == c)):
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")
