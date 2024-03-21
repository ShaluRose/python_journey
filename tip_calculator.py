bill=float(input("What is the bill amount?\n"))
people=int(input("How many people are splitting the bill?\n"))
tip=float(input("What percentage tip would you like to give?\n"))

each_person_pays=(bill/people)*(tip/100+1)
each_person_pays_format="{:.2f}".format(each_person_pays)
print(f"Each person should pay {each_person_pays_format}")
