curso = "Python"

print(curso.center(10, "#"))

print(".".join(curso))

nome = "Claiton"
idade = 43
profissao = "Programador"
linguagem = "Python"

pessoa = {}
##  old style %

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem));

## Método format

print("Olá, me chamo {} . Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem));

## Método format com indice
print("Olá, me chamo {1} . Eu tenho {2} anos de idade, trabalho como {3} e estou matriculado no curso de {0}." .format(linguagem, nome, idade, profissao ));

## Método format nomeado
## print("Olá, me chamo {nome} . Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(linguagem=linguagem, nome=nome, idade=idade, profissao=profissao ));


## Método format nomeado
print("Olá, me chamo {nome} . Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(linguagem=linguagem, nome=nome, idade=idade, profissao=profissao ));

## Método format nomeado 2
## print("Olá, me chamo {nome} . Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa));

## Método f-string
print(f"Olá, me chamo {nome} . Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.");

## formata strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")

print(f"Valor de PI: {PI: 10.2f}")