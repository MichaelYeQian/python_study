#list in dictionary
#list 存储不同的data type很麻烦
traval_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(traval_log["France"][1])

#dictionary in a dictionary
#dictionary 存储不同的data type比较简单
traval_log = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
    "Germany": {
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
        },
}
print(traval_log["France"]["total_visits"])
print(traval_log["France"]["cities_visited"][2])

#dictionary in list  
traval_log = [
    {
        "country":"France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]
print(traval_log[0]["total_visits"])

