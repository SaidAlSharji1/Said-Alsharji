def spider_vs_fly(spider, fly):
    radials = "ABCDEFGH"
    sr, sl, fr, fl = spider[0], int(spider[1]), fly[0], int(fly[1])
    mid_ring = min(sl, fl) if abs(ord(sr) - ord(fr)) <= 2 or abs(ord(sr) - ord(fr)) >= 6 else 0
    answer = sr + str(sl) + "-"
    while sl > mid_ring:
        sl = sl - 1 if sl != 0 else 0
        answer += sr + str(sl) + "-"
    while sl <= fl and mid_ring != 0:
        if sr == fr:
            break
        if 6 <= abs(ord(sr) - ord(fr)):
            if sr > fr:
                sr = chr(ord(sr) + 1) if sr != 'I' else 'A'
            else:
                sr = chr(ord(sr) - 1) if sr != 'H' else '@'
        else:
            sr = chr(ord(sr) + 1) if sr < fr else chr(ord(sr) - 1)
        answer += fr + str(sl) + "-"

    while sl < fl:
        sl = sl + 1
        answer += fr + str(sl) + "-"
    return answer[:-1]

spider = "H3"
fly = "E2"
result = spider_vs_fly(spider, fly)
print(result)
