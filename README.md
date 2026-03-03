Projeto Titanic - Análise de Dados

Este projeto realiza uma análise exploratória do dataset do Titanic utilizando Python e Pandas.

1. Objetivo

Analisar quais fatores influenciaram a sobrevivência dos passageiros.

2. Tecnologias utilizadas

- Python
- Pandas
- Matplotlib

3. Análises realizadas

- Taxa geral de sobrevivência
- Sobrevivência por gênero
- Sobrevivência por classe
- Tratamento de valores nulos
- Visualização com gráficos

4.Principais Insights

- Mulheres tiveram maior taxa de sobrevivência.
- Passageiros da 1ª classe tiveram maior chance de sobreviver.
- A taxa geral de sobrevivência foi aproximadamente 38%.

Projeto Titanic - Análise Exploratória de Dados
Introdução

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (AED) utilizando a base pública do Titanic. O foco é explorar os dados, identificar padrões, tratar valores ausentes e gerar insights sobre os fatores que influenciaram a sobrevivência dos passageiros.

Carregamento de dados

O dataset foi importado utilizando a biblioteca pandas. Foram analisadas as primeiras linhas do conjunto de dados, além das informações gerais como tipos de dados, quantidade de registros e presença de valores nulos.

A base contém 891 registros e 12 colunas, incluindo informações como classe social, sexo, idade, valor da passagem e porto de embarque.

Tratamento de Dados

Durante a análise foram identificados valores nulos nas colunas Age, Cabin e Embarked.

As decisões tomadas foram:
- Remoção da coluna Cabin devido à grande quantidade de valores ausentes.
- Preenchimento dos valores nulos da coluna Age com a média das idades.
- Remoção dos registros com valores ausentes em Embarked.

Após o tratamento, o dataset passou a não conter valores nulos.

Análise Exploratória
A taxa geral de sobrevivência foi de aproximadamente 38%.

A análise por gênero mostrou que:
- Mulheres tiveram taxa de sobrevivência de aproximadamente 74%.
- Homens tiveram taxa de sobrevivência de aproximadamente 18%.

A análise por classe indicou que passageiros da primeira classe tiveram maior taxa de sobrevivência, seguidos pela segunda e terceira classe.

Esses resultados mostram que gênero e classe social influenciaram significativamente as chances de sobrevivência.

Conclusão
A análise exploratória permitiu identificar padrões relevantes no conjunto de dados do Titanic. A utilização de estatísticas descritivas, agrupamentos e visualizações gráficas possibilitou uma melhor compreensão dos fatores associados à sobrevivência.