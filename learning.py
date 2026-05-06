print ("Hello World")

'''list data type'''
l=[1,2,3,4,5] #ordered
print(l) 
print(type(l)) 
print(l[-1]) #accessing single element

#list are mutable
l.append(6) #insert element
print(l)   
l.remove(6) #remove element
print(l)

"""tuple data type"""
t=(1,2,3,"hello",True) #ordered
print(t)
print(type(t))
print(t[-1]) #accessing single element
t.append(2002) #tuple are immutable
print(t)