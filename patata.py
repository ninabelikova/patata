def oi():
    choice = input("Encrypt enter 0, decrypt enter 1 \n")
    if choice == '0':
        key = input("key: ")
        message = input("message: ")
        print(encrypt(key, message))
    else:
        key = input("key: ")
        encrypted = input("encrypted message: ")
        print(decrypt(key, encrypted))




def encrypt(key, message):
    key_array = list(key)

    message_array = list(message)

    results = []
    mods = []


    for index, letter in enumerate(message_array):
        numba_to_add = ord(key_array[((index+1)+2)%len(key)])*len(key_array)
        result = chr((ord(message_array[index]) + numba_to_add)%95 + 32)
        results.append(result)
        mod_result = int((ord(message_array[index]) + numba_to_add)/95)
        mods.append(str(mod_result))

    resultat = ''.join(results)
    modsss = ''.join(mods)

    entire_result = resultat  + modsss

    return entire_result

def decrypt(key, Smessage):
    key_array = list(key)
    Smessage_array = Smessage[:int(len(Smessage)/2)]
    mod_array = Smessage[int(len(Smessage)/2):]
    message=[]
    for index, letter in enumerate(Smessage_array):
    #    print(ord(key_array[index])*len(key))
        message.append(chr((ord(letter)-32)+int(int(mod_array[index])*95) - ord(key_array[((index+1)+2)%len(key)])*len(key)))
    #    print(ord(letter)-32)
    #    print(int(int(mod_array[index])*95))
    #    print(ord(key_array[((index+1)+2)%len(key)])*len(key))

    return ''.join(message)




oi()
