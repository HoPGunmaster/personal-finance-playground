from personal_finance.modules.securities_prices.providers.yahoo import (
    fetch_price_history as fetch_yahoo_price_history,
)

PROVIDER_YAHOO = "yahoo"
DEFAULT_PROVIDER = PROVIDER_YAHOO

SUPPORTED_PROVIDERS = [
    PROVIDER_YAHOO,
]

_PROVIDER_FETCHERS = {
    PROVIDER_YAHOO: fetch_yahoo_price_history,
}


def collect_and_print(
    security: str,
    date_from: str,
    date_to: str,
    provider: str = DEFAULT_PROVIDER,
) -> None:
    try:
        fetcher = _PROVIDER_FETCHERS[provider]
    except KeyError:
        raise ValueError(f"Unsupported provider: {provider}") from None

    data = fetcher(security, date_from, date_to)
    print(data)
