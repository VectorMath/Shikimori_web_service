<p align="center">
  <img src="https://github.com/VectorMath/Shikimori_web_service/blob/master/docs/github_preview.png" />
</p>

# Документация.
Разработка веб-серсвиса на **Flask** для внедрение моделей машинного обучения
 * **Репозиторий проекта: https://github.com/VectorMath/Shikimori**
 * **Репозиторий с DS-частью: https://github.com/VectorMath/Shikimori_DS**

**Примечание:** на данный момент внедрена **PS-модель(Probability Success)**, предсказывающая **успешность/провал:**

 * **Успешность -** аниме будет иметь оценку **от 7 до 10 звёзд.**
 * **Провал -** аниме будет иметь оценку **меньше 7 звёзд.**
## API.

### Введение
Веб-приложение задеплоино на **PythonAnywhere:**

 * **Base url:** https://eugenezharovdeploy.pythonanywhere.com/
 * **Response:** все запросы возвращают **JSON-объект**
 
**Request**
```
  [GET] https://eugenezharovdeploy.pythonanywhere.com/
```

**Response**
```json
{
  "message": "main API-page"
}
```
 
### Получить классификацию.

**Возвращает результат модели** по классификации полученного наблюдения

* **URL:** .../classification

* **Список атрибутов:**
    * **planned:(int)** число людей, запланировавших просмотр - **ОБЯЗАТЕЛЬНЫЙ АТРИБУТ.**
    * **duration:(int)** продолжительность аниме в минутах - **ОБЯЗАТЕЛЬНЫЙ АТРИБУТ.**
    * **studio:(string)** название аниме-студии - **ОБЯЗАТЕЛЬНЫЙ АТРИБУТ.**
    * **year:(int)** год выпуска (**по умолчанию - текущий год**).
 
 #### Примеры.
 
 ------------------------
 **Request**
```
  [GET] https://eugenezharovdeploy.pythonanywhere.com/classification?planned=16000&duration=24&studio=Bones&year=2017
```

**Response**
```json
{
  "predict": "success",
  "probability": 0.89
}
```
------------------------

 **Request (без year)**
```
  [GET] https://eugenezharovdeploy.pythonanywhere.com/classification?planned=8000&duration=15&studio=Toei%20Animation
```

**Response**
```json
{
  "predict": "success",
  "probability": 0.72
}
```
------------------------

## Структура приложения.

 * **app.py -** основной код для запуска веб-приложения.
 * **classifier.py -** реализация бизнес-логики классификатора.
 * **transform.py -** константы и трансформация текстовых значений в численное.
 
 
 * **pkl_objects -** директория с архивированными pytnon-объектами.
    * **clf.pkl -** готовый классификатор.
    * **studio_dict.pkl -** словарь данных о студиях **{"название студии": числовое_значение}**
