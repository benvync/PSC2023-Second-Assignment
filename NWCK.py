
def dis_tree(T, x, y):
    X = T.find(x)
    Y = T.find(y)
    t = [i for i in T[min(X, Y):max(X, Y)] if i in [')', '(', ',']]
    bracket = ''
    for i in t:
        bracket += i
    while '(,)' in bracket:
        bracket = bracket.replace('(,)', '')
    if bracket.count('(') == len(bracket):
        return len(bracket)
    elif bracket.count(')') == len(bracket):
        return len(bracket)
    elif bracket.count(',') == len(bracket):
        return 2
    else:
        return bracket.count(')') + bracket.count('(') + 2

if __name__ == '__main__':
    output_file = 'output_NWCK.txt'
    with open('rosalind_nwck.txt', 'r') as f:
        TREE = [line.strip().replace(';', '') for line in f.readlines() if len(line.strip()) > 0]

    with open(output_file, 'w') as output:
        for i in range(0, len(TREE), 2):
            T = TREE[i]
            x, y = TREE[i + 1].split(' ')
            distance = dis_tree(T, x, y)
            output.write(f"{distance} ")

    print(output_file)
