import sys
try:
    
    number = int(sys.argv[1])

    
    if(number%2 ==0):
      print(int(sys.argv[1]))
      print("pair")
   
    else:
    
     print(int(sys.argv[1]))
     print("impair")
except:
    print("Tu ne me la mettras pas à l'envers.")