mydict = {
          "programming" : "the prcocess or activity of writing computer programs",
           "hardware" : "physical components of a computer",
           "software" : "collection of instructions that tell a computer how to work",
            "rufaida" : " meaning of rufaida is support",
             "rimsha" : "meaning of rimsha is flowers"
        }
inputz = input("enter the word :")

# if inputz in mydict.keys():
#     print(mydict[inputz])
# else:
#     print("there is no such thing")

print(mydict[inputz]) if inputz in mydict.keys() else print("there is no such word in dict")