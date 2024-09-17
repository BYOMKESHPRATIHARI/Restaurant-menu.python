menu =
{
  'pizza'     :80,
  'biryani'   :240,
  'kebab'     :450,
}
print ("pizza : Rs 80.00\n biryani: Rs240.00\n kebab: Rs450.00")

order_total = 0
item_1=input("What you want to Order?")
if item_1 in menu:
  order_total += menu [item_1]
print ("Item {item_1}" has been added to your order")
else 
print ("Ordered item {item_1} is not served")
another_order = input("anything else(yes/no)")
if another_order =="yes":
item_2 = input("what")
if item_2 in menu:
order_total += menu[item_2]
print ("{item_2} has been added")
else
print ("{item_2} is not served")

print ("total {order_total}")
