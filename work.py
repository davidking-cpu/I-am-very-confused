Autumn = ["september","october","november"]
Winter = ["december","january","feb"]
Spring = ["march","april","may"]
Summer = ["june","july","august"]

months =input("Enter the months ")

if months in Autumn:
    season = "Autumn"
elif months in Winter:
    season = "Winter"
elif months in Spring:
    season = "Spring"
elif months in Summer:
    season = "Summer"

if season:    
    print(f"the season is {season}")

if season:
    season = ''
    print('input a month please')

    
     

