#variable check

#def check_valid_variable(variable):
   # if variable.startswith('_'):
   #     return True
    
   # if variable[0].isdigit():
   #     return False
    
   # if variable.startswith('@'):
   #     return False
    
   # if variable.startswith('!'):
      #  return False
    

    #return variable
#print(check_valid_variable('!@name'))

def valid_variable(variable):
    if variable.startswith['?','$','%','&','!','^']:
        return False
    #if variable.startswith('_'):
        #return True
    
    return variable
    
print(valid_variable('?hello'))








#work on later!!!!