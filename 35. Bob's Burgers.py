class Restaurant:

    name = ""
    category = ""
    rating = 0.0
    delivery = False

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

shreya_d = Restaurant()

shreya_d.name = 'Shreya\'s'
shreya_d.category = 'Indian Restro'
shreya_d.rating = 4.9
shreya_d.delivery = True

vk = Restaurant()

vk.name = "V\'s Korean BBQ"
vk.category = "Korean Barbeque"
vk.rating = 4.6
vk.delivery = True

print(vars(bobs_burgers))
print(vars(shreya_d))
print(vara(vk))