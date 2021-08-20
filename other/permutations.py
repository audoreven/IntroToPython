length = 4
# perm = []
solution = [-1 for i in range(length)]
vis = [False for i in range(length)]
count = 0

def dfs(index:int):
    global solution, vis, length, count

    # base case
    if index >= length:
        count += 1
        print("solution:", solution)
        return

    for i in range(length):
        if not vis[i]:
            # do something
            solution[index] = i
            vis[i] = True

            # recurse
            dfs(index+1)

            # undo something
            solution[index] = -1
            vis[i] = False


dfs(0)



"""
dfs(param):
    base case --> return
    
    do something
    recurse == dfs(param)
    undo something


"""