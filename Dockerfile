# Какой язык программирования
FROM python:latest


# Копирование всех файлов во внутрь контейнера
COPY . /code

WORKDIR /code

# Установка библиотек
RUN pip install -r requirements.txt


# Запуск проекта
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]

# 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

