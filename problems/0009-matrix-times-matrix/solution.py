def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
            if len(a[0]) != len(b):
                return -1
            c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
                # we go through the col first
            for col in range(len(b[0])):
                    # go through row next
                for row in range(len(a)):
                        # intalize total
                    total = 0
                    for k in range(len(a[0])):
                        prod = a[row][k] * b[k][col]
                        total = total + prod
                    c[row][col] = total
            return c

