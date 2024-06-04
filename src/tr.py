import json

turkey = [
    {
        "name": "Alanya",
        "code": "TRALY",
        "aliases": []
    },
    {
        "name": "Aliaga",
        "code": "TRALI",
        "aliases": []
    },
    {
        "name": "Ambarli",
        "code": "TRAMB",
        "aliases": []
    },
    {
        "name": "Antalya",
        "code": "TRANT",
        "aliases": []
    },
    {
        "name": "Ayvalik",
        "code": "TRAYV",
        "aliases": []
    },
    {
        "name": "Bandirma",
        "code": "TRBDM",
        "aliases": []
    },
    {
        "name": "Bodrum",
        "code": "TRBXN",
        "aliases": []
    },
    {
        "name": "Borusan",
        "code": "TRBOR",
        "aliases": []
    },
    {
        "name": "Cesme",
        "code": "TRCES",
        "aliases": []
    },
    {
        "name": "Cide",
        "code": "TRCID",
        "aliases": []
    },
    {
        "name": "Darica",
        "code": "TRDAR",
        "aliases": []
    },
    {
        "name": "Derince",
        "code": "TRDER",
        "aliases": []
    },
    {
        "name": "Dikili",
        "code": "TRDIK",
        "aliases": []
    },
    {
        "name": "Dortyol Oil Terminal",
        "code": "TRDOR",
        "aliases": []
    },
    {
        "name": "Eregli",
        "code": "TRERE",
        "aliases": []
    },
    {
        "name": "Fatsa",
        "code": "TRFAT",
        "aliases": []
    },
    {
        "name": "Fethiye",
        "code": "TRFET",
        "aliases": []
    },
    {
        "name": "Finike",
        "code": "TRFNK",
        "aliases": []
    },
    {
        "name": "Gemlik",
        "code": "TRGEM",
        "aliases": []
    },
    {
        "name": "Giresun",
        "code": "TRGIR",
        "aliases": []
    },
    {
        "name": "Gocek",
        "code": "TRGOC",
        "aliases": []
    },
    {
        "name": "Gorele",
        "code": "TRGOR",
        "aliases": []
    },
    {
        "name": "Gulluk",
        "code": "TRGLK",
        "aliases": []
    },
    {
        "name": "Haydarpasa",
        "code": "TRHAY",
        "aliases": []
    },
    {
        "name": "Hereke",
        "code": "TRHER",
        "aliases": []
    },
    {
        "name": "Hopa",
        "code": "TRHOP",
        "aliases": []
    },
    {
        "name": "Icdas Jetty",
        "code": "TRICD",
        "aliases": []
    },
    {
        "name": "Inebolu",
        "code": "TRINE",
        "aliases": []
    },
    {
        "name": "Isdemir",
        "code": "TRISD",
        "aliases": []
    },
    {
        "name": "Iskenderun",
        "code": "TRISK",
        "aliases": []
    },
    {
        "name": "Istanbul",
        "code": "TRIST",
        "aliases": []
    },
    {
        "name": "Izmir",
        "code": "TRIZM",
        "aliases": []
    },
    {
        "name": "Izmit",
        "code": "TRIZT",
        "aliases": []
    },
    {
        "name": "Karabiga",
        "code": "TRKRB",
        "aliases": []
    },
    {
        "name": "Karasu",
        "code": "TRKSP",
        "aliases": []
    },
    {
        "name": "Kumport",
        "code": "TRKUM",
        "aliases": []
    },
    {
        "name": "Kusadasi",
        "code": "TRKUS",
        "aliases": []
    },
    {
        "name": "Samsun",
        "code": "TRSSX",
        "aliases": []
    },
    {
        "name": "Tekirdag",
        "code": "TRTEK",
        "aliases": [
            "TEKIRDAGTURKIYE"
        ]
    },
]

azov = [
    {
        "name": "Azov",
        "code": "RUAZO",
        "aliases": [
            "AZOV",

        ],
    },
    {
        "name": "Berdiansk",
        "code": "UAERD",
        "aliases": [],
    },
    {
        "name": "Henichesk",
        "code": "UAHEN",
        "aliases": [],
    },
    {
        "name": "Kerch",
        "code": "UAKER",
        "aliases": [],
    },
    {
        "name": "Mariupol",
        "code": "UAMP",
        "aliases": [],
    },
    {
        "name": "Rostov-on-Don",
        "code": "RUROV",
        "aliases": [
            "ROSTOV",
            "RUROSTOV"
        ],

    },
    {
        "name": "Taganrog",
        "code": "RUTAG",
        "aliases": [],
    },
    {
        "name": "Temryuk",
        "code": "RUTMR",
        "aliases": [],

    },
    {
        "name": "Yeysk",
        "code": "RUYEY",
        "aliases": [
            "RUYEY",
            "YEYSK"
        ],
    },
    {
        "name": "Kavkaz",
        "code": "RUKZP",
        "aliases": [],
    },
    {
        "name": "Samara",
        "code": "RUKUF",
        "aliases": [],
    }
]

ru_black = [
    {
        "name": "Novorossiysk",
        "code": "RUNVS",
        "aliases": [
            "NOVOROSSIYSKRU",
            "NOVORSSIYSK"
        ],
    },
    {
        "name": "GELENDZHIK",
        "code": "RUGDZ",
        "aliases": [],
    },
]

# def check_port():
turkey_ports = []
azov_ports = []
ru_black_ports = []

for port in turkey:
    turkey_ports.append(port["name"].upper())
    turkey_ports.append(port["code"])
    turkey_ports.extend(port["aliases"])

for port in azov:
    azov_ports.append(port["name"].upper())
    azov_ports.append(port["code"])
    azov_ports.extend(port["aliases"])

for port in ru_black:
    ru_black_ports.append(port["name"].upper())
    ru_black_ports.append(port["code"])
    ru_black_ports.extend(port["aliases"])

with open("res.json", "r") as file:
    data = json.loads(file.read())

result = []

for vessel in data:
    # print(vessel)

    des = vessel["destination"].replace(" ", "")

    if des:

        if des not in turkey_ports and des not in azov_ports and des not in ru_black_ports:
            print(
                json.dumps(
                    vessel,
                    indent=3
                )
            )

        # TODO: define cluster
        if des in azov_ports:
            result.append(vessel)

print("=============>\n")
print(json.dumps(result, indent=3))
print(len(result))

# import requests
#
# url = "https://api.datalastic.com/api/v0/vessel"
#
# params = {
#     'api-key': "5b9f834b-0592-4663-96a0-b86c8465db85",
#     "mmsi": "273459590",
#
# }
# api_response = requests.get(url, params=params).json()
#
# print(json.dumps(api_response, indent=3))
