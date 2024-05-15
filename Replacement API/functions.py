import tabulate


def table_format(lst):
    return tabulate.tabulate(lst, tablefmt="plain")
