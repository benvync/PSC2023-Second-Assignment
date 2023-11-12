def calculate_internal_nodes(Leaves):
    return Leaves - 2

def main():
    with open('rosalind_inod.txt', 'r') as file:
        Leaves = int(file.readline().strip())

    internal_nodes = calculate_internal_nodes(Leaves)
    with open('output_inod.txt', 'w') as output_file:
        output_file.write(str(internal_nodes))

if __name__ == "__main__":
    main()
