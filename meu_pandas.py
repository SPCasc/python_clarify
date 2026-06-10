import pandas as pd

# Criar um dataframe com o pandas
data = {
    'Nome':['Caio', 'Guilherme', 'Carlos', 'Daniel'],
    'Idade':[25, 30, 35, 40],
    'Salario':[5000, 6000, 7000, 8000]
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print('=Conteudo do DataFrame:')
print(df)

# Selecionando uma coluna
print('\nColuna de Nome:')
print(df['Nome'])

# Filtrando linhas (exemplo: idade maior que 30)
print('\nPessoas com idade maior que 30:')
print(df[df['Idade']>30])

# Adicionando uma nova coluna
df['Imposto'] = df['Salario'] * 0.12
print("\nDataFrame com nova coluna de 'Imposto':")
print(df)

# Calculando a média do salário
mediaSalario = df['Salario'].mean()
print('\nMedia Salarial')
print(mediaSalario)

# Calculando a soma do salário
somaSalario = df['Salario'].sum()
print('n\Soma Salarial')
print(somaSalario)

# Salvando o dataframe em um arquivo CSV
df.to_csv('minha_tabela.csv', index=False)
print('\nArquivo Salvo com sucesso')



