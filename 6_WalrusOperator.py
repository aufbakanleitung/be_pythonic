# ctx.py

from _sqlite3 import connect

hello_list = ["hello"]

if hello_list is type(list):
    print("yes")

print(id(1))
a = 1
print(id(a))


class Temptable:
    def __init__(self, curl):
        self.cur = cur
    def __enter__(self):
        self.cur.execute('create table points(x int, y int)')
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.execute('drop table points')


with connect('test.db') as conn:
    cur = conn.cursor()
    with Temptable(cur):
        # cur.execute('create table points(x int, y int)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(3, 4)')
        cur.execute('insert into points (x, y) values(4, 5)')
        for row in cur.execute('select x, y from points'):
            print(row)
