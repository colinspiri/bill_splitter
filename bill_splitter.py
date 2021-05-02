
# Set up variables
people = ["Charlie", "Lucca", "Imran"]
specialty_amounts = {}
for name in people:
    specialty_amounts[name] = 0

# Get total bill info
print("Running bill_splitter.py...")
who_paid = str(input("Who paid the bill? ")).strip().capitalize()
total = float(input("What was the total bill? "))
communal_total = total
print()

# Retrieve specialty amounts
for name in people:
	specialty_amount_input = input("How much did " + name + "'s items cost? ")
	if specialty_amount_input == '':
		continue
	specialty_amounts[name] = float(specialty_amount_input)
	communal_total -= specialty_amounts[name]
print()


# Imran doesn't eat pork
pork = 0
if "Imran" in people:
    pork_input = input("How much did pork cost? (Imran will not be charged) ")
    if pork_input != '':
        pork = float(pork_input)
    print()

# Lucca has a gluten alergy
gluten = 0
glutenfree = 0
if "Lucca" in people:
    gluten_input = input("How much did gluten items cost? (Lucca will not be charged) ")
    if gluten_input != '':
        gluten = float(gluten_input)
    glutenfree_input = input("How much did gluten free items cost? (Lucca pays separately) ")
    if glutenfree_input != '':
        glutenfree = float(glutenfree_input)
        communal_total -= glutenfree
    print()

# Calculate contributions
contributions = {}
for name in people:
    contributions[name] = 0

if pork == 0 and gluten == 0 and glutenfree == 0:
    for name in contributions:
        contributions[name] += communal_total/len(people)
else:
    total_no_pork = communal_total - pork
    total_no_pork_nor_gluten = total_no_pork - gluten
    for name in contributions:
        contributions[name] += total_no_pork_nor_gluten/len(people)
    for name in contributions:
        if name == "Imran":
            continue
        contributions[name] += pork/(len(people) - 1)
    for name in contributions:
        if name == "Lucca":
            continue
        contributions[name] += gluten/(len(people) - 1)

# Add back specialty amounts
for name in people:
    contributions[name] += specialty_amounts[name]
if "Lucca" in people:
    contributions["Lucca"] += glutenfree


# Print contributions
print(" --------------------- ")
for name in contributions:
	contributions[name] = round(contributions[name], 2)
	if name == who_paid:
		continue
	print(name + " owes " + who_paid + " " + str(contributions[name]))
print()
print(who_paid + " is contributing " + str(contributions[who_paid]))
print()















