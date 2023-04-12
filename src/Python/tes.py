import googlemaps

client = googlemaps.Client("AIzaSyBQxvm6eP0nJzHve6JaETdGqa3NfWDyDMs")

print(client.directions('-7.8100673,110.3594581','-7.752020600000001,110.4914674')[0]["overview_polyline"])