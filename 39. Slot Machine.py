import random

Symbols = ['🍒',' 🍇', '🍉','7️⃣']

results = random.choices(Symbols, k=3)
print(results[0] + ' |' + results[1] + ' | ' + results[2])
    
if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print("Jackpot! 💰")
else:
    print("Thanks for playing")
