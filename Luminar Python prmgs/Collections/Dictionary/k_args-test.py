f = open("complete.csv","r")

dict={}

for lines in f:
   lines = lines.rstrip().split(",")
   state = lines[1]
   tot_confd = lines[4]
   death = lines[5]
   recovrd = lines[9]

   if (state not in dict):
       dict[state] = {"confirmed": tot_confd, "recovered": recovrd, "death": death}
   else:
       dict[state] = {"confirmed": tot_confd, "recovered": recovrd, "death": death}


