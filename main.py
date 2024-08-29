#https://gist.github.com/lorey/079c5e178c9c9d3c30ad87df7f70491d
import sys
import os
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import signal
import numpy as np
from selenium.webdriver.common.keys import Keys
import json
import random
import pickle
import math
import pyautogui
import geopandas as gpd
from sqlalchemy import create_engine
from shapely.geometry import Point, LineString
import pandas as pd
import filter_log

from shapely.ops import nearest_points
#Файл для замены категорий зданий
excel_df = pd.read_excel(r'C:\Users\sergey.biryukov\Desktop\HAR parcer\HAR parcer\Buildings\Категории яндекс карты 2.xlsx')
layers_path = r"C:\Users\sergey.biryukov\Desktop\HAR parcer\HAR parcer\Buildings\Mega_parcer2"
#Скорость передвижения стрелки
speed_arrow = 5

start_positionY = 200
step_y = 50
#Игнор ошибок
class NullWritter:
    def write(self, txt):
        pass

def exit_program(signal, frame):
    print("Exiting program")
    sys.exit(0)

# Задайте желаемые клавиши для завершения
signal.signal(signal.SIGINT, exit_program)  # Ctrl+C на большинстве систем
def move_right(speed_arrow,step_y):
    # Переместить курсор вправо
    new_x, new_y = window_width - 100, start_positionY + (a * step_y)
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)
    print('move_right')

def move_left(speed_arrow,step_y):
    # Переместить курсор влево
    new_x, new_y = 100, start_positionY + ((a) * step_y)
    # new_x, new_y = 100, 200
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)
    print("move left")



def righr_scroll(max_iter):
    num_iter = 0
    if parity % 2 != 0:
        while num_iter < max_iter:
            new_x, new_y = window_width - 100, start_positionY + (h * step_y)
            pyautogui.moveTo(new_x, new_y, duration=2)
            # Нажимаем левую кнопку мыши если последняя строка
            print("leftclick")
            pyautogui.mouseDown()
            #если нажался дом
            try:
                close_hose = driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/aside/div/div/div[1]/div[4]/span")
                actions.click(close_hose).perform()

                print("закрыл крестик")
                pyautogui.mouseDown()
            except:
                pass

            # Переместить курсор влевоыд
            new_x, new_y = 100, start_positionY + (h * step_y)
            pyautogui.moveTo(new_x, new_y, duration=1, tween=pyautogui.easeInOutQuad)
            # Отпускаем левую кнопку мыши
            pyautogui.mouseUp()
            num_iter += 1
    else:
        while num_iter < max_iter:
            new_x, new_y = 100, start_positionY + (h * step_y)
            pyautogui.moveTo(new_x, new_y, duration=1)
            # Переместить курсор вниз
            print("left click")
            pyautogui.mouseDown()
            # Если нажался дом
            try:

                close_hose = driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div/div[1]/div[4]/span")
                actions.click(close_hose).perform()

                print("закрыл крестик")
                pyautogui.mouseDown()
            except:
                pass
            # Переместить курсор вправо
            new_x, new_y = window_width - 100, start_positionY + (h * step_y)
            pyautogui.moveTo(new_x, new_y, duration=2)
            pyautogui.mouseUp()
            num_iter += 1


def down_scroll(max_iter):
    num_iter = 0
    while num_iter < max_iter:
        new_x, new_y = 100, start_positionY + ((a) * step_y)
        pyautogui.moveTo(new_x, new_y, duration=1)
        # Переместить курсор вниз
        pyautogui.mouseDown()
        # Переместить курсор вправо
        new_x, new_y = 100, start_positionY
        pyautogui.moveTo(new_x, new_y, duration=2)
        pyautogui.mouseUp()
        num_iter += 1



def fast_moves():
    speed_arrow = 1
    pyautogui.PAUSE = 0

    # Переместить курсор лево-вверх
    new_x, new_y = 100, start_positionY + step_y
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор вправо-вверх
    new_x, new_y = window_width - 100, start_positionY + step_y
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор вниз-право
    new_x, new_y = window_width - 100, window_height - step_y- 200
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор вниз-лево
    new_x, new_y = 100, window_height - step_y- 200
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор лево-вверх
    new_x, new_y = 100, start_positionY + step_y
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор вниз-право
    new_x, new_y = window_width - 100, window_height - step_y- 200
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор вправо-вверх
    new_x, new_y = window_width - 100, start_positionY + step_y
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)

    # Переместить курсор вниз-лево
    new_x, new_y = 100, window_height - step_y - 200
    pyautogui.moveTo(new_x, new_y, duration=speed_arrow)


def screen_coor():
    # Получите текущий URL
    current_url = driver.current_url
    print(f"URL экрана {ekrans}:", current_url)

    lat_coord_ekran = float(current_url.split("=")[2].split("%2C")[0])
    long_coord_ekran = float(current_url.split("=")[2].split("%2C")[1][:-2])
    print(f"Координаты экрана {ekrans + 1}:", lat_coord_ekran, long_coord_ekran)
    return  lat_coord_ekran, long_coord_ekran

def save_in_base(gdf):
    engine = create_engine('postgresql://postgres:J3kCvwVTbp@localhost:5432/sharipovo_map')

    gdf.to_postgis('geoms', engine, if_exists='append',index_label='oid', index=True)


# make chrome log requests
capabilities = DesiredCapabilities.CHROME
options = webdriver.ChromeOptions()
options.set_capability(
            "goog:loggingPrefs", {"performance": "ALL"}
        )
driver = webdriver.Chrome(options=options)
# Игнорирование ошибок в консоли
original_stder = sys.stderr
sys.stderr=NullWritter()
# # Укажите путь к файлу gpkg с зоной для поиска
area_path = r"C:\Users\sergey.biryukov\Desktop\HAR parcer\HAR parcer\Buildings\areaOfSearch_sharipovo.gpkg"

data = gpd.read_file(area_path,driver="GPKG", encoding="utf-8")
# конец игнорирования ошибок в консоли
sys.stderr = original_stder

# Координаты полигона
bounds_data = (data.bounds)
gdf_xmin = bounds_data['minx'].values[0]
gdf_ymin = bounds_data['miny'].values[0]
gdf_xmax = bounds_data['maxx'].values[0]
gdf_ymax = bounds_data['maxy'].values[0]
print("bounds:",bounds_data)
print("Координата старта:",gdf_xmin,gdf_ymax )
print("Правый верхний угол:",gdf_xmax,gdf_ymax)
print("Правый нижний угол:",gdf_xmax,gdf_ymin)
# print(bounds_data)

#Верхняя граница полигона для выбора
left_point = Point(gdf_xmin,gdf_ymax)
right_point = Point(gdf_xmax,gdf_ymax)
right_point_gdf = gpd.GeoDataFrame(geometry=[right_point], crs='EPSG:4326')

line_poly = LineString([left_point, right_point])
linePoly_gdf = gpd.GeoDataFrame(geometry=[line_poly], crs='EPSG:4326')



# # Get the coordinates of the top-right corner
# top_right_corner = (bounds[2],bounds[3])
# print("Координата :",top_right_corner)

json_path  = os.path.join(layers_path, "last_screen.json")
if os.path.isfile(json_path):
    print("Файл Json существует.")
    with open(json_path, "r") as file:
        data = json.load(file)
        start_url = data.get("current_url")
        parity = data.get("parity")

        ekrans = data.get("ekrans")
else:
    start_url = f"https://n.maps.yandex.ru/#!/?z=18&ll={gdf_xmin}%2C{gdf_ymax}&l=nk%23sat"
    ekrans = 0

# fetch a site that does xhr requests
driver.get(start_url)
actions = ActionChains(driver)
actions.click().perform()
driver.maximize_window()

# Получение ширины окна браузера с помощью JavaScript
window_width = pyautogui.size()[0]
window_height = pyautogui.size()[1]

# window_width = driver.execute_script("return window.innerWidth;")
# window_height = driver.execute_script("return window.innerHeight;")


##Autorization
# sleep(2)
# ent_but = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[2]/a/span')
# actions.click(ent_but).perform()
# sleep(1)
# login_field = driver.find_element(By.XPATH,'//*[@id="passp-field-login"]')
# sleep(1)
# login_field.clear()
# sleep(2)
# login_field.send_keys("Doshirag2@yandex.ru")
# login_field.send_keys(Keys.ENTER)
#
# sleep(3)
# pass_input = driver.find_element(By.XPATH,'//*[@id="passp-field-passwd"]')
# pass_input.clear()
# sleep(2)
# pass_input.send_keys("1124561luk")
# sleep(2)
# pass_input.send_keys(Keys.ENTER)
# sleep(25)
# pickle.dump(driver.get_cookies(),open(f"yandex_cookies", "wb"))
for cookie in pickle.load(open(f"yandex_cookies", "rb")):
    driver.add_cookie(cookie)
sleep(2)
driver.refresh()
sleep(random.uniform(1, 2))
sleep(8)
# input_tab  = driver.find_element(By.XPATH,'//input[@placeholder="Поиск мест и адресов"]')
# input_tab.send_keys('Маршрут 5')

print("Ширина окна браузера:", window_width)


h = math.floor((window_height - start_positionY-100)/step_y)
print('h=',h)
# Установите паузу между каждым движением курсора
pyautogui.PAUSE = 1

# Отключите безопасность для предотвращения аварийного завершения программы
pyautogui.FAILSAFE = False

max_ekr_vertikal = 0
# Чётность вертикальных экранов, которая заддаёт направление для скролла
parity = 1
while max_ekr_vertikal < 150:
    max_ekr_horisontal = 0
    # Укажите новые координаты для перемещения курсора
    new_x, new_y = 0, start_positionY
    current_urls = ["1","2"]
    error_ekrans = 0
    last_features = []
    while max_ekr_horisontal < 2:
        logi = []

        if ekrans > 2 and current_urls[-1] == current_urls[-2] :
            while error_ekrans < 3:
                print(current_urls[-1] ,"\n", current_urls[-2])
                print("Экран не сдвинулся с места")
                if error_ekrans == 2:
                    exit()

                if error_ekrans == 0:
                    ekrans -= 1
                error_ekrans += 1
                continue

        error_ekrans = 0
        index_features = []
        print( index_features)
        # Плавно переместите курсор от текущих координат к новым координатам
        pyautogui.moveTo(new_x, new_y, duration=2, tween=pyautogui.easeInOutQuad)

        # Итерации возюканья по экрану
        a = 1
        # ekrans += 1
        print('ekrans',ekrans)

        # Если вдруг нажался дом - закрыть описание
        try:
            close_hose = driver.find_element(By.XPATH,
                                             "/html/body/div[1]/aside/div/div/div[1]/div[4]/span")
            actions.click(close_hose).perform()
            print("закрыл крестик")
            pyautogui.mouseDown()
        except:
            pass

        # Алгоритм, если мы в местности без зданий, чтобы быстрее прошерстить экран
        print("last features", last_features)
        if ekrans != 0 and len(last_features) > 0:
            if len(last_features) <5:
                fast_moves()
                logs_fast = filter_log.filter_log.logs_func(filter_log, driver, logi, excel_df, index_features)
                geojson_str = json.dumps(logs_fast)
                print('logs_return compl')
                # Игнор ошибок
                original_stder = sys.stderr
                sys.stderr = NullWritter()
                gdf_logs_return = gpd.read_file(geojson_str)
                sys.stderr = original_stder
                print('gdf_logs_return compl')
                num_logs_return = gdf_logs_return.shape[0]
                print('num_logs_return compl')

                if num_logs_return == 0:
                    print("на экране нет объектов, иду на следующий")
                    righr_scroll(1)
                    time.sleep(2)
                    # Игнор ошибок
                    # original_stder = sys.stderr
                    # sys.stderr = NullWritter()
                    # gdf = gpd.GeoDataFrame(columns=['id', 'name'])
                    # gdf['geometry'] = None
                    # gdf = gdf.set_geometry('geometry')
                    #
                    # file_path = rf'{layers_path}\builds_saves_{max_ekr_vertikal}_{ekrans}.gpkg'
                    # gdf.to_file(file_path,layer='имя_вашего_слоя', driver="GPKG")
                    # sys.stderr = original_stder
                    # print("count:",gdf.shape[0])
                    # Сохранить данные последнего экрана в json
                    #--------------------------------
                    current_url = driver.current_url
                    current_urls.append(current_url)
                    file_path = rf"{layers_path}\last_screen.json"  # Указание пути и имени файла
                    data = {
                        "current_url": current_url,
                        "ekrans": ekrans,
                        "parity": parity
                    }

                    with open(file_path, "w") as file:
                        json.dump(data, file)
                    #---------------------------------
                    ekrans +=1
                    continue
                else:
                    print(f"на экране {num_logs_return} объектов, остаёмся")


        #     filepath = rf'{layers_path}\builds_saves_{max_ekr_vertikal}_{ekrans - 1}.gpkg'
        #     # Игнор ошибок
        #     original_stder = sys.stderr
        #     sys.stderr = NullWritter()
        #     gdf_filepath = gpd.read_file(filepath)
        #     sys.stderr = original_stder
        #     num_objects = gdf_filepath.shape[0]
        #     print(f"Количество объектов в предыдущем экране {ekrans-1}:", num_objects)
        #     # Если количество объектов на предыдущем экране меньше 5, то считаем сколько на текущем экране
        #     if num_objects < 5:
        #         fast_moves()
        #         logs_fast = filter_log.filter_log.logs_func(filter_log, driver, logi, excel_df, index_features)
        #         geojson_str = json.dumps(logs_fast)
        #         print('logs_return compl')
        #         # Игнор ошибок
        #         original_stder = sys.stderr
        #         sys.stderr = NullWritter()
        #         gdf_logs_return = gpd.read_file(geojson_str)
        #         sys.stderr = original_stder
        #         print('gdf_logs_return compl')
        #         num_logs_return = gdf_logs_return.shape[0]
        #         print('num_logs_return compl')
        #         # Если количество объектов на предыдущем экране = 0, то переходим к следующему экрану
        #         if num_logs_return == 0:
        #             print("на экране нет объектов, иду на следующий")
        #             righr_scroll(1)
        #             time.sleep(2)
        #             # Игнор ошибок
        #             original_stder = sys.stderr
        #             sys.stderr = NullWritter()
        #             gdf = gpd.GeoDataFrame(columns=['id', 'name'])
        #             gdf['geometry'] = None
        #             gdf = gdf.set_geometry('geometry')
        #
        #             file_path = rf'{layers_path}\builds_saves_{max_ekr_vertikal}_{ekrans}.gpkg'
        #             gdf.to_file(file_path,layer='имя_вашего_слоя', driver="GPKG")
        #             sys.stderr = original_stder
        #             print("count:",gdf.shape[0])
        #             # Сохранить данные последнего экрана в json
        #             #--------------------------------
        #             current_url = driver.current_url
        #             current_urls.append(current_url)
        #             file_path = rf"{layers_path}\last_screen.json"  # Указание пути и имени файла
        #             data = {
        #                 "current_url": current_url,
        #                 "ekrans": ekrans,
        #                 "parity": parity
        #             }
        #
        #             with open(file_path, "w") as file:
        #                 json.dump(data, file)
        #             #---------------------------------
        #             ekrans +=1
        #             continue
        #         else:
        #             print(f"на экране {num_logs_return} объектов, остаёмся")
        #

        # Пока текущая итерация не доёдет до конца экрана, мы  будем возюкать
        while a <= h:
            # print("logi:",index_features)
            # Ускоряет стрелку, если вначале экрана 3 итерации подряд не попадалось объектов
            # либо если 6 раз подряд попадались одни и те же объекты
            # print("index_features[-3:]", index_features[-3:])
            print("-3",index_features[-3:],"-6,-3", index_features[-6:-3])
            if a > 1 and index_features[-2:] == index_features[-4:-2] :
                print("Одни и те же фичи, ускоряемся")
                pyautogui.PAUSE = 0
                speed_arrow = 1
                # step_y = 100
                a += 1
            else:
                pyautogui.PAUSE = 1
                speed_arrow = 4
                step_y = 50

            move_right(speed_arrow, step_y)
            print('a = ', a)


            if a < h:

                move_left(speed_arrow, step_y)


            #Если мышка прошерстила весь экран и дошла до конца вниз
            else:
                # Это чтобы когда мы дошли до последнего горизонтального экрана,
                # программа прошерстила его, а не проигнорировала
                if max_ekr_horisontal == 1:
                    pass
                else:
                    righr_scroll(1)
                    ekrans += 1
                    print("Количество экрвнов:", ekrans)
                # Получаем текущие координаты экрана и сверяем с верхней левой точкой целевого полигона
                time.sleep(2)
                lat_coord_ekran, long_coord_ekran = screen_coor()
                current_url = driver.current_url
                current_urls.append(current_url)
                file_path = rf"{layers_path}\last_screen.json"  # Указание пути и имени файла
                data = {
                    "current_url": current_url,
                    "ekrans": ekrans,
                    "parity":parity
                }

                with open(file_path, "w") as file:
                    json.dump(data, file)


                #Если экран браузера вышел за пределы заданной зоны
                if lat_coord_ekran > gdf_xmax and parity % 2 != 0:
                    print("конец горизонтальных экранов:", lat_coord_ekran > gdf_xmax)
                    max_ekr_horisontal += 1
                elif lat_coord_ekran < gdf_xmin and parity % 2 == 0:
                    print("конец горизонтальных экранов:", lat_coord_ekran < gdf_xmin)
                    max_ekr_horisontal += 1
                # После того как прошерстили последний горизонтальный экран
                if max_ekr_horisontal == 2:
                    print("Ща будет вниз")
                    down_scroll(1)
                    parity += 1
                    max_ekr_vertikal += 1
                    ekrans = 0

                    # Получаем координаты экрана и сверяем их long с последней точкой целевого полигона
                    lat_coord_ekran, long_coord_ekran = screen_coor()
                    print("Сравнение экрана и нижней точки:", long_coord_ekran, type(long_coord_ekran), gdf_ymin,
                          type(gdf_ymin))
                    if long_coord_ekran < gdf_ymin:
                        print("Экран опустился ниже заданной области, программа завершается")
                        exit()

                    print("Ща будет влево")
                    #
                    # left_scroll(ekrans)

            a += 1
            print("a=", a)


        # extract requests from logs

            logs_return = filter_log.filter_log.logs_func(filter_log,driver, logi, excel_df, index_features)

            # Преобразуйте словарь в строку с помощью json.dumps()
            geojson_str = json.dumps(logs_return)
            # print("аывавпкпы")
            # Игнор ошибок
        last_features = index_features

        original_stder = sys.stderr
        sys.stderr = NullWritter()

        gdf_geojson_data = gpd.read_file(geojson_str, driver='GeoJSON')
        # Убираем дубликаты
        gdf_geojson_data = gdf_geojson_data.drop_duplicates(subset='id')
        sys.stderr = original_stder

        # Сохраните GeoDataFrame в формате GeoPackage
        # gdf_geojson_data.to_file(rf'{layers_path}\builds_saves_{max_ekr_vertikal}_{ekrans}.gpkg', driver='GPKG')

        save_in_base(gdf_geojson_data)

            #
            # with open(rf'C:\Users\Birykov.SA\Desktop\HAR parcer\Buildings\Mega_parcer\builds_saves_{max_ekr_vertikal}_{ekrans}_Ekran.geojson', 'w') as file:
            #     json.dump(geojson_data, file, indent=2)
    # with open(r'C:\Users\Birykov.SA\Desktop\HAR parcer\Routes\stops.geojson', 'w') as file:
    #     json.dump(stops, file)
