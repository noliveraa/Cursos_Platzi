import requests

APIPlatzi = "https://api.escuelajs.co/api/v1/categories"

def get_categories():
    r=requests.get(APIPlatzi)
    print(r.status_code) #200
    print(r.text) # [{"id":1,"name":"Clothes","image":"https://picsum.photos/640/640?r=4389","creationAt":"2023-08-09T15:52:23.000Z","updatedAt":"2023-08-09T15:52:23.000Z"},{"id":2,"name":"Electronics","image":"https://picsum.photos/640/640?r=7765","creationAt":"2023-08-09T15:52:23.000Z","updatedAt":"2023-08-09T15:52:23.000Z"},{"id":3,"name":"Furniture","image":"https://picsum.photos/640/640?r=405","creationAt":"2023-08-09T15:52:23.000Z","updatedAt":"2023-08-09T15:52:23.000Z"},{"id":4,"name":"Shoes","image":"https://picsum.photos/640/640?r=640","creationAt":"2023-08-09T15:52:23.000Z","updatedAt":"2023-08-09T15:52:23.000Z"},{"id":5,"name":"Others","image":"https://picsum.photos/640/640?r=2813","creationAt":"2023-08-09T15:52:23.000Z","updatedAt":"2023-08-09T15:52:23.000Z"}]
    categories = r.json() #convierto ese texto que traigo en formato json
    for category in categories: #extraigo lo que se requiere en este caso los nombres de las categorias
        print(category['name'])

get_categories()