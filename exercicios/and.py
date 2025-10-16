entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

#O if só é executado se TODA a expressão for verdadeira

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")