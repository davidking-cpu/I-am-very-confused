def check_user_input():
  home_appliances = {'fridge','television','fan','cylinder','generator','laptop','air_conditioner','stablizer','bulb','land_phone'}
  
  while True:
    user_input = input('choose any home appliance of your choice ' )

    if user_input.lower() in home_appliances:
      home_appliances.remove(user_input.lower() )
      print(f'deleted {user_input.lower()}.available appliances:{home_appliances}')

    else:
      print(f'{user_input.lower()} not available.')
      if not home_appliances:
        print('home_appliance is absent')



print(check_user_input())
      
