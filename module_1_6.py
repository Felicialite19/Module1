my_dict={'Ann':25,'Don':31,'Alex':40,'Rose':19}
print('Dict: ',my_dict)
print('Existing value: ',my_dict['Ann'])
my_dict['Lisa']=22
my_dict.update({'Sam':52, 'Kate':28})
Del_value=my_dict.pop('Don')
print('Not existing value: ',my_dict.get(Del_value))
print('Deleted value: ',Del_value)
print('Modified dictionary: ',my_dict)

my_set={1,2,5,'Text',5,2}
print('Set: ',my_set)
my_set.add((6,7))
my_set.discard(2)
print('Modified set: ',my_set)
