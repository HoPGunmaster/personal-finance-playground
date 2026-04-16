import argparse
from datetime import datetime

from personal_finance.modules.securities_prices.collector import (
    DEFAULT_PROVIDER,
    SUPPORTED_PROVIDERS,
    collect_and_print,
)


def valid_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid date '{value}'. Expected format YYYY-MM-DD."
        ) from None


def parse_args():
    parser = argparse.ArgumentParser(description="Personal Finance CLI")

    parser.add_argument(
        "--ticker",
        required=True,
        help="Security ticker symbol (e.g. AAPL)",
    )

    parser.add_argument(
        "--from",
        dest="date_from",
        required=True,
        type=valid_date,
        help="Start date in YYYY-MM-DD format",
    )

    parser.add_argument(
        "--to",
        dest="date_to",
        required=True,
        type=valid_date,
        help="End date in YYYY-MM-DD format",
    )

    parser.add_argument(
        "--provider",
        choices=SUPPORTED_PROVIDERS,
        default=DEFAULT_PROVIDER,
        help="Price data provider",
    )

    args = parser.parse_args()

    if args.date_from > args.date_to:
        parser.error("--from date must be earlier than or equal to --to date")

    return args


def main():
    args = parse_args()

    collect_and_print(
        security=args.ticker,
        date_from=args.date_from,
        date_to=args.date_to,
        provider=args.provider,
    )


if __name__ == "__main__":
    main()
