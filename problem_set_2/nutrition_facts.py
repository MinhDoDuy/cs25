#5 Nutrition Facts
fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Sweet Cherries": 100,
    "Banana": 110,
    "Chocolate": 120
}
f = input("Item: ").lower()
if f in fruits:
    print("Calories: ", fruits[f]) #Lấy giá trị tương ứng với key f trong dict