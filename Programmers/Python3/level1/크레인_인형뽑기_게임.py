def solution(board, moves):
    result = []
    count = 0
    idx = 0
    board_len = len(board)
    for i in moves:
        for j in range(board_len):
            if board[j][i - 1] is not 0:
                result.append(board[j][i - 1])
                board[j][i - 1] = 0
                if idx > 0 and result[idx] == result[idx - 1]:
                    del result[idx]
                    del result[idx - 1]
                    count += 2
                    idx -= 2
                idx += 1
                break
    answer = count
    return answer