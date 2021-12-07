def invest(amount, rate, years):
    for year in range(years):
        amount *= (1+rate)
        print(f"year {(year+1)}: CHF {amount:.2f}")


invest(100, 0.25, 10)