import re, csv


def get_data():
    main_data = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    with open("info_1.txt", "r", encoding="windows-1251") as f:
        for line in f.readlines():
            if re.search(main_data[0], line):
                os_prod_list.append(line.split()[2])
            if re.search(main_data[1], line):
                os_name_list.append(line.split()[2])
            if re.search(main_data[2], line):
                os_code_list.append(line.split()[2])
            if re.search(main_data[3], line):
                os_type_list.append(line.split()[2])

    with open("info_2.txt", "r", encoding="windows-1251") as f:
        for line in f.readlines():
            if re.search(main_data[0], line):
                os_prod_list.append(line.split()[2])
            if re.search(main_data[1], line):
                os_name_list.append(line.split()[2])
            if re.search(main_data[2], line):
                os_code_list.append(line.split()[2])
            if re.search(main_data[3], line):
                os_type_list.append(line.split()[2])
    with open("info_3.txt", "r", encoding="windows-1251") as f:
        for line in f.readlines():
            if re.search(main_data[0], line):
                os_prod_list.append(line.split()[2])
            if re.search(main_data[1], line):
                os_name_list.append(line.split()[2])
            if re.search(main_data[2], line):
                os_code_list.append(line.split()[2])
            if re.search(main_data[3], line):
                os_type_list.append(line.split()[2])

    with open("main_data.txt", "w", encoding="utf-8") as f:
        f.write(f"{main_data[0]} {main_data[1]} {main_data[2]} {main_data[3]} \n"  )
        lison = [os_prod_list, os_name_list, os_code_list, os_type_list]
        for number in range(3):
            f.write(f'{lison[0][number]} {lison[1][number]} {lison[2][number]} {lison[3][number]} \n')


def write_to_csv(address):
    get_data()
    with open("main_data.txt", "r", encoding="utf-8") as f:
        with open(f"{address}.csv", "w", encoding="utf-8") as f1:
            csv_file = csv.writer(f1)
            for line in f.readlines():
                csv_file.writerow(line.split())
write_to_csv("main_data")