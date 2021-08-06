# (command, id, nickname) -> "(id에 해당하는 nickname)님이 (command)"
def solution(record):
    id_nickname = {}
    splited = [''] * len(record)
    answer = []
    for idx in range(len(record)):
        try:
            command, ID, nickname = map(str, record[idx].split())
            id_nickname[ID] = nickname
        except:
            command, ID = map(str, record[idx].split())
        splited[idx] = (command, ID)
    for cmd, Id in splited:
        if cmd == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(id_nickname[Id]))
        elif cmd == 'Leave':
            answer.append("{}님이 나갔습니다.".format(id_nickname[Id]))
        else:
            continue
    return answer
