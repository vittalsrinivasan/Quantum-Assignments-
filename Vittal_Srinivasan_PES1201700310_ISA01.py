from pylab import *
from qutip import *
val='y'
b = Bloch()

while val=='y':
    print("Options to represent the state in Bloch Sphere form:")
    print("1 --> Enter the [x,y,z] coordinates of the state.")
    print("2 --> Enter the values of theta and phi in radians for polar representation of the state.")
    opt=input("Enter option:")
    if opt=='1':
        x=float(input('Enter x coordinate:'))
        y=float(input('Enter y coordinate:'))
        z=float(input('Enter z coordinate:'))
        pnts1 = [x, y, z]
        print("the coordinates are: ",pnts1)
        print("The state is:",z,"|0> + (",x, "+ i", y,")|1>")
        b.add_vectors(pnts1)
        #print("The bloch sphere for state",z,"|0> + (",x, "+ i", y,")|1> is")
        b.show()
        
    elif opt=='2':    
        th=float(input('Enter theta value:'))
        phi=float(input('Enter phi value:'))
        xp = math.sin(phi)*math.cos(th)
        yp = math.sin(th)*math.sin(phi) 
        zp = math.cos(th)
        pnts = [xp, yp, zp]
        print("the coordinates are: ",pnts)
        print("The state is: cos(",th,"/2),|0> +sin(",th,"/2) exp(i",phi,")|1>")
        b1 = Bloch()
        b1.add_vectors(pnts)
        b1.show()
    else:
        print("Please try again")
        
    val=input("Do you want to continue? y/n: ")
    #b.clear()
    print(" ")
