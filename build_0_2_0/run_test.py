from colorama import init, Fore

from .tests import TESTS_CLOJURE
from .interpreter import CLython

class Do_Test:
    #инициализация colorama
    init(autoreset=True)

    #настройка цветов
    good = Fore.GREEN
    bad = Fore.RED
    except_ = Fore.YELLOW
    #static = 'blue'
   
    def __init__(self) -> None:
        pass
        
    def all_tests(self):
        return TESTS_CLOJURE

    def tests(self) -> None:
        how_do_tests = []
        for name_test in TESTS_CLOJURE:
            #print(f'Выполняется тест: {name_test}')
            tests = TESTS_CLOJURE[name_test]
                
            for num, test in enumerate(tests):
                output = []
                print(f'Выполняется тест {name_test} #{num}')
                print(f'Входные данные: {test["test"]}')
                print(f'Ожидаемые выходные данные: {test["out"]}')
                try:
                    cluthon = CLython(code = test["test"])
                    output = cluthon.output
                    print(f'Выходные данные: {output}')
                    
                    if test['out'] == output:
                        print(f'{self.good}Good: Тест {name_test} #{num} - прошёл!')
                        how_do_tests.append(True)
                        
                    elif test['out'] != output:
                        print(f'{self.bad}Failed: Тест {name_test} #{num} - не прошёл!')
                        how_do_tests.append(False)
                    
                    else:
                        print(f'Они почему-то не равны!')
                        print(f'type(output): {type(output)}')
                        print(f'type(test["out"]): {type(test["out"])}')
                        
                except Exception as ex:
                    print(f'Error: {ex}')
                    how_do_tests.append('Fail')
                    print(f'{self.except_}Failed: Тест {name_test} - не прошёл!')
                print('-'*100)
                
        good_tests = sum([1 for x in how_do_tests if x == True])
        bad_tests = sum([1 for x in how_do_tests if x == False])
        error_tests = sum([1 for x in how_do_tests if x == 'Fail'])
        print(f'Количество тестов\n{self.good} Удачных: {good_tests}\n{self.bad} Неудачных: {bad_tests}\n{self.except_} Ошибок итератора: {error_tests}')

