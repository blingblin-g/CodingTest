def distance(hand, num):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    
    hand_x, hand_y = location[hand]
    num_x, num_y = location[num]

    return abs(hand_x - num_x) + abs(hand_y - num_y)

def solution(numbers, hand):
    answer = ''
    left_hand = '*'
    right_hand = '#'
    left_side = ['1', '4', '7', '*']
    middle_side = ['2', '5', '8', '0']
    right_side = ['3', '6', '9', '#']
    right_dist = 0
    left_dist = 0

    numbers = list(map(str, numbers))

    for num in numbers:
        if num in left_side:
            answer += 'L'
            left_hand = num
        elif num in right_side:
            answer += 'R'
            right_hand = num
        else:
            left_dist = distance((left_hand), num)
            right_dist = distance((right_hand), num)
            if hand == 'right':
                if left_dist < right_dist:
                    answer += 'L'
                    left_hand = num
                else:
                    answer += 'R'
                    right_hand = num
            else:
                if left_dist > right_dist:
                    answer += 'R'
                    right_hand = num
                else:
                    answer += 'L'
                    left_hand = num
    return answer
