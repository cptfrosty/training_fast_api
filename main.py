#Проект предназначен для обучающих целей для изучения:
# разработка веб-сервиса
# работа с fast api

import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host='localhost',
        port=8080,
        reload = True
    )