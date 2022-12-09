
# Omar El-Sharif


'''This script generates a 1000 line .txt file. Each line in the file consists of a faculty 
first name, last name, rank, and salary. Faculty’s first name and last name for the ith line are 
FirstNamei and LastNamei. The rank is randomly generated as assistant, associate, and full. The 
salary is randomly generated as a number with two digits after the decimal point. The salary for 
assistant professor is a number in the range from 50,000 to 80,000, for associate professor from 
60,000 to 110,000, and for full professor from 75,000 to 130,000. The file is then saved in Salary.txt. 
Another function takes an input filename (Salary.txt). That function reads the data from 
Salary.txt file and displays the total salary for assistant professors, associate professors, full 
professors, and all faculty, respectively, and the average salary for assistant professors, associate 
professors, full professors, and all faculty, respectively.

Finally, a main function calls the above two functions.''' 




import random 


# blank = first name, last name, rank, and salary

ranks = ["assistant", "associate",  "full"]

salaryassistant  = 0 
salaryassociate   = 0
salaryfull = 0

countassistant = 0 
countassociate  = 0
countfull = 0 




file = open("Salary.txt", "w") 

for i in range(1,1001):
    ranknum = random.randint(0,2)
    rank = ranks[ranknum]
    if rank == "assistant": 
        salary = random.uniform(50000,80000)
        countassistant += 1
        salaryassistant += salary 
    elif rank == "associate":
        salary = random.uniform(60000,110000)
        countassociate  += 1
        salaryassociate   += salary 
    else:
        salary = random.uniform(75000,130000)
        countfull +=1
        salaryfull  += salary

    

    salary = "{0:.2f}".format(salary)


    
    x = ("FirstName" + str(i) + " LastName" + str(i) + " " + rank + " " + str(salary))
    #print(x)
    file.write(x)
    file.write("\n")
    




if countfull > 0:
    
    avgfull = salaryfull/countfull
else:
    avgfull = 0
if countassistant > 0: 
    avgassistant = salaryassistant/countassistant
else:
    avgassistant = 0
if countassociate  >0: 
    avgassociate =  salaryassociate /countassociate 
else: avgassociate  = 0



salaryassistant = "{0:.2f}".format(salaryassistant)
salaryassociate  = "{0:.2f}".format(salaryassociate )
salaryfull = "{0:.2f}".format(salaryfull)



avgassistant = "{0:.2f}".format(avgassistant)
avgassociate  = "{0:.2f}".format(avgassociate )
avgfull = "{0:.2f}".format(avgfull)






a = ("Total salary for assistant professors:",salaryassistant )
b= ("Total salary for associate professors:",salaryassociate )
c= ("Total salary for full professors:",salaryfull)
d= ("Average salary for assistant professors:",avgassistant)
e= ("Average salary for associate professors:",avgassociate )
f= ("Average salary for full professors:",avgfull)

a = list(a)

a = " ".join([a[0], a[1]]) 

b = list(b)

b = " ".join([b[0], b[1]]) 

c = list(c)

c = " ".join([c[0], c[1]]) 

d = list(d)

d = " ".join([d[0], d[1]]) 

e = list(e)

e = " ".join([e[0], e[1]]) 


f = list(f)

f = " ".join([f[0], f[1]]) 


##file.write(str(a))
##file.write("\n")
##file.write(str(b))
##file.write("\n")
##file.write(str(c))
##file.write("\n")
##file.write(str(d))
##file.write("\n")
##file.write(str(e))
##file.write("\n")
##file.write(str(f))
##file.write("\n")




print(a)
print(b)
print(c)
print(d) 
print(e)
print(f) 

file.close() 


