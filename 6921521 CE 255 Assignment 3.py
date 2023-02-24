#6921521
#Aboagye Theophilus Amo Oduro
#COMPUTER APPLICATION ASSIGNMENT
#https://github.com/theophilusaa/datastructures.git





Car =["Ford Mustang","Volkswagen Beetle","Nissan Pathfinder","Maruti Suzuki","Toyota Corolla","Chevrolet Equinox","Toyota Sienna","Toyota Land Cruiser Prado",
      "Lexus RX","Toyota Tundra","Toyota Tacoma","Toyota Sequoia","Toyota Matrix","Nissan Pathfinder",
      "Nissan Sentra","Nissan Maxima","Nissan Versa","Nissan Patrol","Nissan Titan","Nissan Frotier",
      "Hyundai Accent","Hyundai Elantra","Hyundai Tucson","Hyundai Sonata","Hyundai Santa Fe","Honda Civic","Honda Accord","Honda Pilot","Honda Odyssey",
      "Mercedes-Benz C-Class"]
Models=["2003","2004","2008","2012","2019","2021","2022"]
Price=[16000,125000,990000,680000,720000,178000,422000]
CarModelPrice=[]
print("Welcome to Theo's car Dealership")
order=input("Which car would you like to buy?")
if order in Car:
   model=input("Please enter the model of the car you would like to buy.")
   if model in Models:
     if model=="2003":
      print("The price of the vehicle chosen is GHS",Price[0])
     elif model=="2004":
      print("The price of the vehicle chosen is GHS",Price[1])
     elif model=="2008":
      print("The price of the vehicle chosen is GHS",Price[2])
     elif model=="2012":
      print("The price of the vehicle chosen is GHS",Price[3])     
     elif model=="2019":
      print("The price of the vehicle chosen is GHS",Price[4])
     elif model=="2021":
      print("The price of the vehicle chosen is GHS",Price[5])
     elif model=="2022":
      print("The price of the vehicle chosen is GHS",Price[6])
   else:
     print("This model is not available")
else:
 print("This vehicle is not available")
 
      
    