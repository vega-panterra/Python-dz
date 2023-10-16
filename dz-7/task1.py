# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

__all__ = ['group_files']

def group_files(desired_name, digit_count, source_extension, target_extension, name_range):
    directory = os.getcwd()
    file_counter = 1

    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            original_name = filename[name_range[0]-1:name_range[1]]
            if desired_name:
                original_name += desired_name

            number = str(file_counter).zfill(digit_count)

            new_name = original_name + number + target_extension

            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

            file_counter += 1


if __name__=="__main__":
    group_files("_new", 2, ".txt", ".jpg", [3, 6])