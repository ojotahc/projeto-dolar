# Pipeline ETL: Cotação do Dólar (PTAX)

Pipeline de engenharia de dados que extrai a cotação do dólar da API pública do Banco Central, trata os dados com pandas e os carrega em um banco SQLite para análise com SQL.

## Fluxo do pipeline

API do Banco Central (PTAX) → pandas (limpeza e transformação) → SQLite → consultas SQL

## Etapas

1. **Extract:** consulta a API PTAX do Banco Central com `requests` e carrega o JSON em um DataFrame.
2. **Transform:** converte datas, renomeia colunas para `snake_case`, remove duplicados e nulos, ordena por data e cria as colunas `ano`, `mes` e `variacao_diaria`.
3. **Load:** grava a tabela `cotacoes` em um banco SQLite com `to_sql`.

## Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/ojotahc/projeto-dolar.git
cd projeto-dolar
```

2. Crie e ative o ambiente virtual (Windows):

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o pipeline:

```bash
python etl.py
```

Isso cria o arquivo `cotacoes.db` na pasta do projeto.

## Análises com SQL

O arquivo `consultas.sql` reúne as consultas feitas sobre a tabela `cotacoes`:

- Média da cotação de venda por mês
- Maior e menor cotação de compra e venda no período
- Data da maior e da menor cotação de venda

## Resultados (jan a set/2026)

- Maior cotação de venda: **R$ 5,4372** em 02/01/2026
- Menor cotação de venda: **R$ 4,8973** em 11/05/2026
- Mês com menor média de venda: maio (R$ 4,9837)