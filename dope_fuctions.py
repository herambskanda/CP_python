def unique_factors(root_number, fac_list, prefix:list = []): # except itself
    for i in range(2,root_number):
        if root_number%i == 0:
            prefix += [i]
            x = prefix+[int(root_number/i)]
            x.sort(reverse=True)
            duplicate = False
            for y in fac_list:
                if y == x: 
                    duplicate = True
            if not duplicate:
                fac_list.append(x)
            unique_factors(int(root_number/i), fac_list, prefix )
    if len(prefix) > 0:
        print("---")
        prefix.pop(-1)

def all_factors(root_number, fac_list, prefix:list = []):#except itself
    for i in range(2,root_number):
        if root_number%i == 0:
            prefix += [i]
            x = prefix+[int(root_number/i)]
            fac_list.append(x)
            all_factors(int(root_number/i), fac_list, prefix )
    if len(prefix) > 0:
        print("---")
        prefix.pop(-1)
