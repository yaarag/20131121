import math

countries = {}

def calcDistanceFromCountry():
    file = open("cow.txt", 'r')
    myLine = ""
    index = 0
    for line in file.readlines():
        if (line[0] != '#') & (line[0:3] != 'ISO'):
            myLine = line
            #===================================================================
            # [1:] is in order to remove the space in the beginning of the word
            #===================================================================
            countries[myLine.split(';')[4][1:]] = ( ( myLine.split(';')[61][1:] , myLine.split(';')[62][1:]))
    return calcDistFromCnt('Israel')
    
#===============================================================================
# distanceFromCountry
#===============================================================================
def calcDistFromCnt(country):
    minDistance = 10000
    res_country = "none"
    for each_country in countries:
        calc_dist = setCountriesToCalcDist(country , each_country)
        if (minDistance > calc_dist) & (calc_dist > 0):
            minDistance = calc_dist
            res_country = each_country
    print minDistance
    return res_country
        
def setCountriesToCalcDist(country1, country2):  
    return distance_on_unit_sphere(float(countries[country1][0]),float(countries[country1][1]),float(countries[country2][0]),float(countries[country2][1]) )
      
def distance_on_unit_sphere(lat1, long1, lat2, long2):
    earth_radius = 6373.0
    
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # in your favorite set of units to get length.
    return arc * earth_radius  
 
 
assert calcDistanceFromCountry() == "Occupied Palestinian Territory"
 
