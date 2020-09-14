import shutil
import os

# Перенесення файлів з одної папки в іншу
# shutil.move('/Users/liuk/my_repos/app_flask/flask_env/task1', '/Users/liuk/my_repos/app_flask/flask_env/task2')

# Прочитать текстовое содержимое из всех файлов каталога и объеденить его в одном файле через разделитель точка с запятой.
base_path = '/Users/liuk/my_repos/app_flask/flask_env/task2/'
lst = os.listdir(base_path)
lst_new = []
print(lst)
for file_lst in lst:
     if os.path.isdir(base_path + file_lst):
         print("Folder is {}".format(base_path + file_lst))
     else:
         lst_new.append(file_lst)
         print("File is {}".format(base_path + file_lst))


with open('textfile_1.txt', encoding='utf-8') as new_file:
     pass
 for files in lst_new:
     with open("/Users/liuk/my_repos/app_flask/flask_env/task2/task1/" + files, 'r') as num_file:
         data = num_file.read()
         print(data)
         with open('textfile_1.txt', 'a', encoding='utf-8') as new_file:
             new_file.write(data)
             new_file.write(';'+'\n')


# Есть текстовый файл вида.
#
# file1.txt, file2.txt. file3.dat, file4.log
#
# Необходимо прочитать его содержимое и создать столько же пустых файлов, которые перечислены через запятую.
with open('file_task.txt') as file_4:
     data_4 = file_4.read()
     print(data_4)
     data_lst = data_4.split(',')
     print(data_lst)
     for index_data_lst in data_lst:
         with open(index_data_lst, 'w') as index_file:
             pass