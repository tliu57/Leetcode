from collections import OrderedDict
MENU = {
  "Fruit": 2.15,
  "Fries": 2.75,
  "Salad": 3.35,
  "Wings": 3.55,
  "Plate": 5.80,
  "Mozzarella": 4.20,
}

epsilon = 0.01
total_amount = 15.05

def solution(total_amount, menu):
    # given total_amount and menu, return a possible appetizer
    candidates = OrderedDict(sorted(menu.items(), key=lambda t: t[1]))
    target = total_amount
    result = []
    sub = []
    helper(result, sub, target, candidates, 0)
    return result
    
    
def helper(result, sub, target, candidates, pos): 
    if target >= 0 and target < epsilon:
            if sub not in result:
                result.append([elem for elem in sub])
            return
    for i in range(pos, len(candidates)):
        newTarget = target - candidates.items()[i][1]
        if newTarget >= 0:
            sub.append(candidates.items()[i])
            helper(result, sub, newTarget, candidates, pos+1)
            sub.pop()
            

print solution(total_amount, MENU)
