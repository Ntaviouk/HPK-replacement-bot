from scraper import get_replacement
from scraper import get_date_replacement

from functions import table_format

if __name__ == "__main__":
    print(get_replacement())
    print(get_date_replacement())
    print(table_format(get_replacement()))

    for i in get_replacement():
        if len(i) != 6:
            print(i)
        print(len(i))