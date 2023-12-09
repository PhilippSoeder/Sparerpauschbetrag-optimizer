from math import ceil
import argparse


def read_csv(file: str) -> list[dict]:
    result: list = []
    with open(file, mode="r", encoding="utf-8") as f:
        content = f.read()
        if len(content) == 0:
            return []
        lines: list = content.splitlines()[1:]
        for line in lines:
            d, a, p = line.split(", ")
            result.append({"date": d, "amount": float(a), "price": float(p)})
        return sorted(result, key=lambda x: x["date"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sparerpauschbetrag", type=float)
    parser.add_argument("current_price", type=float)
    args = parser.parse_args()
    OPEN_SPARERPAUSCHBETRAG: float = args.sparerpauschbetrag
    CURRENT_ETF_PRICE: float = args.current_price

    # only 70% of profits on etfs are taxed in Germany
    target_profit: float = OPEN_SPARERPAUSCHBETRAG / 70 * 100

    buys: list = read_csv("0_buys.csv")
    sells: list = read_csv("0_sells.csv")

    sum_amount_sells: float = sum([sell["amount"] for sell in sells])

    while sum_amount_sells > 0:
        if sum_amount_sells >= buys[0]["amount"]:
            sum_amount_sells -= buys[0]["amount"]
            buys.pop(0)
        else:
            buys[0]["amount"] = buys[0]["amount"] - sum_amount_sells
            sum_amount_sells = 0

    profit: float = 0
    amount_to_sell: float = 0
    total: float = 0

    # Helper variables to reduce amount_to_sell and total to next lower int
    previous_profit_share: float = 0
    previous_price_share: float = 0

    while target_profit > profit:
        profit_share: float = CURRENT_ETF_PRICE - buys[0]["price"]
        if profit_share * buys[0]["amount"] <= target_profit:
            amount_to_sell += buys[0]["amount"]
            profit += buys[0]["amount"] * profit_share
            target_profit -= buys[0]["amount"] * profit_share
            total += buys[0]["amount"] * CURRENT_ETF_PRICE
            previous_profit_share = profit_share
            previous_price_share = buys[0]["price"]
            buys.pop(0)
        else:
            diff_to_next_full_share = ceil(amount_to_sell) - amount_to_sell
            if diff_to_next_full_share * profit_share + profit < target_profit:
                amount_to_sell += diff_to_next_full_share
                target_profit -= diff_to_next_full_share * profit_share
                profit += diff_to_next_full_share * profit_share
                total += diff_to_next_full_share * CURRENT_ETF_PRICE
                amount_to_sell += int(target_profit / profit_share)
                possible = int(target_profit / profit_share)
                profit += possible * profit_share
                target_profit -= possible * profit_share
                total += possible * CURRENT_ETF_PRICE
            break

    too_much: float = amount_to_sell - int(amount_to_sell)
    amount_to_sell = int(amount_to_sell)
    profit -= too_much * previous_profit_share
    profit = round(profit, 2)
    total -= too_much * CURRENT_ETF_PRICE
    total = round(total, 2)

    print(f"Shares to sell: {amount_to_sell}")
    print(f"You will receive: {total}€")
