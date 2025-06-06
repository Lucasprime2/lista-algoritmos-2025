popA = 80000      
popB = 200000      
anos = 0           
while popA < popB:
    popA *= 1.03   
    popB *= 1.015  
    anos += 1
print(f"Serão necessários {anos} anos.")