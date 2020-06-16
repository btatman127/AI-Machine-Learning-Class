import random
import math

# read text file for more info


# multiply vectors of same length
def mul_to_vec(x, y):
    results = [x[i] * y[i] for i in range(len(x))]
    return results


# multiplies scalar to a matrix
def scalar_mul_to_matrix(x, y):
    results = []
    for i in range(len(y)):
        a = [x*y[i][j] for j in range(len(y[0]))]
        results.append(a)
    return results


# multiplies two matrices together
def mat_mul(X, Y):
    if not hasattr(X[0], '__len__'):
        X = [X]
    if not hasattr(Y[0], '__len__'):
        Y = [Y]
    if len(X[0]) == 1:
        results = []
        for i in range(len(X)):
            a = [X[i][0] * Y[0][j] for j in range(len(Y[0]))]
            results.append(a)
        return results
    else:
        return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X][0]


# vector subtraction of two vectors of the same length
def vec_sub(x, y):
    results = [x[i]-y[i] for i in range(len(x))]
    return results


# matrix addition of two matrices of the same size
def mat_add(x, y):
    results = []
    for i in range(len(x)):
        results.append([x[i][j]+y[i][j] for j in range(len(x[0]))])
    return results


# transpose matrix
def transpose(x):
    if hasattr(x[0], '__len__'):
        a = []
        for i in range(len(x[0])):
            b = [x[j][i] for j in range(len(x))]
            a.append(b)
        return a
    else:
        return x


def sigmoid(x):
    a = []
    if hasattr(x[0], '__len__'):
        for i in range(len(x)):
            b = [1 / (1 + math.exp(-x[i][j])) for j in range(len(x[0]))]
            a.append(b)
    else:
        a = [1 / (1 + math.exp(-x[j])) for j in range(len(x))]
    return a


def sigmoid_derivative(x):
    a = [1 - x[j] for j in range(len(x))]
    c = [x[k] * a[k] for k in range(len(x))]
    return c


class Network:
    def __init__(self, *args):
        # initialize the weights for the biases that we will add later
        self.activity = sigmoid
        self.activity_derivative = sigmoid_derivative
        self.layers = len(args)
        self.arch = args
        self.weights = []

        # Random initialization with range of weight values (-0.1,0.1)
        for layer in range(self.layers - 1):
            w = []
            for i in range(args[layer] + 1):
                v = [random.uniform(-0.1, 0.1) for j in range(args[layer + 1])]
                w.append(v)
            self.weights.append(w)

    def _forward_prop(self, y):

        for i in range(len(self.weights) - 1):
            activation = mat_mul(y[i], self.weights[i])
            activity = self.activity(activation)
            # add the bias for the next layer
            activity.insert(0, 1)
            y.append(activity)

        # last layer
        activation = mat_mul(y[-1], self.weights[-1])
        activity = self.activity(activation)
        y.append(activity)

        return y

    def _back_prop(self, y, target, learning_rate=1):
        error = vec_sub(target, y[-1])
        delta_vec = [mul_to_vec(error, self.activity_derivative(y[-1]))]

        # begin from the back, from the next to last layer
        for i in range(self.layers - 2, 0, -1):
            error = mat_mul(delta_vec[-1], transpose(self.weights[i][1:]))
            if not hasattr(error[0], '__len__'):
                error = [mul_to_vec(error, self.activity_derivative(y[i][1:]))]
            else:
                error = [mul_to_vec(error[0], self.activity_derivative(y[i][1:]))]
            delta_vec.append(error)

        # set the values from back to front
        delta_vec.reverse()

        # adjust the weights, using the backpropagation rules
        for i in range(len(self.weights)):
            a = mat_mul(transpose([y[i]]), delta_vec[i])
            self.weights[i] = mat_add(self.weights[i], scalar_mul_to_matrix(learning_rate, a))

    def train(self, data, labels, learning_rate=1):
        b = data.copy()
        # Add column of ones to X
        # This is to add the bias unit to the input layer
        b.insert(0, 1)
        x = [b]

        y = self._forward_prop(x)

        # back-propagation of the error to adjust the weights:
        self._back_prop(y, labels, learning_rate)

    def predict_single_data(self, x):
        val = x.copy()
        val.insert(0, 1)
        for i in range(0, len(self.weights)):
            val = self.activity(mat_mul(val, self.weights[i]))
            val.insert(0, 1)
        return val[1:]

    # check the prediction result
    def run(self, X):
        y = self.predict_single_data(X)
        return y


def experiment(sizes, inputs, targets):
    net = Network(*sizes)
    for input in inputs:
        print(f'{input} -> {net.run(input)}')
    print('Training...')
    training = list(zip(inputs, targets))
    for epoch in range(10000):
        random.shuffle(training)
        for input, target in training:
            net.train(input, target)
    print('After training:')
    for input in inputs:
        print(f'{input} -> {net.run(input)}')
