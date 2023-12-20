lista = [1,2,3,4,'5','hola',False]
users = [
    {
    'name':'Dany',
    'username':'dany1299',
    'email': 'daniela@gmail.com',
    },
    {
    'name':'Angela',
    'username':'angela1299',
    'email': 'angela@gmail.com',
    },
    {
    'name':'Pepe',
    'username':'pepe1299',
    'email': 'pepe@gmail.com',
    },
    {
    'name':'Angel',
    'username':'angel299',
    'email': 'angel@gmail.com',
    },
]
#print(len(lista))

for i in range (len(users)): #len para que intere de acuerdo al tamaño (for normal)
    print(users[i]['name'])
    print(users[i]['email'])

for user in users:  #for each, por cada usuario su nombre y su correo 
    print(user['name']) 
    print(user['email'])
    if user['name']=='dany1299':
        print('Es Dany')
    elif user['name']=='Angela': #else if combinado
        print('Es Angela')
    else: 
        print('Es otra persona')

#libreria con switch