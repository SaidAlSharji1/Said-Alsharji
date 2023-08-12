from productClass import Product

def main():
    p1 = Product ("water", "drink" , 1000)
    print(p1.discribtion())
    p1.discount(0.005)
    print(p1.discribtion())
main()