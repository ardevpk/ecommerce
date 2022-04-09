# from django.test import TestCase

# Create your tests here.

from .models import product


# def addprods():
#     for i in range(0, 41):
#         name = input("Enter Product Name: ")
#         peicePerBox = int(input("Enter Peice Per Box: "))
#         priceByBox = int(int(input("Enter Price Per Peice: ")) * peicePerBox)
#         products = product.objects.create(
#         brand = "Crystal",
#         name = name,
#         # color = input("Enter Product Color: "),
#         color = "White",
#         category = name,
#         image = "allproduct.png",
#         priceByBox = priceByBox,
#         stockByPeice = "1000",
#         peicePerBox = peicePerBox,
#         discount = False if 'Y' in input("Press Y if This Product Is Not Discounted: ") else True
#         )
#         products.save()
#         print(f"{i}: Product Added Successfully")



            # peicePerBox = prod.peicePerBox
            # priceByBox = int(int(price) * peicePerBox)
            # # priceByBox = prod.priceByBox
            # productsave = product.objects.create(
            # brand = "Grandi",
            # name = name,
            # # color = input("Enter Product Color: "),
            # color = "White",
            # category = name,
            # image = "allproduct.png",
            # priceByBox = priceByBox,
            # stockByPeice = "1000",
            # peicePerBox = peicePerBox,
            # discount = True
            # )






def addprods():
    # products = product.objects.all().filter(color="White", brand="Grandi").order_by('id')
    products = product.objects.all().filter(color=input("Enter The Color To Filter: "), brand=input("Enter The Brand To Filter: ")).order_by('id')
    brand = input("Enter The Brand To Add To New Product: ")
    color = input("Enter The Color To Add To New Product: ")
    for count, prod in enumerate(products):
        name = prod.name
        price = input(f"Enter Price of \'{prod.name}\' Peice: ")
        if price == "":
            continue
        else:
            peicePerBox = prod.peicePerBox
            priceByBox = int(int(price) * peicePerBox)
            # priceByBox = prod.priceByBox
            productsave = product.objects.create(
            brand = brand,
            name = name,
            color = color,
            category = name,
            image = "allproduct.png",
            priceByBox = priceByBox,
            stockByPeice = "1000",
            peicePerBox = peicePerBox,
            discount = True
            )
            productsave.save()
            print(f"{count+1}: Product Added Successfully")

# def addprods():
#     products = product.objects.all().filter(name="2Way Only").order_by('id')
#     for count, prod in enumerate(products):
#         productsave = product.objects.get(id=prod.id)
#         productsave.name = "2 Way Only"
#         productsave.category = "2 Way Only"
#         productsave.save()
#         print(f"{count}: Product Added Successfully")