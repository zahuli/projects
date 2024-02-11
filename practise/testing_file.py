# # for i in range(6):
# #     print(i)

# # x = -5
# # print(type(str(x)))
# # print(len(str(x)))

# # print(9/2)

# roms = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# # print(type(roms["X"]))

# a = [1, 2, 3, 4]

# notValid = {"(}", "(]", "{)", "{]", "[)", "[}"}

# counts = {
#     "(": 0,
#     ")": 0,
#     "{": 0,
#     "}": 0,
#     "[": 0,
#     "]": 0
# }

# s = "[(([{{{}}}])))"

# for i in s:
#     counts[i] += 1

# # print(counts)

# if counts["("] == counts[")"] and counts["{"] == counts["}"] and counts["["] == counts["]"]:
#     print("ok")


# po = ["("]
# print(po[-1])

# po.append("[")
# po.append("[")
# po.append("[")

# print(po)

# if po[-1] in {"{", "("}:
#     print("da")


gridSize = 9

for row in range(0, 9):
    if (row == 3) or (row == 6):
        print("---------------------")
    for col in range(0, 9):
        if (col == 3) or (col == 6):
            print("|", end=" ")
        print(0, end=" ")

    print()

l = [1, 2]

for item in range(1, len(l)):
    print(l[item])
