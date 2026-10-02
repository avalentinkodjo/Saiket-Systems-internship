import requests

# Affectation de l'URL de l' API Open-Meteo dans une variable
url = "https://api.open-meteo.com/v1/forecast"

# Création d'un dictionnaire pour stocker le information des paramètres de demande
params = {
    "latitude" : 6.1256,
    "longitude" : 1.2254,
    "current" : "temperature_2m,wind_speed_10m"
}

#Execution de la requette Get pour récupérer les informations & affectation à une variable pour récupérer les données JSON
response = requests.get(url, params=params)

#conversion des données JSON en objet Python manipulable & affectation à une variable objet
data = response.json()

#Séparation de chaque données de l'objet data
temperature = data["current"]["temperature_2m"]
wind_speed = data["current"]["wind_speed_10m"]
time = data["current"]["time"]

#Affichage de la reponse
print(" \n *** WEATHER - API ***")
print(" \t -> Localisation : Lomé")
print(" \t -> La date et l'heure actuelle est : ",time)
print(" \t -> La température à ce lieu est : ",temperature,"°C")
print(" \t -> La vitesse du vend de ce lieu est : ", wind_speed,"km/h")
