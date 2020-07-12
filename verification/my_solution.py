import bisect
from collections import defaultdict


def triangular_islands(triangles):
    squars = []
    n = 1
    while True:
        if (sq := n ** 2) > 1000000:
            break
        squars.append(sq)
        n += 1

    adj_dict = dict()
    for t in triangles:
        bl = bisect.bisect_left(squars, t)

        if bl % 2 == t % 2:
            v = t - bl * 2
        else:
            v = t + (bl + 1) * 2
        adj_nums = [t - 1, v, t + 1]

        first = bl ** 2 + 1
        last = first + bl * 2

        if t == first:
            adj_nums = adj_nums[1:]
        if t == last:
            adj_nums = adj_nums[:-1]
        adj_dict[t] = set(adj_nums)

    colors = defaultdict(int)
    rest = set(triangles)

    def set_color(triangle, c):
        stack = [triangle]
        while stack:
            num = stack.pop()
            for r_num in list(rest):
                if r_num in adj_dict[num]:
                    colors[r_num] = c
                    stack.append(r_num)
                    rest.remove(r_num)

    c = 0
    for triangle in triangles:
        if not colors[triangle]:
            c += 1
            colors[triangle] = c
            set_color(triangle, c)

    t_groups = defaultdict(list)
    for k, v in colors.items():
        t_groups[v].append(k)

    return map(len, t_groups.values())


if __name__ == '__main__':
    assert sorted(triangular_islands([1, 2, 4, 5, 10, 11, 12, 9, 14, 15, 16])) == [1, 1, 1, 4, 4]
    assert sorted(triangular_islands([1, 2, 3, 4, 5, 10, 11, 12, 9, 14, 15, 16])) == [4, 4, 4]
    assert sorted(triangular_islands([14, 22, 12])) == [1, 2]
