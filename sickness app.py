x = input("Enter the temperature: ").lower()
m = ""
n = ""
def fever(x):

    if x == 'high':
        print("high fever")
    elif x=='low':
        print("low fever")
    else:
        print("ok")

f = fever(x)


def weak(m):
    print("Do you experience General body weakness: ")
    m = input("Enter y for yes and n for No: ").lower()
    if m == 'y':

        print("Experincing General body weakness")

    else:
        print("Normal")

w = weak(m)

def headache(n):
    print("Do you experience a headache: ")
    n = input("Enter y for yes and n for No: ").lower()
    if n == 'y':

        print("Experincing a headache ")

    else:
        print("Normal")
h = headache(n)
print(f'With the following signs and syptoms\nit shows that\nyou have malaria')

