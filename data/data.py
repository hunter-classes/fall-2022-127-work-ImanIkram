# Which NYC borough has the most active projects under constructions in schools 
#Extra: Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis.

import csv
reader = csv.DictReader(open("Active_Projects_Under_Construction.csv"))
data = [x for x in reader]

borough = [str(x['City']) for x in data] #gets all the boroughs in a list

# finds the total number of projects in each borough
def freq(borough,v):
    f = borough.count(v)     
    return f

Bronx =  freq(borough,"Bronx")
Brooklyn = freq(borough,"Brooklyn")
Queens = freq(borough,"Queens")
Manhattan = freq(borough,"Manhattan")
StatenIsland = freq(borough,"Staten Island")

print("The total number of active projects in Manhattan is", Manhattan)
print("The total number of active projects in Queens is", Queens)
print("The total number of active projects in Staten Island is", StatenIsland)
print("The total number of active projects in Brooklyn is", Brooklyn )
print("The total number of active projects in the Bronx is", Bronx,"\n")

# getting the borough with the most active projects
boroughs = {'Bronx':Bronx, 'Brooklyn':Brooklyn, 'Queens':Queens, 'Manhattan':Manhattan, 'Staten Island': StatenIsland}
largest = max(boroughs, key=boroughs.get)
print(largest,"has","the most active projects under construction in schools.")

#Extra: 
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
gborough = ['Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Bronx']
nums = [Brooklyn,Manhattan,Queens,StatenIsland,Bronx]
ax.bar(gborough,nums)
plt.show()