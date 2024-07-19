codigo_de_finalizacao = 1 
quantidade_pessoas_nao_gostaram = 0
quantidade_pessoas_gostaram = 0
acima_18_anos = 0
abaixo_18_anos = 0
soma_idades = 0
pessoas_sexo_feminino = 0
pessoas_sexo_masculino = 0
maiores_18_ou_sexo_masculino_e_gostaram = 0 
menores_18_sexo_feminino_e_não_gostaram = 0

while codigo_de_finalizacao != 0: 
    
    gostou = input("Você gostou dos novos produtos? Digite [Sim] ou [Não]: ")
    if gostou == 'Não': 
        quantidade_pessoas_nao_gostaram += 1
    else: 
        quantidade_pessoas_gostaram += 1  
   
    idade_pessoal = int(input("Qual a sua idade? "))
    if idade_pessoal >= 18: 
        acima_18_anos += 1 
    else:
        abaixo_18_anos += 1 

    soma_idades = soma_idades + idade_pessoal
    
    sexo = input("Qual o seu sexo? Digite [F] para feminino ou [M] para masculino: ")
    if sexo == 'F': 
        pessoas_sexo_feminino += 1
    else: 
        pessoas_sexo_masculino += 1 
    
    if idade_pessoal >= 18 and gostou != 'Não' or sexo != 'F' and gostou != 'Não': 
        maiores_18_ou_sexo_masculino_e_gostaram +=1
    
    if gostou == 'Não' and idade_pessoal < 18 and sexo == 'F': 
        menores_18_sexo_feminino_e_não_gostaram +=1
        
    codigo_de_finalizacao = int(input("Digite [1] para continuar e [0] para finalizar: "))

total_de_pessoas = acima_18_anos + abaixo_18_anos 
percentual_menores_18 = (menores_18_sexo_feminino_e_não_gostaram / total_de_pessoas) * 100
media_idades = soma_idades / total_de_pessoas 

print("O número de pessoas que gostaram dos novos produtos foi: ", quantidade_pessoas_gostaram)
print("O número de pessoas que não gostaram dos novos produtos foi: ", quantidade_pessoas_nao_gostaram)
print("O número de pessoas maiores de 18 anos inclusive pessoas do sexo masculino que gostaram foi: ", maiores_18_ou_sexo_masculino_e_gostaram)
print("O percentual de pessoas menores de 18 anos do sexo feminino que não gostaram foi: ", "%.1f" %percentual_menores_18, "%")
print("A média de idade das pessoas que responderam a pesquisa foi: ", "%.2f" %media_idades)