import copy


# get the life support rate
def get_life_support_rate(file_path):
    temp_list = list()
    temp_dict = dict()
    file = open(file_path, 'r')  # read the diagnostic file
    line_count = 0
    for line in file:
        line = line.rstrip()
        temp_list.append(line)
    ind = 0
    while len(temp_list) != 1:
        for line in temp_list:
            for i in range(len(line)):
                if str(i) not in temp_dict.keys():
                    temp_dict[str(i)] = [line[i]]
                else:
                    temp_dict[str(i)].append(line[i])
        gamma_str = ''
        epsilon_str = ''

        gamma_str += str(max(set(temp_dict[str(ind)]), key=temp_dict[str(ind)].count))
        # epsilon_str += str(min(set(temp_dict[str(ind)]), key=temp_dict[str(ind)].count))
        ox_temp = []
        for item in temp_list:
            if item[0] == gamma_str:
                ox_temp.append(item)

        # print(epsilon_str)
        if ind >= 4:
            break
        ind += 1


if __name__ == "__main__":
    life_support_rate = get_life_support_rate("../diagnostic_report")
