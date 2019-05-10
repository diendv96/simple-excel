from simpleexel.models import SimpleExcel

if __name__ == '__main__':
    N = int(input())
    se = SimpleExcel()
    inpt = []
    for _ in range(2*N):
        inpt.append(input())
    for line in range(0, len(inpt), 2):
        se[inpt[line]] = inpt[line+1]
    # Output
    try:
        se.__check_deps__()
    except ValueError as err:
        print(err)
        exit(0)
    print(se)

