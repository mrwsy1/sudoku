import backtrack

sample = [
    [2,5,6,4,0,3,0,9,1],
    [0,0,0,0,0,6,0,0,5],
    [3,4,0,8,0,0,0,2,0],
    [4,2,0,5,0,8,0,1,3],
    [0,0,5,0,0,0,6,0,7],
    [6,8,0,1,0,0,0,0,4],
    [5,0,8,7,3,0,0,6,0],
    [1,0,0,6,8,0,0,0,9],
    [0,0,0,2,1,0,0,3,0]]

def print_grid(sample):
    for i in range(9):
        if i%3==0 and i!=0:
            print()
        for j in range(9):
            if j%3==0 and j!=0:
                print("\t", end="")
            if j==8:
                print(sample[i][j])
            else:
                print(sample[i][j], end=" ")

solution = backtrack.find_solution(sample)
if solution==True:
    print("\t--------\n\t ANSWER\n\t--------")
    print_grid(sample)
else:
    print("\t-------\n\t ERROR\n\t-------")
    print("Unable to solve puzzle.")