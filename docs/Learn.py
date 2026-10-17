# This line is a comment. Python ignores it.
# print("Hello from Osogbo")
# print(28454 * 100)
# print(10/4)

# state = "Osun"
# print(state)
# state = "Lagos"
# print(state)

# population = 3256858
# buffer_distance = 500
# ward_name = "Olorunda"
# print(ward_name, buffer_distance)

# print(5 + 5 )
# print("5" + "5")

# area_text = "12.4"
# area_number = float(area_text)
# print(area_number * 100)

# wards = ["Olorunda", "Ifelodun", "Ife North", "Ife South"]
# print (len(wards))
# print(wards[0])
# print(wards[1])

#   wards = ["Osogbo", "Ife", "Ede", "Iwo"]
#   wards.append("Ilesa")
#   print(wards)
#   for ward in wards:
#      print("checking", ward)

#areas = [28454, 3345, 20131]

#   for area in areas:
#    hectares = area * 100
#    print(area, "square km is", hectares, "hectares")
#print("done")

#area = 28454

#if area > 20000:
 #   print("large")
#elif area > 5000:
#    print("medium")
#else:
#    print("small")

#for area in areas:
#    if area > 20000:
#        print(area, "is large")
#    else:
#        print(area, "is small")

oyo_hectares = 28454 * 100
lagos_hectares = 3345 * 100
kano_hectares = 20131 * 100

def km2_to_hectares(area):
    return area * 100
print(km2_to_hectares(28454))
print(km2_to_hectares(3345))
print(km2_to_hectares(20131))

def describe(name, count):
    return name + " has " + str(count) + " wards"
print(describe("Osogbo", 10))
print(describe("Ibadan North", 12))

print(total)
