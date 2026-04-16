import yfinance as yf


def fetch_price_history(security: str, date_from: str, date_to: str):
    return yf.download(
        tickers=security,
        start=date_from,
        end=date_to,
        progress=False,
    )
