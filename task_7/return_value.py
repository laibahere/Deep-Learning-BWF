#8-6
def city_country(city,country):
 return(f"{city}, {country}")

print(city_country('Paris','France'))
print(city_country('New York','USA'))
print(city_country('Sydney','Australia'))

#8-7
def make_album(artist, album_title, num_tracks=None):
 album = {'artist': artist, 'title': album_title}
 if num_tracks:
  album['tracks'] = num_tracks
  return album

album1 = make_album('Michael Jackson', 'Thriller')
album2 = make_album('Queen', 'A Night at the Opera', 12)
album3 = make_album('Led Zeppelin', 'IV', 8)

print(album1)
print(album2)
print(album3)

#8-8
while True:
 print("\nEnter an album's artist and title or enter 'q' to quit:")
 artist = input("Artist: ")
 if artist == 'q':
  break
title = input("Title: ")
album = make_album(artist, title)
print(album)