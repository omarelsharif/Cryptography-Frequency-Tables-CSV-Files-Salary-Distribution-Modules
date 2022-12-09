
# Omar El-Sharif


def main():
    filename = input("Enter a filename: ") #You can demo this with USConstitution.txt
    inputFile = open(filename, "r") 
    file = inputFile.read()
    file = file.lower()
    d = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for ch in file:
        if ch in alpha:
            if ch not in d:
                d[ch] = 1
            else:
              
                d[ch] += 1
    keys = list(d.keys())
    keys.sort()
    print("Letter     Count") 
    for key in keys:
        x = key
        y = d[key]
        x = "{0:<10}".format(x)
        y = "{0:<10}".format(y) 
        print(x,y)

        
          
main() 
