pizzaTopping = ["(B)acon","(O)lives","(H)am","(M)ushrooms","(P)ineapple","(S)alami","(A)nchovies"];
pizzaType = (
			{"name":"Small","price":5,"display":"(S)mall"},
			{"name":"Medium","price":8,"display":"(M)edium"},
			{"name":"Large","price":12,"display":"(L)arge"}
	);

def verifyInputIsNumber(text):
	print(text)
	number=input()
	try:
		val = int(number)
		return val
	except ValueError:
		print("Invalid Input...Please Try Again")
		return verifyInputIsNumber(text)

def confirmYesNo(text):
	print(text)
	choice=input().upper()
	if choice=='Y':
		return True
	elif choice=='N':
		return False
	else:
		print("Invalid Input...Please Try Again")
		return confirmYesNo(text)

def getPizzaType(text):
	print(text)
	choice=input().upper()
	if choice=="S":
		return ["Small",5]
	elif choice=="M":
		return ["Medium",8]
	elif choice =="L":
		return ["Large",12]
	else:
		print("Error!! Invalid Input.. Please Try Again..")
		return getPizzaType(text)

def getTopping(text):
	print(text)
	choice=input().upper()
	if choice == "B":
		return "Bacon"
	elif choice =="O":
		return "Olives"
	elif choice =="H":
		return "Olives"
	elif choice =="M":
		return "Mushrooms"
	elif choice =="P":
		return "Pineapple"
	elif choice =="S":
		return	"Salami"
	elif choice =="A":
		return "Anchovies"
	elif choice =="Q":
		return "Exit"
	else:
		print("Error!! Invalid Input.. Please Try Again..")
		return getTopping(text)

print ("----------------------------------------");
print ("--- Welcome to Pizza Ordering System ---");
print ("----------------------------------------\n")

while True:
	numberOfPizza=verifyInputIsNumber("Number Of Pizza?")
	allOrder=[]
	for x in range(numberOfPizza):
		total=0
		order={}
		print ("******************************************")
		print ("          Starting Order For Pizza #",x+1)
		print ("******************************************")
		print("Select Size Available:")
		print("%-20s%-5s"%("Size","Price"))
		for pizza in pizzaType:
			print("%-20s$%-5d"%(pizza["display"],pizza["price"]))
		selectedSize=getPizzaType("Select Pizza Size")
		order['size']=selectedSize[0]
		total+=selectedSize[1]
		top=[]
		if confirmYesNo("Do You Want To Add Topping (Y)es/(N)o"):
			print("Available Topping")
			for tops in pizzaTopping:
				print (tops)
			print("Press Q to Stop Taking Topping")
			for x in range(0,4):
				text="Select Topping #"+str(x+1)
				tempChoice=getTopping(text)
				if tempChoice=="Exit":
					break
				top.append(tempChoice)
				total+=1
			if len(top)<4:
				for x in range(len(top),4):
					top.append("")
		else:
			for x in range(0,4):
				top.append("")
		order['top1']=top[0]
		order['top2']=top[1]
		order['top3']=top[2]
		order['top4']=top[3]
		order['total']=total
		allOrder.append(order)

	client={}
	print("Client Name:")
	client['name']=input()
	print("Client Phone Number:")
	client['phone']=input()
	sTotal=0
	for sOrder in allOrder:
		sTotal+=sOrder['total']
	client['total']=sTotal
	while True:
		print("(C)ollect or (D)eliver")
		coll=input().upper()
		if coll=="C":
			client['deliveryCharge']=0
			client['collect']="Collect"
			client['address']=False
			break
		elif coll=="D":
			client['deliveryCharge']=0
			if sTotal<30:
				client['deliveryCharge']=8
				client['total']=sTotal+8
			client['collect']="Deliver"
			print("Client Address")
			client['address']=input()
			break
		else:
			print("Input Invalid")

	print("**************************************************************************")
	print("                            Current Order Summary");
	print("**************************************************************************")
	print("%-60s%-10s"%("Name",client['name']))
	print("%-60s%-10s"%("Phone:",client['phone']))
	print("%-60s%-10s"%("Collect/Deliver",client['collect']))
	if client['address']:
		print("%-60s%-10s"%("Address",client['address']))
	print("--------------------------------------------------------------------------")
	print("%-20s%-40s%10s"%("SIZE","TOPPING","TOTAL"));
	print("--------------------------------------------------------------------------")
	aTotal=0
	for nOrder in allOrder:
		aTotal+=nOrder['total']
		print("%-20s%-40s%10d"%(nOrder['size'],nOrder['top1']+nOrder['top2']+nOrder['top3']+nOrder['top4'],nOrder['total']))
	print("--------------------------------------------------------------------------")
	print("%-60s%10d"%("Gross Total",aTotal))
	print("%-60s%10d"%("Delivery Charge",client['deliveryCharge']))
	print("--------------------------------------------------------------------------")
	print("%-60s%10d"%("Total",client['total']))
	print("--------------------------------------------------------------------------")


	print("\n\n\n\n**************************************************************************")
	print("                            THANK YOU");
	print("**************************************************************************")


	if confirmYesNo("New Order (Y)es/(N)o")==False:
		break
	print("****************************STARTING NEW ORDER****************************\n\n\n")