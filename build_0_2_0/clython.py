import sys
from colorama import init, Fore

from .interpreter import CLython
from .run_test import Do_Test


#инициализация colorama
init(autoreset=True)

#версия clython
VERSION = '0.2.0'

#настройка цвета
GOOD = 'green'


def main(list_args) -> None:
    #это уже не нужно, потому что все будет запускаться
    #через PATH - А значит будем принимать
    '''
    -version
    -REPL Запуск обработки кода через консольный режим

    #запуск файла на выполнение через консоль
    $name_clython_repl <name_file>.clp

    #запуск исполняемого файла из директории
    $name_clython_repl <name_dir> <name_start_file>.clp
    
    #запуск через директорию в которой есть project.clp или .clj или .json
    #программе его придется найти самостоятельно - будет запущен default командой
    #если программа его не найдет, вылетит ошибка
    $name_clython_repl <name_dir>

    #такой же запуск, что и выше, только на выполнение команды заданной в файл
    $name_clython_repl <name_dir> <command>


    #Менеджер пакетов - PipeLine DeadLine
    умеет устанавливать данный язык программирования
    + контролировать разные версии языков программирования
    '''
    
    if len(list_args) == 0:
    
        #запускаем REPL
        command = ''
        print('Запущена REPL оболочка языка программирования CLython')
        print('Чтобы прочитать Справку = Документацию введите help')
        print('Чтобы завершить работу введите quit')
        while True:
            print(f'{Fore.GREEN}$:>', end='')
            code = input()
            if code == 'quit':
                break;
            else:
                try:
                    CLython(code = code);
                except Exception as ex:
                    print(f'Ошибка: {ex=}')
    
    #получение текущей версии clython интерпритатора
    elif 'version' in list_args or 'ver' in list_args or 'v' in list_args or '-ver' in list_args or '-v' in list_args:
        print(f'Vesion CLython is: {VERSION}')
    
    #получение справки по языку  
    elif 'help' in list_args:
        print('Help')
    
    #запуск проверки интерпритатора тестами    
    elif 'test' in list_args:
        print('test')
        test = Do_Test().tests()
        
    #вывод всех доступных тестов    
    elif 'all_tests' in list_args:
        print('tests')
        test = Do_Test().all_tests()
        print(f'TESTS:\n{test}')
    
    #чтение и работа с файлом
    elif len(list_args) == 1:
        #считываем файл и запускаем его в интерпритаторе
        pass

    
    
    

if __name__ == '__main__':
    
    
    #получаем все передаваемые из консоли параметры
    new_list = sys.argv
    #print(f'type: {type(new_list)}')
    print(f'value: {new_list=}')
    print(f'length: {len(new_list)}')
    
    main(new_list[1:])
    
    