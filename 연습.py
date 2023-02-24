def solution2(n, lost, reserve):
    reserve_= set(reserve)-set(lost)
    lost_= set(lost)-set(reserve)

    print(reserve_)
    print(lost_)

    for reserve in reserve_:
        front = reserve-1
        back = reserve+1
        if front in lost_:
            lost_.remove(front)
        elif back in lost_:
            lost_.remove(back)
            
    return n - len(lost_)


n = 5
lost = [2, 4]
reserve = [3]

print(solution2(n, lost, reserve)) # return 2