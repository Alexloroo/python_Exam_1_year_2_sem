# Проект для экзамена по курсу "Введение в Python" 
Проект заключается в предикте цен на дома в Индии на основе набора данных, содержащего информацию о различных характеристиках домов и их ценах.

# Описание данных
price - Price of the Houses

area - Area of a House

bedrooms - Number of House Bedrooms

bathrooms - Number if Bathrooms

stories - Number of House Stories

mainroad - Weather connected to Main Road

guestroom - Weather has a guest room

basement - Weather has a basement

hotwaterheating - Weather has a hotwater heater

airconditioning - Weather has an airconditioning

parking - Number of House Parkings

prefarea - Prefarea of the House

furnishingstatus - Furnishing status of the House


# МЛ Сервис
Весь анализ данных, выбор модели и обучение модели были выполнены в ноутбуке ML/Analyze.ipynb. [Ноутбук](ML/Analyze.ipynb).

Запуск мл сервиса через docker-compose
```
docker-compose up ml-api --build
```
пример вызова API
```
curl -X 'POST' \
  'http://0.0.0.0:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "area": 7420,
  "bedrooms": 4,
  "bathrooms": 1,
  "stories": 2,
  "mainroad": "yes",
  "guestroom": "yes",
  "basement": "yes",
  "hotwaterheating": "yes",
  "airconditioning": "yes",
  "parking": 2,
  "prefarea": "no",
  "furnishingstatus": "furnished"
}'
```
Оутпут

```json
{
  "pred": 7185000
}
```

 ### Для установки датасета
```
make get-data 
```

Используемый датасет
https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

