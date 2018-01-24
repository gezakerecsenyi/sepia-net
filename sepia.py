#SEPIA - Suggestive Evolving Pixel Interpreting Algorithm

names = []
costs = []

width = int(input("Amount of pixels in each row"))
pixels = int(input("Amount of rows in picture")) * width

for i in range(int(input("Amount of possible values"))):
  names.append(input("Input number " + str(i+1) + " "))
  exec(names[i] + " = []")

amount = pixels

for b in range(len(names)):
  for i in range(amount):
    exec(names[b] + ".append(0)")

for i in range(int(input("Amount of inputs to be given"))):
  newInput = list(input("Enter input"))
  value = input("Enter value")
  limit = len(newInput)
  for b in range(limit):
    newInput[b] = int(newInput[b])
    if newInput[b] == 0:
      exec(value + "[b] = (" + value + "[b] - 0.5) / 2")
    else:
      exec(value + "[b] = (" + value + "[b] + 1) / 2")
      if b != 0:
        exec(value + "[b-1] = (" + value + "[b-1] + 0.5) / 2")
      if b > 1:
        exec(value + "[b-2] = (" + value + "[b-2] + 0.25) / 2")
      if b < limit - 1:
        exec(value + "[b+1] = (" + value + "[b+1] + 0.5) / 2")
      if b < limit - 2:
        exec(value + "[b+2] = (" + value + "[b+2] + 0.25) / 2")
      if b > width:
        exec(value + "[b-width] = (" + value + "[b-width] + 0.5) / 2")
      if b > width * 2:
        exec(value + "[b-(width*2)] = (" + value + "[b-(width*2)] + 0.25) / 2")
      if b > width - 1:
        exec(value + "[b-(width-1)] = (" + value + "[b-(width-1)] + 0.25) / 2")
      if b > width + 1:
        exec(value + "[b-(width+1)] = (" + value + "[b-(width+1)] + 0.25) / 2")
      if b < pixels - width:
        exec(value + "[b+width] = (" + value + "[b+width] + 0.5) / 2")
      if b < pixels - (width * 2):
        exec(value + "[b+(width*2)] = (" + value + "[b+(width*2)] + 0.25) / 2")
      if b < pixels - (width - 1):
        exec(value + "[b+(width-1)] = (" + value + "[b+(width-1)] + 0.25) / 2")
      if b < pixels - (width + 1):
        exec(value + "[b+(width+1)] = (" + value + "[b+(width+1)] + 0.25) / 2")
    
  for b in range(len(names)):
    print(names[b], "=", eval(names[b]))
    
number = input("Enter input to be tested")

for i in range(len(names)):
  cost = 0
  costs.append(0)
  for b in range(len(eval(names[i]))):
    curVal = eval(names[i])[b]
    if curVal == 0.0:
      if int(number[b]) == 1:
        if b == 0:
          curVal -= (1 / amount) / 2
        else:
          curVal -= (cost / amount) / 2
      else:
        if b == 0:
          curVal += 1 / amount
        else:
          curVal += cost / amount
    if number[b] == "0":
      cost -= curVal / 2
    else:
      cost += curVal
  costs[i] = cost
print(costs)

for i in range(len(costs)):
  curHolder = 0
  if costs[i] >= costs[curHolder]:
    curHolder = i
    print(names[i])
