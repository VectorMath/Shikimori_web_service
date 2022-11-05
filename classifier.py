"""Модуль с классификатором."""
import os
import json
import pickle
import transform
import numpy as np

# Получим наш классификатор.
clf = pickle.load(open(
    os.path.join(os.path.dirname(__file__),
                 'pkl_objects',
                 'clf.pkl'), 'rb'))


def classify(planned, episode_duration, studio, year):
    """Делает классификацию наблюдения
    :parameter
    planned (int): количество людей, планирующих просмотр аниме.
    episode_duration (int): продолжительность эпизода в минутах.
    studio (str): название аниме-студии.
    year (int): год выпуска.
    """
    X = np.array([planned,
                  episode_duration,
                  transform.get_studio_value(studio),
                  year]).reshape(1, -1)
    label = {0: 'failure',
             1: 'success'}
    y = clf.predict(X)
    probability = np.round(np.max(clf.predict_proba(X)), 2)

    return json.dumps({
        'predict': label[y[0]],
        'probability': probability
    })
