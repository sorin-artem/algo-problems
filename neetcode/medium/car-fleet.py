def carFleet(target: int, position, speed):
    cars = [[p, s] for p,s in zip(position, speed)]
    cars.sort(reverse=True)
    stack = []
    for i in range(len(cars)):
        car_position, car_speed = cars[i]
        time = (target - car_position) / car_speed
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

print(carFleet(10, [5,1,0,7], [2,2,1,1]))