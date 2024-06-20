import requests
 
global get_phone
get_phone = input( '[+] Phone : ' )
 
def check():
    pass
 
def info():
    response = requests.get( f'https://htmlweb.ru/geo/api.php?json&telcod={ get_phone }' )
 
    user_country = response.json()[ 'country' ][ 'english' ]
    user_id = response.json()[ 'country' ][ 'id' ]
    user_location = response.json()[ 'country' ][ 'location' ]
    user_city = response.json()[ 'capital' ][ 'english' ]
    user_width = response.json()[ 'capital' ][ 'latitude' ]
    user_lenth = response.json()[ 'capital' ][ 'longitude' ]
    user_post = response.json()[ 'capital' ][ 'post' ]
    user_oper = response.json()[ '0' ][ 'oper' ]
 
    global all_info
    all_info = f'\nCountry : { user_country }\nID : { user_id }\nLocation : { user_location }\nCity : { user_city }\nLatitude : { user_width }\nLongitude : { user_lenth }\nIndex post : { user_post }\nOperator : { user_oper }'
 
    print( all_info )
 
def record():
    user_record = input( '\n[?] Record(y/n) : ' )
 
    if user_record == 'y':
        file = open( 'data_phone.txt', 'a' )
        file.write( f'{ all_info }\n' )
        file.close()
 
    if user_record == 'n':
        print( '\n<O.K>' )
 
def main():
    info()
    record()
 
main()