def create_3d_array(a, b, c):
    return [[[0 for _ in range(a)] for _ in range(b)] for _ in range(c)]

def main():
    while True:
        try:
            # Read a line of input and parse dimensions
            dimensions = input().strip().split()
            if not dimensions:  # Skip empty lines
                continue
            a, b, c = map(int, dimensions)
            
            # Create and print the 3D array
            array_3d = create_3d_array(a, b, c)
            print(array_3d)
            
        except EOFError:
            break

if __name__ == "__main__":
    main()