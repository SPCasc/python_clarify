import pandas as pd

# Dados dos funcionários
dados = {
    "Nome":['Maria','João','Marcos','Ana','Mariana'],
    "Idade":[28, 42, 31, 24, 36],
    "Cargo":['Analista','Gerente','Desenvolvedor','Estagiária','Analista'],
    "Salario":[5500, 9000, 7500, 2500, 6200]
}

# Criando o DataFrame
df = pd.DataFrame(dados)
# Exibindo o dataFrame completo:
print('=== DataFrame Completo ===')
print(df)

# Exibir apenas a coluna Cargo
print('\n=== Cargo ===')
print(df['Cargo'])

# Exibir apenas funcionários com salário maior que 6000
print('\n=== Funcionários com salário maior que 6000 ===')
print(df[df['Salario']>6000])

# Funcionários com idade menor que 35
print('\n=== Funcionários com idade maior que 35 ===')
print(df[df['Idade']>35])

# Criar uma coluna de bônus de 15%
df['Bonus'] = df['Salario'] * 0.15
print("\n=== Bonus ===")
print(df)

# Criar uma coluna de salário final (Salário+Bônus)
df['Salario Final'] = df['Salario'] + df['Bonus']
print("\n=== Salario Final ===")
print(df)

# Estatísticas
print('\n=== Estatísticas ===')
print(f"Media Salarial: R$ {df['Salario'].mean():.2f}")
print(f"Maior Salário: R$ {df['Salario'].max():.2f}")
print(f"Menor Salário: R$ {df['Salario'].min():.2f}")

# Ordenado por salário
print('\n=== Funcionários ordenados por salário ===')
print(df.sort_values(by='Salario', ascending=False))

# Quantidade por cargo
print('\n=== Quantidade por Cargo ===')
print(df['Cargo'].value_counts())

# Funcionários cujo nome começa com M
print("\n=== Funcionários com nome iniciando em 'M'===")
print(df[df['Nome'].str.startswith("M")])

# Funcionários com maior salário final
maiorSalarioFinal = df.loc[df['Salario Final'].idxmax()]
print('\n=== Funcionários com Maior Salário Final ===')
print(maiorSalarioFinal)

# Salvando em CVS
df.to_csv("funcionarios.cvs", index=False)
print('\nAqruivo "funcionario.cvs" salvo com sucesso.')