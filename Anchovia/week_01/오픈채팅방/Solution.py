def solution(record):
    answer = []
    userList = {}
    
    for rec in record:
        msg = rec.split()
        if msg[0] in ['Enter', 'Change']:
            userList[msg[1]] = msg[2]
    
    for rec in record:
        msg = rec.split()
        if msg[0] == 'Enter':
            answer.append(f"{userList[msg[1]]}님이 들어왔습니다.")
        elif msg[0] == 'Leave':
            answer.append(f"{userList[msg[1]]}님이 나갔습니다.")
    
    return answer