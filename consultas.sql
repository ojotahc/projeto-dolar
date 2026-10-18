-- Consulta 1: média da cotação de venda por mês
SELECT
    ano,
    mes,
    ROUND(AVG(cotacao_venda), 4) AS media_venda
FROM cotacoes
GROUP BY ano, mes
ORDER BY ano, mes;

-- Consulta 2: maior e menor cotação no período
SELECT
    MAX(cotacao_compra) AS maior_compra,
    MIN(cotacao_compra) AS menor_compra,
    MAX(cotacao_venda) AS maior_venda,
    MIN(cotacao_venda) AS menor_venda
FROM cotacoes;

-- Consulta 3: data da maior cotação de venda
SELECT data, cotacao_venda
FROM cotacoes
ORDER BY cotacao_venda DESC
LIMIT 1;

-- Consulta 4: data da menor cotação de venda
SELECT data, cotacao_venda
FROM cotacoes
ORDER BY cotacao_venda ASC
LIMIT 1;