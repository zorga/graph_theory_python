#!/usr/bin/python

import sys
from graph import *

def main():
    q = (int(raw_input().strip()))
    assert 1 <= q <= 10
    restab = []
    for i in range(q):
        n, m = raw_input().strip().split(' ')
        n, m = int(n), int(m)
        assert 2 <= n <= 1000
        assert 1 <= m <= ((n * (n - 1)) / 2)

        g = Graph()
        
        for j in range(m):
            u, v = raw_input().strip().split(' ')
            u, v = int(u), int(v)
            assert 1 <= u <= n
            assert 1 <= v <= n
            for k in range(1, n + 1):
                g.add_vertex(str(k))
            g.add_edge((str(u), str(v)))

        s = (int(raw_input().strip()))
        assert 1 <= s <= n
        g.breadth_first_search(str(s))
        res = ""
        for v in g.vertices():
            if v != str(s):
                if g.get_vertex(str(v)).distance() == sys.maxsize:
                    res += "-1 "
                else:
                    val = g.get_vertex(str(v)).distance() * 6
                    res += str(val) + " "
        restab.append(res)

    for res in restab:
        print(res)


if __name__ == '__main__':
    main()
