# Этот репо создан для прохождения на стажировку.

S_triangile_circle - библиотека/модуль для нахождения площади круга по радиусу и площади треугольника по 3-ём сторонам. Также, треугольник проверяется на то: прямоугольный ли он или нет и существует ли он впринципе.

pyspark_task - модуль, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий. 

Тесты для S_triangile_circle лежат в test_S_triangile_circle и активируются командой в терминале: pytest test_S_triangile_circle.py

Тесты для pyspark_task лежат в test_pyspark_task и активируются командой в терминале: pytest test_pyspark_task.py

> [!NOTE]
> Для запуска test_pyspark_task требуется 11 java

## Как скачать репо: 
1. ```git clone https://github.com/Verper1/for_internship.git```
2. ```uv sync```
3. ```pytest```