#def moving(on_bridge, bridge_length):
#    passed = []
#    next_on_bridge = [0] * bridge_length
#    for i, truck in enumerate(on_bridge):
#        print("index is...", i)
#        if on_bridge[0] != 0:
#            passed.append(on_bridge[0])
#        if i < bridge_length - 1:
#            next_on_bridge[i] = on_bridge[i + 1]
#    next_on_bridge[-1] = 0
#    return next_on_bridge
        

#def solution(bridge_length, weight, truck_weights):
#    count = 0
#    on_bridge = [0] * bridge_length
#    passing = []
#    #on_bridge[-1] = truck_weights[0]
#    while truck_weights:
#        on_bridge = moving(on_bridge, bridge_length)
#        count += 1
#        if sum(on_bridge) + truck_weights[0] <= weight:
#            on_bridge[-1] = truck_weights[0]
#            passing.append(truck_weights.pop(0))
#        print("truck is ...", truck_weights)
#        print(count, ":: on_bridge :", on_bridge)
#    answer = count + bridge_length
#    return answer

def moving(on_bridge, bridge_length, on_weight):
    if on_bridge[0] != 0:
        on_weight -= on_bridge[0]
    i = 0
    next_on_bridge = on_bridge[1:]
    next_on_bridge.append(0)
    return next_on_bridge, on_weight
        

def solution(bridge_length, weight, truck_weights):
    count = 0
    on_weight = 0
    on_bridge = [0] * bridge_length
    while truck_weights:
        on_bridge, on_weight = moving(on_bridge, bridge_length, on_weight)
        count += 1
        if on_weight + truck_weights[0] <= weight:
            on_bridge[-1] = truck_weights[0]
            on_weight += truck_weights[0]
            truck_weights.pop(0)
    answer = count + bridge_length
    return answer

print(solution(2, 10, [7, 4, 5, 6]))