total=int(input('Enter the total no. of bananas at the start: ')) 
distance=int(input('Enter the distance which is to be covered: ')) 
load_capacity=int(input('Enter maximum load capacity of the camel: ')) 
lost_bananas=0 
bananas=total 
for i in range(distance): 
    while bananas>0: 
        bananas=bananas-load_capacity 
        if bananas==1: 
            lost_bananas=lost_bananas-1 
        lost_bananas=lost_bananas+2 
    lost_bananas=lost_bananas-1 
    bananas=total-lost_bananas 
    if bananas==0: 
        break 
print(bananas)