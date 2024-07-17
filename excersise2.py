#def check_data_type():
   # lst = [1,2, 'fool']
   # for mylist in lst:
       # if type(mylist)== str or type(mylist)== float or type(mylist)==bool or type(mylist) == int:
      #      return 'list contains mixed data types'
      #  else:
            #return type(mylist)
        
#print(check_data_type())


def same_data_types():
    lst = ['Beat','Run','fly',1]
    for my_list in lst:
        if type(my_list)== str or type(my_list)== int:
            return 'list is a string'
        else:
            return 'list is not a string'
        
    print(same_data_types())