def person(name,**data):
    print(name)
    #print(data)
    
    for i,j in data.items():
        print(i,j)

person(name='Dhanya',age=23,place='Ekm',mob=7736768188)