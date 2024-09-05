immutable_var=1,5,'data',True
print('Immutable tuple: ',immutable_var)
#immutable_var[0]=2 //значения внури кортежа неизменяемы, и назначаются единожды
#print(immutable_var)
mutable_list=[12,'a','c']
mutable_list[2]='Modified'
print('Mutable list: ',mutable_list)