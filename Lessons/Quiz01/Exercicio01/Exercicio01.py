import re

senha = ""
erro = 0

senha = input("Digite sua senha: ")

if (len(senha) < 6 or len(senha) > 32):
    erro = -1
if not re.search(r'[a-z]', senha):
    erro = -1
elif not re.search(r'[A-Z]', senha):
    erro = -1
elif re.search(r'/s', senha):
    erro = -1
elif re.search(r'/W', senha):
    erro = -1
else:
    print("\nSenha válida")

if erro == -1:
    print("\nSenha invalida")

