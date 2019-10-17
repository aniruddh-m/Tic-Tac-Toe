import socket

def checkValidity(a, n):
    # Check rows
    for i in range(n):
        prod = 1       
        for j in range(n):
            prod = prod*a[i][j]       
        if(prod == 8):
            return(True, 2)
        elif(prod == 1):
            return(True, 1)

    # Check columns
    for i in range(n):
        prod = 1       
        for j in range(n):
            prod = prod*a[j][i]       
        if(prod == 8):
            return(True, 2)
        elif(prod == 1):
            return(True, 1)
    
    # Check leading diagonal
    prod = 1
    for i in range(n):
        prod = prod*a[i][i]

    if(prod == 8):
        return(True, 2)
    elif(prod == 1):
        return(True, 1)
    
    # Check non leading diagonal
    prod = 1
    for i in range(n):
        prod = prod*a[i][n-1-i]
    if(prod == 8):
        return(True, 2)
    elif(prod == 1):
        return(True, 1)
    
    # If neither of the players has won the game, continue the game
    return(False)

def isEmpty(x, y, a):
    if(a[x][y] == 0):
        return(True)
    else:
        return(False)

def player_input():
    x, y = input().split()
    x = int(x)
    y = int(y)
    return(x, y)

def printGrid(a):
    for row in a:
        print(row)

def createGrid(n):
    a = []
    for _ in range(n):
        a.append([0]*n)
    return(a)

if __name__ == "__main__":
    n = 3
    grid = createGrid(n)
    printGrid(grid)

    end = False
    player = 0

    client = socket.socket()
    host_ip = '' #Enter Server IP within the single quotes
    client.connect((host_ip, 1234))


    while(not end):

        if(player == 1):
            x, y = player_input()
            empty_status = isEmpty(x, y, grid)

            if(empty_status == False):
                print("Try again")
            
            else:
                grid[x][y] = player+1
                player = (player+1)%2
                end = checkValidity(grid, n)
                printGrid(grid)
                co_ord = str(x) + " " + str(y)
                client.send(co_ord.encode('utf-8'))
        else:
            co_ord = client.recv(200)
            co_ord = co_ord.decode('utf-8')

            x, y = co_ord.split()
            x = int(x)
            y = int(y)

            grid[x][y] = player+1
            player = (player+1)%2
            end = checkValidity(grid, n)
            printGrid(grid)