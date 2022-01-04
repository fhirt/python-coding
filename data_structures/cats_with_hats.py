CAT = f"\N{CAT}"
HAT = f"\N{TOP HAT}"
cats = []
hundred = list(range(1,101))

cats.append(None)
for i in hundred:
    cats.append(False)

for i in hundred:
    next_cat = i
    while next_cat < 101:
        cats[next_cat] = not cats[next_cat]
        next_cat += i

for idx, cat in enumerate(cats):
    if idx > 0:
        print(f"#{idx}\t{CAT if cat else HAT}")