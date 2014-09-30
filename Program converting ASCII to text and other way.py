#Harry Robinson
#30-09-2014
#Program converting ASCII to text and other way

numberConverted = print("Do you want to convert an ASCII code or a text character? ASCII or Textcharacter")
if numberConverted == ASCII:
    ASCIINumber = chr(numberConverted)
    print("ASCII in text character is {0}".format(ASCIINumber))
if numberConverted == Textcharacter:
    textNumber = ord(numberConverted)
    print("Text number in ASCII code is {0}".format(textNumber))
    
