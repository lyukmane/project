import requests


def enter():
    print('\033[33mЩоб побачити гілку Frontend натисніть - 1 ')
    print('Щоб побачити гілку Backend натисніть  - 2 \033[0m')
    while True:
        try:
            x = int(input('\033[34mВведіть число: \033[0m'))
            if x == 1 or x == 2:
                return x
        except ValueError:
            print('\033[33mВведіть 1 або 2')
        except Exception:
            print('\033[31mНекоректні дані')


def file_open():
    with open('sites.txt', 'r') as my_file:
        text_file = my_file.read()
        return text_file


def get_url(my_file, y):
    path_to_rsb = "/static/rsb.json"
    path_to_release = "/static/release.json"
    num = 33
    for line in my_file.split():
        if y == 1:
            try:
                f = requests.get("https://" + line.strip() + path_to_release)
            except ValueError:
                print('\033[31m Помилка в домені сайту')
            except Exception:
                print('\033[31m Некоректні дані')
            data_f = f.json()
            print(('{0:-<' + str(num) + '}').format(line.strip()) + "\033[0m" + " | " + '{:^}'.format(data_f['updDate']) + " | " +
                  data_f['version'] + " | " + "\033[32m" + data_f['branch'] + "\033[0m")
        elif y == 2:
            try:
                f = requests.get("https://" + line.strip() + path_to_rsb)
            except ValueError:
                print('\033[31m Помилка в домені сайту')
            except Exception:
                print('\033[31m Некоректні дані')
            data_f = f.json()
            print(
                ('{0:-<' + str(num) + '}').format(line.strip()) + " | " + '{:^}'.format(
                    data_f['deployDateUTC'][:16]) + " | " + "\033[32m" + data_f['currentBranch'] + "\033[0m")


def enter_after():
    print('Щоб побачити гілку Frontend натисніть   - 1 ')
    print('Щоб побачити гілку Backend натисніть    - 2 ')
    print('Щоб завершити роботу програми натисніть - 0 ')
    while True:
        try:
            x = int(input('Введіть число: '))
            if x == 1 or x == 2 or x == 0:
                return x
        except ValueError:
            print('Введіть 1 або 2')
        except Exception:
            print('\033[31mНекоректні дані')
