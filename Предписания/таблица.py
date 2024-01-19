from tabulate import tabulate
table = [
    [r"$ {:.1f}\pm {:.1f}$".format (2.3564, 0.5487)],
    [r"$ {:.1f}\pm {:.1f}$".format (45.1236, 8.00021)]
]
print(tabulate(table, tablefmt="latex"))