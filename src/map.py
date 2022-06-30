""""
https://www.udemy.com/course/the-python-mega-course/learn/lecture/7221278#overview
lecture 130
"""

import folium
import time
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"dir_path:{dir_path}")


def func_test():
    map = folium.Map(location=[-21.80158482316849, -54.54833021801829], )  # zoom_start=6)
    #  latitude [-90,90] and longitude [-180,180]
    map.save(f"{dir_path}/map.html")
    # map.save(f"{dir_path}/map{int(time.time())}.html")


if __name__ == "__main__":
    func_test()
