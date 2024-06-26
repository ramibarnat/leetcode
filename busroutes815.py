from collections import deque


def busToDest(routes, source, target):
    # [[1,2,7],[3,6,7]]
    # {1: [0]}
    # {1: [0], 2: [0], 7: [0]}
    # {1: [0], 2: [0], 7: [0,1], 3:[1], 6:[1]}
    # we know the final array that we want to get to
    dic = {}
    for i, route in enumerate(routes):
        for stop in route:
            if stop in dic:
                dic[stop].append(i)
            else:
                dic[stop] = [i]

    if source not in dic or target not in dic:
            return -1
    
    queue = deque([(source, 0)])  # (bus stop, number of buses taken)
    seen = {source: None}
    while queue:
        cur_stop, num_buses = queue.popleft()
        for route_index in dic[cur_stop]:
            for stop in routes[route_index]:
                if stop == target:
                    return num_buses + 1
                elif stop not in seen:
                    seen[stop] = None
                    queue.append((stop, num_buses + 1))

            routes[route_index] = [] # this is a super smart way to avoid duplicate exploration
                
    return -1

arr = [[1,2,7],[3,6,7]]
print(busToDest(arr, 1, 7))
    