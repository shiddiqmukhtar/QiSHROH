data={"fn":"Mukhtar",
    "ln":"Shiddiq",
    "addres":"Makassar",
    "age":50,
    "hobby":[
        "ngaji",
        "coding"],
    "sun":{
        "tapa":{
            1:"khadijah",
            2:"hafsah",
            3:None},
        "takim":{
            1:"rayyan",
            2:"ruqayyah",
            3:"ranya"},
        "lia":{
            1:None,
            2:None,
            3:None}
    }
}

#print(data)
print(data["sun"]["lia"][2]) 
print(data["sun"]["tapa"][1], data["addres"])
for k, v in data.items():
    print(k + ':' + str(v))