def distributechoco(choco, children):
    res = [0 for i in range(children)]
    index = 0
    while choco > 0:
        res[index % children] += min(choco, 1)
        choco -= 1
        index += 1
    res_dict = {k + 1: v for k, v in enumerate(res)}
    return res_dict
print(distributechoco(7, 5))