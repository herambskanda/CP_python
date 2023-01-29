"""  At the beginning of time, the priests were given three poles and a stack of 64 gold disks, 
each disk a little smaller than the one beneath it. Their assignment was to transfer all 64 
disks from one of the three poles to another, with two important constraints. They could only 
move one disk at a time, and they could never place a larger disk on top of a smaller one."""

pole_1 = []
pole_2 = []
pole_3 = []

disk_count = 4
for i in range(disk_count):
    pole_1.append(disk_count-i)

print(pole_1, pole_2, pole_3)

def move_disk(from_pole, to_pole):
    a = from_pole[-1]
    from_pole.pop(-1)
    to_pole.append(a)

def recursive_move(from_pole, to_pole, inter_pole, disk_count):
    if disk_count >= 2:
        recursive_move(from_pole, inter_pole, to_pole, disk_count-1)
        move_disk(from_pole, to_pole)
        recursive_move(inter_pole, to_pole, from_pole, disk_count-1)
    else:
        move_disk(from_pole, to_pole)

recursive_move(pole_1, pole_3, pole_2, disk_count)
print(pole_1, pole_2, pole_3)