def minimum_edges_to_tree(n, edges):
    m = len(edges)
    return n - 1 - m

def main():
    with open('rosalind.tree.txt', 'r') as file:
        n = int(file.readline().strip())
        edges = [tuple(map(int, line.strip().split())) for line in file]

    result = minimum_edges_to_tree(n, edges)
    with open('output_TREE.txt', 'w') as output_file:
        output_file.write(str(result))

if __name__ == "__main__":
    main()
