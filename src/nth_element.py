# 求第k个最大数
def nth_element(result, left: int, kth: int, right: int, op: Callable[[int, int], bool]):
    if left == right:
        return

    pivot = random.randint(left, right)
    result[pivot], result[right] = result[right], result[pivot]
    # 三路划分（three-way partition）
    sepl = sepr = left - 1
    for i in range(left, right+1):
        if op(result[i], result[right]):
            sepr += 1
            result[sepr], result[i] = result[i], result[sepr]
            sepl += 1
            result[sepl], result[sepr] = result[sepr], result[sepl]
        elif result[i] == result[right]:
            sepr += 1
            result[sepr], result[i] = result[i], result[sepr]
    if sepl < left + kth <= sepr:
        return
    elif left + kth <= sepl:
        nth_element(result, left, kth, sepl, op)
    else:
        nth_element(result, sepr + 1, kth - (sepr - left + 1), right, op)
