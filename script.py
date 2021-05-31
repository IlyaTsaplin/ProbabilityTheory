import random


class Graph:

    def __init__(self, matrix, starting_state):
        self.matrix = matrix
        self.curState = starting_state-1
        self.path = [starting_state]
        self.times = [0]*len(self.matrix)
        self.times[starting_state-1] += 1
        
    def set_state(self, state):
        self.curState = state-1
        
    def clean_path(self):
        self.path = [self.curState+1]
        
    def clean_times(self):
        self.times = [0]*len(self.matrix)
        self.times[self.curState] += 1
        
    def print_times_percentages(self):
        times_sum = sum(self.times)
        percentages = self.times
        for i in range(len(percentages)):
            percentages[i] /= times_sum
        
        print(percentages)
        
    def move(self):
        probability = random.random()

        index = 0
        summary = self.matrix[self.curState][index]
        while probability > summary:
            index += 1
            summary = summary + self.matrix[self.curState][index]

        self.curState = index
        self.times[index] += 1
        self.path = self.path + [index + 1]


#Задание матрицы
matrix = [[0.2, 0.4, 0.2, 0.0, 0.2, 0.0],
          [0.1, 0.3, 0.4, 0.0, 0.2, 0.0],
          [0.6, 0.1, 0.1, 0.0, 0.2, 0.0],
          [0.0, 0.0, 0.0, 0.6, 0.0, 0.4],
          [0.3, 0.3, 0.2, 0.0, 0.2, 0.0],
          [0.0, 0.0, 0.0, 0.7, 0.0, 0.3]]

test = Graph(matrix, 1)

for state in range(len(matrix)):
    test.set_state(state+1)
    test.clean_path()
    test.clean_times()
    print('State ' + str(state+1) + ':\n')
    print('10 moves:')
    for i in range(10):
        test.move()
    
    print('Path: ' + str(test.path))
    print('Time percentages: ')
    test.print_times_percentages()
    print('\n')
    
    test.set_state(state+1)
    test.clean_path()
    test.clean_times()
    
    print('50 moves:')
    for i in range(50):
        test.move()
        
    print('Path: ' + str(test.path))
    print('Time percentages: ')
    test.print_times_percentages()
    print('\n')
    
    test.set_state(state+1)
    test.clean_path()
    test.clean_times()
    
    print('100 moves:')
    for i in range(100):
        test.move()
    
    print('Path: ' + str(test.path))
    print('Time percentages: ')
    test.print_times_percentages()
    print('\n')
    
    test.set_state(state+1)
    test.clean_path()
    test.clean_times()
    
    print('1000 moves:')
    for i in range(1000):
        test.move()
        
    print('Path: ' + str(test.path))
    print('Time percentages: ')
    test.print_times_percentages()
    print('\n')


