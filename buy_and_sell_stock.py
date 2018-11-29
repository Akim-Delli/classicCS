from typing import List


def calculate_max_profit(prices: List[int]) -> int:
    min_price_so_far, max_profit = float('inf'), 0.0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit


if __name__ == "__main__":
    print(calculate_max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
