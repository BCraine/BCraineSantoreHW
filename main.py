def main():
    state_tax_massachusetts = .0625
    state_tax_new_hampshire = 0
    state_tax_maine = .0550

    wic_eligible_food = ["Cereal: $2.99", "Vegetables: $1.49", "Juice: $3.29", "Milk: $4.05", "Cheese: $ 0.89",
                         "Meat: $8.69", "Fruit: $0.49", "Bread: $2.00", "Water: $1.99", "Soda: $3.50"]
    wic_prices = [2.99, 1.49, 3.29, 4.05, 0.89, 8.69, 0.49, 2.00, 1.99, 3.50]

    clothing = ["Shirt: $14.99", "Pants: $24.05", "Shoes: $49.99"]
    clothing_prices = [14.99, 24.05, 49.99]

    everything_else = ["Toothbrush: $0.99", "Toothpaste: $1.99", "Deodorant: $0.99",
                       "Shampoo: $4.99", "Conditioner: $4.99"]
    e_e_prices = [0.99, 1.99, 0.99, 4.99, 4.99]

    state = input("Please enter a state to do business in.\n"
                  "You may pick between Massachusetts, New Hampshire, or Maine\n")

    print(wic_eligible_food)
    print(clothing)
    print(everything_else)

    items = ""
    price = 0
    total = 0
    while items != "done":
        items = input("Please enter items you would like to buy from above\n"
                      "Enter item twice if you have two of same thing and so forth\n"
                      "Enter 'done' when finished ")
        if items.lower() == "cereal":
            price += wic_prices[0]
            print("$", price)
        if items.lower() == "vegetables":
            price += wic_prices[1]
            print("$", price)
        if items.lower() == "juice":
            price += wic_prices[2]
            print("$", price)
        if items.lower() == "milk":
            price += wic_prices[3]
            print("$", price)
        if items.lower() == "cheese":
            price += wic_prices[4]
            print("$", price)
        if items.lower() == "meat":
            price += wic_prices[5]
            print("$", price)
        if items.lower() == "fruit":
            price += wic_prices[6]
            print("$", price)
        if items.lower() == "bread":
            price += wic_prices[7]
            print("$", price)
        if items.lower() == "water":
            price += wic_prices[8]
            print("$", price)
        if items.lower() == "soda":
            price += wic_prices[9]
            print("$", price)
        if items.lower() == "shirt":
            price += clothing_prices[0]
            print("$", price)
        if items.lower() == "pants":
            price += clothing_prices[1]
            print("$", price)
        if items.lower() == "shoes":
            price += clothing_prices[2]
            print("$", price)
        if items.lower() == "toothbrush":
            price += e_e_prices[0]
            print("$", price)
        if items.lower() == "toothpaste":
            price += e_e_prices[1]
            print("$", price)
        if items.lower() == "deodorant":
            price += e_e_prices[2]
            print("$", price)
        if items.lower() == "shampoo":
            price += e_e_prices[3]
            print("$", price)
        if items.lower() == "conditioner":
            price += e_e_prices[4]
            print("$", price)

    print("Total cost before tax ", "$", price)
    if state.lower() == "massachusetts":
        total = price + (price * state_tax_massachusetts)
        print("Total cost after tax ", "$", total)
    if state.lower() == "new hampshire":
        total = price + (price * state_tax_new_hampshire)
        print("Total cost after tax ", "$", total)
    if state.lower() == "maine":
        total = price + (price * state_tax_maine)
        print("Total cost after tax ", "$", total)
    return total


if __name__ == '__main__':
    main()
