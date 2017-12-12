def solution(words):
    table = dict()
    for word in words:
        key = "".join(sorted(word))
        if key in table.keys():
            table[key].append(word)
        else:
            table[key] = [word]

    return table


if __name__ == "__main__":
    a = "abc"
    b = "acb"
    c = "cab"

    d = "qwe"
    e = "qew"
    f = "ewq"

    words = [a,b,c,d,e,f]
    table = solution(words)
    for key in table.keys():
        print(table[key])
