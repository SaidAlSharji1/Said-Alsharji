from productClass import Product

def main():
    p1 = Product ("water", "drink" , 1000)
    p2 = Product ("Tv", "Electronic", 200)
    print(p1.discribtion())
    p1.discount(5)
    print(p1.discribtion())
    print(p1.get_price())
    print(p2.discribtion())
    p2.discount(20)
    print(p2.discribtion())
main()