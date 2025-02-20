def caesar(text,s):
    print("The Encrypted text is : ")
    for i in range(len(text)):
        char = text[i]        
        if (char.isupper()):
            print(chr((ord(char) + s-65) % 26 + 65),end ="")
        elif(char.islower()):
            print(chr((ord(char) + s - 97) % 26 + 97),end =  "")
        else:
            print(char,end = "")

texttbe = input("Enter the text to be encrypted : ")
shift = int(input("Enter the shift value : "))
decryptedtext = caesar(texttbe,shift)
