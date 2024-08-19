#creating a dictionary with visited countries

travelLog = [
{
    "country" : "France",
    "visits" : 12,
    "cities" : ["Paris", "Lille", "Dijon"]
},
{
    "country" : "Germany",
    "visits" : 5,
    "cities" : ["Berlin", "Hamburg", "Stuttgart"]
}
]

def addNewCountry(country,times,citiesVisited):
    travelBlog = {}
    travelBlog["country"] = country
    travelBlog["visits"] = times
    travelBlog["cities"] = citiesVisited
    travelLog.append(travelBlog)

addNewCountry("Russia",2,["Moscow", "Saint Petersburg"])
print(travelLog)
