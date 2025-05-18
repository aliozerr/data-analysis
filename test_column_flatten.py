def flatten_data(tmp_key, data: dict, tmp: list):
    for key in sorted(list(data.keys())):
        if isinstance(data[key], dict):
            flatten_data(tmp_key+key+"_", data[key], tmp)
        else:
            value = data[key]
            tmp.append({tmp_key + key: value})

tmp={
        "gender": "female",
        "name": {
            "title": "Miss",
            "first": "\u0627\u0644\u0646\u0627",
            "last": "\u062c\u0639\u0641\u0631\u06cc"
        },
        "location": {
            "street": {
                "number": 3684,
                "name": "\u06a9\u0645\u06cc\u0644"
            },
            "city": "\u06a9\u0631\u062c",
            "state": "\u0633\u06cc\u0633\u062a\u0627\u0646 \u0648 \u0628\u0644\u0648\u0686\u0633\u062a\u0627\u0646",
            "country": "Iran",
            "postcode": 34411,
            "coordinates": {
                "latitude": "20.8059",
                "longitude": "6.6018"
            },
            "timezone": {
                "offset": "0:00",
                "description": "Western Europe Time, London, Lisbon, Casablanca"
            }
        },
        "email": "ln.jaafry@example.com",
        "login": {
            "uuid": "21465fe7-4f45-413e-b6d7-11e382a4e356",
            "username": "heavybutterfly185",
            "password": "spidey",
            "salt": "8svgo40y",
            "md5": "2a169a1ff8643a47512c7ee44757a052",
            "sha1": "5facc4e349c7416fe0080963fbbe984c70b4ee59",
            "sha256": "34cf1e1b442b78fd75a4691a60feb0af661f22099a6c4ea9a69078e21f0eac00"
        },
        "dob": {
            "date": "1996-10-11T04:10:56.599Z",
            "age": 28
        },
        "registered": {
            "date": "2006-05-31T16:42:13.993Z",
            "age": 18
        },
        "phone": "016-29234276",
        "cell": "0925-372-9753",
        "id": {
            "name": "",
            "value": "null"
        },
        "picture": {
            "large": "https://randomuser.me/api/portraits/women/53.jpg",
            "medium": "https://randomuser.me/api/portraits/med/women/53.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/women/53.jpg"
        },
        "nat": "IR"
    }

my_list=[]
flatten_data("",tmp,my_list)
print(my_list)