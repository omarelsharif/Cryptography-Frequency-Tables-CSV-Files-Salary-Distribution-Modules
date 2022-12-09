


# Omar El-Sharif

'''This transposition cipher implements a three-rail fence that takes every third character
and puts into one of the three rails'''



def scramble2Encrypt(plainText,outname):
    evenChars = ""
    oddChars = ""
    charCount = 1
    for ch in plainText: 
        if charCount ==2:          
            evenChars = evenChars + ch
            charCount = 1 
          
        else:
            oddChars = oddChars + ch
            charCount = 2
        
    cipherText = evenChars + oddChars
    #print(cipherText)

    output = open(outname, "w")
    output.write(cipherText)
    output.close()

def scramble2Decrypt(cipherText, outname):
    
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]      
    evenChars = cipherText[halfLength:]
    plainText = ""
    
    for i in range(halfLength):             
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

        
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    
    output = open(outname, "w")
    output.write(plainText)
    output.close()


def main():
    filename = input("Enter a source filename: ")
    outname = input("Enter a target filename: ")
    choice = input("Enter E to encrypt or D to decrypt the input file: ")
    
                    
    fopened = open(filename, "r")
    file = fopened.readlines()
    stringfile = ""
    for ch in file:
        stringfile += ch
    if choice == "E": 
        scramble2Encrypt(stringfile,outname)
    
    elif choice == "D":
        scramble2Decrypt(stringfile,outname)


main()
