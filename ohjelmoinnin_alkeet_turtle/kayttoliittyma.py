def tulosta_ohjeet():
    print('Miten haluat, että piirtoalueella liikutaan?')
    print('Eteenpäin (1)')
    print('Taaksepäin (2)')
    print('Oikealle (3)')
    print('Vasemmalle (4)')
    print('Lopetus (5)')

tulosta_ohjeet()

liikkeet = []

while True:
    valinta = int(input('Valintasi: '))
    if valinta == 5:
        print('Kiitos ja hei!')
        break
    elif valinta == 1:
        liikkeet.append('eteenpäin')
    elif valinta == 2:
        liikkeet.append('taaksepäin')
    elif valinta == 3:
        liikkeet.append('oikealle')
    elif valinta == 4:
        liikkeet.append('vasemmalle')
    else:
        print('Valinta ei kelpaa')
    
print('Kynän liikkeet ovat:')
print(liikkeet)


