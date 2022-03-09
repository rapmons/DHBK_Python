
from prettytable import PrettyTable
table = PrettyTable()

# table.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )
table.add_column("ho ten",["nguyen van a","nguyen van b","nguyen van c"])
table.add_column("tuoi",["30","20","50"])
table.add_column("nam sinh",["1990","1991","1992"])
table.align="l" #can le
print(table)