# file = open("Day20_21_highscore.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("Day20_21_highscore.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("Day20_21_highscore.txt", mode="w") as file:
#     file.write("New text.")

# with open("../../Desktop/my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


import pandas
data = pandas.read_csv("Day25 US State Game/Day25_50_states.csv")
for state in data.state:
    print(state)