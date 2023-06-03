import random 

INTERVAL = 1000

num_points_circle = 0
num_points_square = 0


for i in range(INTERVAL**2):
    rand_x = random.uniform(-1,1)
    rand_y = random.uniform(-1,1)

    distance_from_origin = rand_x**2 + rand_y**2

    if distance_from_origin <= 1:
        num_points_circle+=1
    
    num_points_square+=1

est_pi = 4*num_points_circle/num_points_square

print(f'The estimated value of pi is {est_pi}')



