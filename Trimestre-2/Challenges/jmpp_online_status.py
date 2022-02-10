def online_count(dic):
    salida = 0
    for elem in dic:
        if dic[elem] == 'online':
            salida += 1
    return salida

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))