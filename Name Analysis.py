
# Omar El-Sharif 

'''This script takes a boy or girl name as an input,
and analyzes them in comparison to the most popular boy and girl names
included in seperate .txt files, then determines whether the name specified
is amongst them. The user can decline to enter names, and receives a report
regarding their input's results in the shell.''' 



boys = "BoyNames.txt"
boys = open(boys,"r")
boyslist = [] 
for aline in boys:
    boyslist.append(aline) 

girlslist = []
girls = "GirlNames.txt"
girls = open(girls,"r")
for aline in girls:
    girlslist.append(aline)

#print(girlslist)
finalgirls = []
for i in girlslist:
    i = i.replace("\n","")
    finalgirls.append(i) 

    
finalboys = []
for i in boyslist:
    i = i.replace("\n","")
    finalboys.append(i) 

#print(finalboys)
#print(finalgirls)

check = "yes"
if check == "yes":
    boysname = str(input("Enter a boy's name, or N if you do not wish to enter a boy's name: "))
    if boysname == "N":
        finalb = ("You chose not to enter a boy's name") 
    else:
        for i in finalboys:
            if i == boysname:
                finalb = []
                finalb.append(str(boysname))
                finalb.append("is one of the most popular boy's names")
                
                finalb = " ".join([finalb[0], finalb[1]])


                check = "no"
        if check == "yes":

            finalb = []
            finalb.append(str(boysname))
            finalb.append("is not one of the most popular boy's names")
                
            finalb = " ".join([finalb[0], finalb[1]])
            check = "no" 

   
    girlsname = str(input("Enter a girl's name, or N if you do not wish to enter a girl's name: "))
    if girlsname == "N":
        finalg = ("You chose not to enter a girl's name")

        
    else:
        for i in finalgirls:
            if i == girlsname:
                finalg = []
                finalg.append(str(girlsname))
                finalg.append("is one of the most popular girl's names")
                
                finalg = " ".join([finalg[0], finalg[1]])

                check = "no"


        if check == "yes":

            finalg = []
            finalg.append(str(girlsname))
            finalg.append("is not one of the most popular girl's names")
                
            finalg = " ".join([finalg[0], finalg[1]])
            check = "no" 


    print(finalb)
    print(finalg)




                

