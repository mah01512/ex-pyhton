def calcular_media():
    
    disciplina = input("Digite o nome da disciplina: ")

    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    
    media = sum(notas) / len(notas)

     
    if media >= 7:
        condicao = "Aprovado" 
     
        condicao = "Reprovado"

    
    print(f"\nDisciplina: {disciplina}")
    print(f"Média: {media:.2f}")
    print(f"Condição: {condicao}")    
calcular_media()