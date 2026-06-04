tipoEscola = input("Tipo da Escola: \n [1]Publico \n [2]Particular \nR: ")
mediaAluno = input("Qual a media do aluno? \nR: ")
freqAluno = input("Qual a frequencia do aluno? \nR: ")
mediaAluno = int(mediaAluno)
freqAluno = int(freqAluno)




if tipoEscola == "2" :
    print("------ ESCOLA PARTICULAR Etapa -------------")
    if mediaAluno >= 7 and freqAluno >= 70 :
        print("Aprovado")
    else :
        print("Reprovado")

if tipoEscola == "1" :
    print("-------- ESCOLA PÚBLICA ETEC --------------")
    if mediaAluno >= 7 and freqAluno >=70 :
        print("Aprovado")
    else :
        print("Reprovado")

print("Fim da aplicação")

