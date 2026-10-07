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
    df["data"] = df["dataHoraCotacao"].dt.date
    df = df.rename(columns={
    "cotacaoCompra": "cotacao_compra",
    "cotacaoVenda": "cotacao_venda",
})
    df = df.drop(columns="dataHoraCotacao")
    return df

if __name__ == "__main__":
    bruto = extrair()
    limpo = transformar(bruto)
    print(limpo.columns)
    print(limpo.head())
    # print(limpo[["dataHoraCotacao", "data"]].head())
    # print(limpo["data"].dtype)