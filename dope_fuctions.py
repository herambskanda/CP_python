def fun(lim, s = []):
    i = 0
    s += [i]
    lim -= 1
    if i == lim:
        return(s)
    else:
        fun(lim, s)

s = []
fun(5,s)
print(s)