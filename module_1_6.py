my_dict = {'Nadya':2000,'Sasha':2001,'Veronika':2008,'Makar':2013,'Polina':2020}
print(my_dict)
print(my_dict['Nadya'])
my_dict['Vasia']=1983
print(my_dict['Vasia'])
my_dict.update({'Max':2010,'Egor':2015})
print(my_dict)
a=my_dict.pop('Max')
print(a)
print(my_dict)

my_set={1,2,1,2,1}
print(my_set)
my_set.add(3)
my_set.add(4)
my_set.discard(1)
print(my_set)
