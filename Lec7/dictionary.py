#chuangjian dictionary
prog_dictionary = {
    "Bug" : "program error" , 
    #key     value
    "loop" :"do something iteratively"
}

#calling
print(prog_dictionary["Bug"]) 

#modification
prog_dictionary["Bug"] = "cuowu"
print(prog_dictionary["Bug"])

#add
prog_dictionary["function"] = "y=kx"
print(prog_dictionary)

#clean wipe
prog_dictionary={}
print(prog_dictionary)



