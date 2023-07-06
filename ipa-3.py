'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    TO_USER = social_graph[to_member]["following"]
    FROM_USER = social_graph[from_member]["following"]
    
    if to_member in FROM_USER and from_member not in TO_USER:
        relationship = "follower"
    
    elif to_member in FROM_USER and from_member in TO_USER:
        relationship = "friends"
        
    elif to_member not in FROM_USER and from_member in TO_USER:
        relationship = "followed by"
        
    else:
        relationship = "no relationship"
        
    return str(relationship)


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    for col in range(len(board)):
        if len(set(board[a][col] for a in range(len(board)))) == 1 and board[0][col] != '--':
            return board[0][col]

    for row in board:
        if len(set(row)) == 1 and row[0] != '--':
            return row[0]

    DIA1 = [board[a][a] for a in range(len(board))]
    if len(set(DIA1)) == 1 and DIA1[0] != '--':
        return DIA1[0]

    DIA2 = [board[a][len(board)-a-1] for a in range(len(board))]
    if len(set(DIA2)) == 1 and DIA2[0] != '--':
        return DIA2[0]

    return str("NO WINNER")

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    Leg_List = list(route_map.keys())
    
    n = 0
    Index_Keys = 0
    Time = 0
    
    for keys in Leg_List:
        if first_stop not in keys[0]:
            Index_Keys = (1+Index_Keys)
        if first_stop in keys[0]:
            Index_Keys = (1+Index_Keys)
            break
            
    for keys in Leg_List[Index_Keys - 1:]:
        if second_stop in keys[1] and first_stop in keys[0]:
            Time = route_map[keys]["travel_time_mins"]
            return Time
        
        elif second_stop not in keys[1] and first_stop not in keys[0]:
            Time = Time + route_map[keys]["travel_time_mins"]
            n = n+1
        
        elif second_stop not in keys[1] and first_stop in keys[0]:
            Time = Time + route_map[keys]["travel_time_mins"]
            n = n+1
             
        else:
            Time = Time + route_map[keys]["travel_time_mins"]
            return Time
   
        
    for keys in Leg_List:
        if second_stop in keys[1] and first_stop in keys[0]:
            Time = route_map[keys]["travel_time_mins"]
            return Time
        
        elif second_stop not in keys[1] and first_stop not in keys[0]:
            Time = Time + route_map[keys]["travel_time_mins"]
            n = n+1
        
        elif second_stop not in keys[1] and first_stop in keys[0]:
            Time = Time + route_map[keys]["travel_time_mins"]
            n = n+1
             
        else:
            Time = Time + route_map[keys]["travel_time_mins"]
            return Time
