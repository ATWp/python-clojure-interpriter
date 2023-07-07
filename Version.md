## Version
[Когда будет выпущена версия 1.0?]()
	

## Version *0.2.0*
*22.04.2022*
**Рефракторинг кода**
**Изменения**:
- Описание версий перенесено в отдельный файл
- Последовательность записи версий в файле Version.md, будет изменено на обратное. Новые версии - выше, чем старые.
- Теперь в jupyter подключаются внешние зависимости(тесты, интерпритатор) из одного модуля build
*Так что теперь можно писать на "Высшем" Lisp, когда ты пишешь на python*
- Добавлена версия, работающая из консоли(REPL)
*Версия REPL и jupyter будут совпадать всегда!*
- Запуск REPL происходит из файла run.py -> **clython.py**
- Добавлен файл [Cast CLython](https://github.com/ATWp/python-clojure-interpriter/blob/main/__docs__/Cast_CLython.md)
- [Добавлен файл оптимизаций](https://github.com/ATWp/python-clojure-interpriter/blob/main/__docs__/book/Optimizations.md)
- Теперь ошибки и недостатки программы, будут отдельно выписываться в issuess git проекта

**Количество пройденых тестов**:
*<span>Общее количество тестов</span>*: 25
*<span style="color:green">Удачных (Good)</span>*: 10
*<span style="color:red">Неудачных</span>*: 14
*<span style="color:yellow">Ошибок итератора</span>*: 1

**Release REPL 0.2.0**
[Реализация CLython в виде консольного приложения](https://github.com/ATWp/python-clojure-interpriter/releases/tag/#CLython-build-0.2.0)

**Release jupyter 0.2.0**	
[Release version 0.2.0](https://github.com/ATWp/python-clojure-interpriter/releases/tag/#CLython-build-0.2.0)


## Version *0.1.1*
*19.04.2022*
**Рефракторинг кода**
	
**Изменения**:
- Создан класс интерпритатора CLython в качестве фасада работы с кодом
- Создан класс Reserved_Functions для вызова зарезервированных функций
- Добавлены методы, позволяющие вычислять базовые математические операции
	
**Исправления**:
- Изменена структура тестов
- Исправлена функция тестирования
- Выполняется проверка выходных значений тестов
	
- Изменен парсер. Теперь символы - разделители, удаляются при парсинге
	
**Количество пройденых тестов**:
*<span style="color:green">Удачных (Good)</span>*: 10
*<span style="color:red">Неудачных</span>*: 14
*<span style="color:yellow">Ошибок итератора</span>*: 1

**Release jupyter 0.1.1**	
[Release version 0.1.1](https://github.com/ATWp/python-clojure-interpriter/releases/tag/%23CLython-jupyter-0.1.1)


### Version *0.1.0*
*15.04.2022*
Самый простой интерпритатор, написанный в jupyter

**Release jupyter 0.1.0**
[Release version 0.1.0](https://github.com/ATWp/python-clojure-interpriter/releases/tag/%23CLython-jupyter-0.1.0)


### Version *0.0.1*
*14.04.2022*
Идея и больше ничего