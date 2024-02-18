version = [number for number in input().split('.')]
filtered_version = ''.join(version)
filtered_version = int(filtered_version)
filtered_version += 1

next_version = '.'.join(str(num) for num in str(filtered_version))

print(next_version)

# next_version = [int(number) for number in input().split('.')]
# next_version[-1] += 1
#
# for index in range(len(next_version) - 1, 0, -1):
#     if next_version[index] > 9:
#         next_version[index] = 0
#         next_version[index - 1] += 1
#
# print('.'.join(str(num) for num in next_version))
