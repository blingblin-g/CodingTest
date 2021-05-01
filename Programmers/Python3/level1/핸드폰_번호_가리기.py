def solution(phone_number):
    phone = phone_number[-4:]
    answer = '*' * (len(phone_number) - 4) + phone
    return answer