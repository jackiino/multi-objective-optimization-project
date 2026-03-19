from tabulate import tabulate
from IPython.display import HTML, display

a_list = [
    ["Resource", "Profit", "Working hours", "raw material", "pollution"],
    ["P1", 10, 4, 3, 7],
    ["P2", 6, 3, 2, 4, ],
    ["P3", 4, 2, 1, 3]
]

table = tabulate(
    a_list,
    tablefmt='html',
    headers='firstrow'
)

display(HTML(table))