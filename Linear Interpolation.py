Y1= float(input('What is your Y1 value? \n'))
Y2= float(input('What is your Y2 value? \n'))
Y3= float(input('What is your Y3 value? \n'))
X1= float(input('What is your X1 value? \n'))
X3= float(input('What is your X3 value? \n'))
if Y1 == Y3:
  print ("This does not need interpolation.")
else:
  X2 = (Y2-Y1)*(X3-X1)/(Y3-Y1)+X1
  print ("The interpolated X2 value is: " + str(X2))
