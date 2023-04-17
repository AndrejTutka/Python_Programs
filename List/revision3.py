# Find out, what outcome is obtained using the max() and min() from the list3. Reason it!

list3 = ["Shanghai","China","Buenos Aires","Argentina","Mumbai","India","Mexico City","Distrito Federal","Mexico","Karachi","Pakistan","İstanbul","Turkey","Delhi","India","Manila","Philippines","Moscow","Russia","Dhaka","Bangladesh","Seoul","South Korea","São Paulo","Brazil","Lagos","Nigeria","Jakarta","Indonesia","Tokyo","Japan","Zhumadian","China","New York","New York","United States","Taipei","Taiwan","Kinshasa","Democratic Republic of the Congo","Lima","Peru","Cairo","Egypt","London","United Kingdom","Beijing","China","Tehrān","Iran","Nanchong","China","Bogotá","Colombia","Hong Kong","China","Lahore","Pakistan","Rio de Janeiro","Brazil","Baghdad","Iraq","Tai’an","China","Bangkok","Thailand","Bangalore","India","Yueyang","China","Santiago","Chile","Kaifeng","China","Kolkata","India","Toronto","Ontario","Canada","Yangon","Myanmar","Sydney","New South Wales","Australia","Chennai","India","Riyadh","Saudi Arabia","Wuhan","China","Saint Petersburg","Russia","Chongqing","China","Chengdu","China","Chittagong","Bangladesh","Alexandria","Egypt","Los Angeles","California","United States","Tianjin","China","Melbourne","Victoria","Australia","Ahmadābād","India","Pusan","South Korea","Abidjan","Cote d'Ivoire","Kano","Nigeria","Hyderābād","India","Puyang","China","Yokohama-shi","Japan","Ibadan","Nigeria","Singapore","Singapore","Ankara","Turkey","Shenyang","China","Hồ Chí Minh City","Vietnam","Shiyan","China","Cape Town","South Africa"]

def sum_letters(text):
  outcome = 0
  for symbol in text:
    outcome += ord(symbol)
  return outcome


print(max(list3))                       #???
print(max(list3, key = len))            #The longest name in the list
print(max(list3, key = sum_letters))    #???

print(min(list3))                       #???
print(min(list3, key = len))            #???
print(min(list3, key = sum_letters))    #???