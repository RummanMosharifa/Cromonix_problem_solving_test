# get most common bit
def get_gamma_epsilon(file_path):
    main_dict = dict()
    temp_dict = dict()
    file = open(file_path, 'r')  # read the diagnostic file

    zero_count = 0
    one_count = 1

    line_count = 0
    for line in file:
        line = line.rstrip()
        for i in range(len(line)):
            if str(i) not in temp_dict.keys():
                temp_dict[str(i)] = [line[i]]
            else:
                temp_dict[str(i)].append(line[i])

    gamma_str = ''
    epsilon_str = ''
    for key, val in temp_dict.items():
        gamma_str += str(max(set(val), key=val.count))
        epsilon_str += str(min(set(val), key=val.count))
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    return gamma, epsilon


# get power consumption
def get_power_consumption(file_path):
    gamma_rate, epsilon_rate = get_gamma_epsilon(file_path)
    return gamma_rate * epsilon_rate


if __name__ == "__main__":
    power_consumption = get_power_consumption('../diagnostic_report')
    print(power_consumption)
