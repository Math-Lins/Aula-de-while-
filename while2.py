alunos = int(input("Digite o número de alunos:"))
x = 1
soma = 0
while x <=alunos:
    num = float(input("Digite as notas dos alunos:"))
    soma = soma +num
    # soma+=nota
    x+=1
media = soma/alunos
print("A média da turma é:", media)
