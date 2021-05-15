def solution(brown, yellow):
    answer = []
    area = (brown - 4) // 2
    for i in range(1, area):
        w, h = area - i, i
        if w * h == yellow:
            break

    answer.append(w + 2)
    answer.append(h + 2)

    return answer