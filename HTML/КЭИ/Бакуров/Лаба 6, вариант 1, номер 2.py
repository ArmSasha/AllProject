city = tuple(input().split())
if 'Москва' not in city:
    city = city + ('Москва', )
print(*city)