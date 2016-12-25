example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

def create_data_structure(string_input):
    string = string_input.split('.')
    network ={}
    connections =[]
    games =[]
    for i in string:
        if i.find('connected')>=0:
            connections.append(i)
        elif i.find('play')>= 0:
            games.append(i)

    for i in connections:
        after_split = i.split()
        name = after_split[0]
        network[name] = {}
        name_list = []
        pos = i.find('to')
        i = i[pos+3:]
        after_split = i.split(', ')
        len_list = len(after_split)
        for i in range(0,len_list):
            name_list.append(after_split[i])
        network[name]['connections'] = name_list

    for i in games:
        after_split = i.split()
        name = after_split[0]
        pos = i.find('play')
        i = i[pos+5:]
        after_split = i.split(', ')
        len_list = len(after_split)
        play_list=[]
        for i in range(0,len_list):
            play_list.append(after_split[i])
        network[name]['games'] = play_list
        
    return network

def get_connections(network, user):
    if user in network:
        return network[user]['connections']
    else:
        return None

def get_games_liked(network,user):
    if user in network:
        return network[user]['games']
    else:
        return None
    

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B not in network[user_A]['connections']:
        network[user_A]['connections'].append(user_B)
    return network

def add_new_user(network, user, games):
    if user not in network:
        network[user] = {}
        network[user]['connections'] = []
        network[user]['games'] = games
    return network

def get_secondary_connections(network, user):
    list2nd = []
    if user not in network:
        return False
    for connection in network[user]['connections']:
        if connection in network:
            for node in network[connection]['connections']:
                if node not in list2nd:
                    list2nd.append(node)
    return list2nd

def count_common_connections(network, user_A, user_B):
    common_number = 0
    if user_A not in network or user_B not in network:
        return False
    for connection in network[user_A]['connections']:
        if connection in network[user_B]['connections']:
            common_number = common_number + 1
    return common_number

def find_path_to_friend(network, user_A, user_B, checked = None):
    path = [user_A]
    if user_A not in network or user_B not in network:
        return None
    checked = checked or []
    path = [user_A]
    checked.append(user_A)
    connections = get_connections(network, user_A)
    if user_B in connections:
        return path + [user_B]
    else:
        for connection in connections:
            if connection not in checked:
                newpath = find_path_to_friend(network, connection, user_B, checked)
                if newpath:
                    return path + newpath
    return None


net = create_data_structure(example_input)
#print get_connections(net, 'John')
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "clark")
#print get_connections(net, 'John')
add_new_user(net, "Debra", []) 
add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) 
#print get_games_liked(net, "Debra")
#print get_games_liked(net, "Nick")
#print net
#print get_secondary_connections(net, "Mercedes")
#print count_common_connections(net, "Mercedes", "John")
#print get_connections(net, "Mercedes")
#print get_connections(net, "John")
print find_path_to_friend(net, 'John', 'Robin')
