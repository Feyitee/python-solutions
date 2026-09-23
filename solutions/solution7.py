
def filter_prices(prices, cutoff):
    result = []

    for price in prices:
        if price >= cutoff:
            result.append(price)

    return result



response =  {
    "model": "gpt",
    "score" : 0.92
}
response["score"]