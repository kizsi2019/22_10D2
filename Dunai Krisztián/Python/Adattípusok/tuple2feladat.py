def find_max_min_green(r, g, b):
    max_comp = max(r, g, b)
    min_comp = min(r, g, b)
    if g > 0:
        has_green = True
    else:
        has_green = False
    return (has_green, max_comp, min_comp)

def main():
    r = int(input("Enter the red component: "))
    g = int(input("Enter the green component: "))
    b = int(input("Enter the blue component: "))
    has_green, max_comp, min_comp = find_max_min_green(r, g, b)
    if has_green:
        print("The color contains green component")
    else:
        print("The color does not contain green component")
    print("The maximum component is:", max_comp)
    print("The minimum component is:", min_comp)

if __name__ == "__main__":
    main()
