
items = ["x", "y", "z"]

print((items[i],items[j]) for i in range(len(items)) for j in range(i+1, len(items)))

#[('x', 'y'), ('x', 'z'), ('y', 'z')]

#for i in range(len((items))):
#    for j in range(i+1,len(items)):

 #       print((items[i],items[j]))
