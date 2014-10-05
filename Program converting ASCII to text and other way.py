#Harry Robinson
#30-09-2014
#Program converting ASCII to text and other way

print("Do you want to convert an ASCII code ? (y/n)")
response = input()
if response == "y":
    ASCIINumber = int(input("Give an ASCII number"))
    ASCIINumberConverted = chr(ASCIINumber)
    print("The ASCII number is {0} in text characters.".format(ASCIINumberConverted))


if response == "n":
    print("Do you want to convert a text character? (y/n)")
    response2 = input()
    if response2 == "y":
<<<<<<< HEAD
        textNumber = input("Give text character: ")

        textNumberConverted = ord(textNumber)
        print("The ASCII code is {0}".format(textNumberConverted))

       
=======
        textNumber = int(input("Give text character"))
        textNumberConverted = ord(textNumber)
        print("Text character is {1}".format(textNumberConverted))
>>>>>>> branch 'master' of https://github.com/Jokekiller/Theory-Programmes.git
        

