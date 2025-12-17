
#dictionary is a collection of key-value pairs  

capitals = {'USA': 'Washington, D.C.', 
            'France': 'Paris',
            'India' : 'New Delhi',
            'Russia' : 'Moscow'}
print(capitals['USA'])
print(capitals.get('Germany')) #None
print(capitals.keys())
print(capitals.values())
print(capitals.items())

###############################################

capitals.update({'Germany' : 'Berlin'})
capitals.update({'USA' : 'New York'})
capitals.pop('France')
print(capitals)

capitals.clear()
for key,value in capitals.items():
    print(key,value)