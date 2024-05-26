from pulp import *

lemonade = LpVariable("Lemonade_units", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_juice_units", lowBound=0, cat='Integer')

model = LpProblem("Maximize_production", LpMaximize)

model += lemonade + fruit_juice, "Total_Production"
# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

model.solve()

print("Status:", LpStatus[model.status])
print("Total production:", value(model.objective))
print("Lemonade units:", value(lemonade))
print("Fruit juice units:", value(fruit_juice))
