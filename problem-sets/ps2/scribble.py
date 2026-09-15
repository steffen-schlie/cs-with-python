import copy

old_list = [[1,2],[3,4],[5,6]]
new_list = copy.deepcopy(old_list)

old_list.append([7,8])
old_list[1][1] = 9
print(old_list)
print(new_list)