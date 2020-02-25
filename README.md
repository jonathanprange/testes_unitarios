# testes_unitarios

# Aula 1
    # Introdução
    # 1. teste_assert.py
# Aula 2
    # 2. teste_sem_framework.py (recaptular métodos e classes)
# Aula 3
    # 3. teste_com_framework.py
    # 3.1 tests/test_com_framework.py
# Aula 4
    # 4.1 tdd_1.py e tests/test_tdd_1.py 
    # 4.2 tdd_2.py e tests/test_tdd_2.py 
    # 4.3 tdd_3.py e tests/test_tdd_3.py 
    # 4.4 tdd_4.py e tests/test_tdd_4.py 

# (mock/mock.py) Arquivo em comum para as aulas 5, 6 e 7.

# Aula 5
    # 5. mock/mock.py e tests/test_cobertura.py
# Aula 6
    # 6.1 mock/mock.py e tests/test_mock_1.py
    # 6.2 mock/mock.py e tests/test_mock_2.py
    # 6.3 mock/mock.py e tests/test_mock_3.py
    # 6.4 mock/mock.py e tests/test_mock_4.py
# Aula 7
    # 7.1 mock/mock.py e tests/test_mock_5.py
    # 7.2 exemplos_mock/exemplos_mock_1.py e tests/test_mock_6.py 
    # 7.3 exemplos_mock/exemplos_mock_2.py e tests/test_mock_7.py

# Observações:

    # Pycharm por padrão, permite que você execute cada teste através de uma interface que ele possui,
    você da play no test e pode debugar caso necessário.

    # Vscode é necessário baixar a extensão "Test Explorer UI" e após instalado, realizar a seguinte        configuração:
        aperte as teclas "Ctrl" + "shift" + "p" 
        procure por:   Python:Configure Tests
        escolha a opção:   Unittest
        escolha a opção:   .    (referente ao root directory)
        escolha a opção:   test_*.py  (ele coletará todos os arquivos que comecem com test_)
    
        Arquivos de testes e métodos de testes, por padrão iniciam com test_
        O framework unittest não entenderá como um teste, os métodos que não começarem com test_

        Após configurar, aparecerá no canto esquerdo do Vscode, um símbolo de Erlenmeyer (vulgo vidro das aulas de quimica, para fazer misturas).

        Através dele você pode rodar todos os seus testes através de um botão de player.
        Também temos um botão para debugar.

        Ou podemos também ir no método de teste que estamos querendo executar, os botões de player e debug também aparecerão lá.