"""Модуль для преобразования."""
import os
import pickle
import datetime

'''Константы.'''
CURRENT_YEAR = datetime.date.today().year

__CURRENT_DIR = os.path.dirname(__file__)  # текущая директория.
__PKL_DIR = 'pkl_objects'
__DICTS_PKL = 'studio_dict.pkl'

# Словарь аниме-студии.
__studio = pickle.load(open(
    os.path.join(__CURRENT_DIR,
                 __PKL_DIR,
                 __DICTS_PKL), 'rb'))
__studio['none'] = 1000


def get_studio_value(anime_studio):
    """Возвращает числовое значение аниме-студии.

    :param
    anime_studio: аниме-студия, полученная из запроса.
    """
    try:
        return __studio[anime_studio]
    except KeyError:
        return __studio['none']
