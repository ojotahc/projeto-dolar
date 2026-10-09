import requests # chamadas para api
import pandas as pd

URL = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
    "?@dataInicial='01-01-2026'&@dataFinalCotacao='09-30-2026'"
    "&$format=json"
)

def extrair() -> pd.DataFrame:
    resposta = requests.get(URL, timeout=30)
    resposta.raise_for_status()
    dados = resposta.json()["value"]
    return pd.DataFrame(dados)

def transformar(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"])
    df["data"] = df["dataHoraCotacao"].dt.date # .dt abre o “acessador de datas” do pandas. Ele só existe em colunas do tipo datetime
    df = df.rename(columns={
        "cotacaoCompra": "cotacao_compra",
        "cotacaoVenda": "cotacao_venda",
})
    df = df.drop(columns="dataHoraCotacao")
    df = df.drop_duplicates(subset="data")
    df = df.dropna() # remove qualquer linha que tenha pelo menos um valor nulo, em qualquer coluna.
    df = df.sort_values("data") # ordena as linhas da data mais antiga para a mais nova
    df = df.reset_index(drop=True) # refaz o índice (0, 1, 2...) e descarta o antigo
    df["ano"] = pd.to_datetime(df["data"]).dt.year
    df["mes"] = pd.to_datetime(df["data"]).dt.month
    df["variacao_diaria"] = df["cotacao_venda"].pct_change() * 100
    return df

if __name__ == "__main__":
    bruto = extrair()
    limpo = transformar(bruto)
    print(bruto.shape)
    print(limpo.shape)
    
    print(limpo.head()) # mostra as 5 primeiras linhas.
    print(limpo.tail()) # mostra as 5 últimas.
    print(limpo.dtypes)

    # print(limpo.duplicated(subset="data").sum())
    # print(limpo.isna().sum())
    # print(limpo.columns)
    # print(limpo[["dataHoraCotacao", "data"]].head())
    # print(limpo["data"].dtype)

