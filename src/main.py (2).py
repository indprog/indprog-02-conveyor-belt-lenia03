motors = int(input())
weight=int(input())
weight_per_motor=weight/motors
if weight_per_motor<=12:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No! The conveyor belt cannot carry the packages.")   