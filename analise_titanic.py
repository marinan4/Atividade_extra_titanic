# Importando bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando dataset
# Leitura do arquivo csv titanic

df = pd.read_csv("data/titanic_dataset.csv")

# Visualização das primeiras linhas
print(df.head())

# Informações gerais do dataset
print(df.info())

# Estatísticas descritivas
print(df.describe())


# Verificaçáo dos valores nulos 
print(df.isnull().sum())

# Tratamento de valores nulos

# Remover coluna Cabin (muitos valores nulos)
df.drop(columns=["Cabin"], inplace=True)

# Preencher valores nulos da idade com a média
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remover registros com Embarked nulo
df.dropna(subset=["Embarked"], inplace=True)

# Conferir valores nulos após tratamento
print("Valores nulos após tratamento:")
print(df.isnull().sum())

#Análise

# Taxa geral de sobrevivência
taxa_sobrevivencia = df["Survived"].mean()
print("Taxa geral de sobrevivência:", taxa_sobrevivencia)

# Sobrevivência por genêro
sobrevivencia_genero = df.groupby("Sex")["Survived"].mean()
print("Sobrevivência por genêro:")
print(sobrevivencia_genero)

# Sobrevivência por classe
sobrevivencia_classe = df.groupby("Pclass")["Survived"].mean()
print("Sobrevivência por classe:")
print(sobrevivencia_classe)

#Visualizações em grafico

print("Taxa de sobrevivência por classe e sexo:")
print(df.groupby(["Pclass", "Sex"])["Survived"].mean())

df.groupby(["Pclass", "Sex"])["Survived"].mean().unstack().plot(kind="bar")

plt.title("Sobrevivência por Classe e Sexo")
plt.ylabel("Taxa de Sobrevivência")
plt.xlabel("Classe")
plt.show()
