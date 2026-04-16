from unittest.mock import patch

import pandas as pd

from personal_finance.modules.securities_prices.collector import (
    PROVIDER_YAHOO,
    collect_and_print,
)


@patch("personal_finance.modules.securities_prices.collector._PROVIDER_FETCHERS")
def test_collect_and_print_calls_yahoo_provider(mock_providers):
    # arrange
    fake_df = pd.DataFrame({"price": [1, 2, 3]})
    mock_fetch = mock_providers[PROVIDER_YAHOO]
    mock_fetch.return_value = fake_df

    # act
    collect_and_print(
        security="AAPL",
        date_from="2024-01-01",
        date_to="2024-01-05",
        provider=PROVIDER_YAHOO,
    )

    # assert
    mock_fetch.assert_called_once_with(
        "AAPL",
        "2024-01-01",
        "2024-01-05",
    )
