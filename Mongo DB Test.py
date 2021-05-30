import pymongo

Client = pymongo.MongoClient('mongodb://localhost:27017/')

Database = Client['CompanyUsers']

Table = Database['Users']

Users = [
    {'_id': 945357012 , 'Name': 'Ramin', 'LastName': 'Kazemi', 'Phone': '+989011868165'},
    {'_id': 945357013 , 'Name': 'Ali', 'LastName': 'Asadi', 'Phone': '+989144267984'},
    {'_id': 945357014 , 'Name': 'Armin', 'LastName': 'Taheri', 'Phone': '+989114756287'},
    {'_id': 945357015 , 'Name': 'Amir', 'LastName': 'Akbari', 'Phone': '+989124786354'}
]

Table.insert_many(Users)