# find max profit from a single buy and sell
# have to buy before selling, no shorting allowed

# run through examples
# ask question as a way to inform a checklist
bitcoin_prices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    # find the largest differences in value, toss out any
    # differences that result from shorting

    # if the first index is the largest value in entire array
    # then our profit is 0

    # check for the lowest price that's not the last in the array
    # buy at this price and check for the max price and sell at the
    # price. Set a buy and sell variable and compare

    # keep track of current max