def is_inside(list_1, list_2):
    if  list_2[0] <= list_1[0] <= list_2[0] + list_2[2] and list_2[1] <= list_1[1] <= list_2[1] + list_2[3]:
        return True
    else:
        return False


check = is_inside([100, 120], [140, 60, 100, 200])
print(check)

check = is_inside([200, 120], [140, 60, 100, 200])
print(check)
