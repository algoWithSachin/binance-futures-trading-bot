import argparse
from bot.client import BinanceClient
from bot.validators import *
from bot.logger import log_info, log_error


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_type(args.type)
        validate_quantity(args.qty)
        validate_limit_price(args.type, args.price)

        client = BinanceClient()

        result = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.qty,
            price=args.price
        )

        print("\nORDER RESPONSE")
        print("-" * 40)
        print(f"Order ID     : {result.get('orderId')}")
        print(f"Symbol       : {result.get('symbol')}")
        print(f"Side         : {result.get('side')}")
        print(f"Type         : {result.get('type')}")
        print(f"Status       : {result.get('status')}")
        print(f"Qty          : {result.get('origQty')}")
        print(f"Executed Qty : {result.get('executedQty')}")
        print("-" * 40)
        log_info(
            f"ORDER PLACED | {args.symbol} | {args.side} | {args.type} | qty={args.qty} | orderId={result.get('orderId')}"
        )

    except Exception as e:
        print("ERROR:", str(e))
        log_error(
        f"ORDER FAILED | {args.symbol} | {args.side} | {args.type} | qty={args.qty} | error={str(e)}"
     )


if __name__ == "__main__":
    main()