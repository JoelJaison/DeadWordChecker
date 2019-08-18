def process_list(list):
    for i in range(len(list)):
        if "-" in list[i]:
            list[i] = list[i].replace("-", " ")
    return list
