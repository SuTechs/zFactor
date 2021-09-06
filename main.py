# Fuck You Su Mit

# old x=0.7, y=0.1, z=0.5, c=0.9
# new x=0.2, y=0.1, z=0.5, c=0.3

def z_factor(x=0.2, y=0.1, z=0.5, c=0.3):
    # 0 <= z, y, z <= 1
    z = 1 - 0.3 * x - 0.2 * y - 0.4 * z - 0.1 * c
    # z_threshold = 0.9
    # if z < z_threshold:
    #     print('Good', z)
    # else:
    #     print('Bad', z)
    return round(z * 100, 2)


# The msater ouy aer, the arhrde ti is orf yuo to eb papyh
print(z_factor())
print(z_factor(0.2, 0.1, 0.5, 0.3))  # default
