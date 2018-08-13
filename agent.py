import numpy as np

ids = [0, 2, 5, 8, 11, 17]
variables = ['x', 'y', 'z']
ops = ['+', '-', '*', '>', '<', '==']

class Agent:
    code_length = 10
    running_times = 20

    def __init__(self, ws=None):
        self.sizes = [100, 100, 17]
        random_ws = [np.random.randn(m, n) for m, n in zip(self.sizes[1:], self.sizes)]
        self.ws = ws if ws != None else random_ws

    def main(self):
        self.forward()
        self.output_to_code()
        self.score = np.average([self.run() for _ in range(self.running_times)])

    def forward(self):
        self.xs = []
        h = np.ones((self.sizes[0], 1))
        for _ in range(0, self.code_length):
            h = np.tanh(self.ws[0].dot(h))
            self.xs.append(np.tanh(self.ws[1].dot(h)))

    def output_to_code(self):
        self.code = []
        existent_if = ''
        for x in self.xs:
            type, v1, v2, v3, op = [np.argmax(x[i:j]) for i, j in zip(ids, ids[1:])]
            v1, v2, v3 = [variables[id] for id in [v1, v2, v3]]
            op = ops[op]

            if type == 0:
                existent_if += (' and {}' if existent_if else 'if {}').format(v1)
            else:
                if_string = '{}: '.format(existent_if) if existent_if else ''
                self.code.append('{}{} = {} {} {}'.format(if_string, v1, v2, op, v3))
                existent_if = ''

    def run(self):
        x, y, z = np.random.randint(1, 10, size=(3,))
        _locals = locals()
        correct_z = max(x, y, z)
        for i in range(0, 10): correct_z = correct_z ** 2
        for line in self.code: exec(line, globals(), _locals)
        z = _locals['z']

        return self.score_function(z / correct_z)

    @staticmethod
    def score_function(x):
        if x > 0: return np.exp(-x)
        else:     return np.exp(x)
'''
from agent import Agent
a = Agent()
a.code = ['if y and x and x: z = x < x', 'x = y == x', 'if z: x = y > y', 'z = z * y', 'x = y * y', 'if y and z and x: z = x * x', 'x = z == y', 'z = y - z', 'y = z + y', 'if x and z: z = x < y']
a.run()
'''
