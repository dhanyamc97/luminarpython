#define empty set()
#possible to difrent types of data
#insertion order not preserved
#duplicates not allowed
#indexing or slicing not supported in set



#st=set()
st={1,2,4,6,7,8}
print(type(st))

stt={1,2,3,"hello",10.4,True,False}


#operations -add,union
stt.add(4)
print(stt)

st3=stt.union(st)
print(st3)

#intersection

st5=stt.difference(st)
print(st5)