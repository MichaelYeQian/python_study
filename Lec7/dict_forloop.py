
prog_dictionary = {
    "Bug" : "program error" , 
    #key     value
    "loop" :"do something iteratively"
}

#only print "key"
for key in prog_dictionary:
    print(key)

#if want to print the value : print(dictionary[key])
for key in prog_dictionary:
    print(prog_dictionary[key])
