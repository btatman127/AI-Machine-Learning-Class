import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


# run either "experiment_1(m)" or "experiment_2(m)" where m is the number of data points
# experiment_1 compares the curves of degree 1,2 & 20 over the data points
# experiment_2 compares each degree to Average MSE
# lowest Average MSE will find the most likely degree of the equation used to generate the data points
# in this case, the answer should be 4

def generate_coefficients():
    """"
    Returns an array of five numbers, to be used as coefficients of a polynomial. Each number is chosen uniformly from the
    interval [-0.5, 0.5).
    """
    return np.random.uniform(low=-0.5, high=0.5, size=(5,))


def generate_data(m, coefficients):
    """
    Returns two arrays, X and y, each of which is m by 1. The values of X are evenly spaced across the interval
    [-5.0, 5.0]. For each x, the corresponding y value is

    a + b * X + c * X**2 + d * X**3 + e * X**4 + <noise>

    where coefficients is (a, b, c, d, e) and the noise for each point is normally distributed with mean 0 and
    standard deviation 1.
    """
    # evenly divides an array from [-5.0, 5.0] with length=m for X
    f = np.linspace(-5.0, 5.0, num=m).reshape(m, 1)

    # for y
    s = []
    for i in range(m):
        # a + b * X + c * X**2 + d * X**3 + e * X**4 + <noise>
        v = 0
        for j in range(len(coefficients)):
            v = v+coefficients[j]*f[i]**j
        s.append(v+np.random.uniform(low=-4, high=4))

    return f, s


def fit_curve(X, y, degree):
    """
    Returns a trained model that fits a polynomial of the specified degree to the data.
    """
    # basically we have an array for x values and an array of y values of what the fitted polynomial is
    x_plot = np.linspace(-5.0, 5.0, 100).reshape(100, 1)
    model = make_pipeline(PolynomialFeatures(degree), Ridge())
    model.fit(X, y)
    y_plot = model.predict(x_plot)
    return [x_plot, y_plot]


def plot_curve(degree, model):
    """
    Plots a curve for model, which represents a polynomial of the specified degree.
    The x values for the curve are 100 points evenly spaced across the interval [-0.5, 0.5].
    """
    # plot the polynomial for that degree
    plt.plot(model[0], model[1], label="degree %d" % degree)


def plot_data(X, y):
    """
    Plots X and y (as a scatter plot) and also constrains the y limit so that later, much larger values of y will not
    reset it.
    """
    plt.ylim(min(y) - 0.1 * (max(y) - min(y)), max(y) + 0.1 * (max(y) - min(y)))
    plt.scatter(X, y)


def experiment_1(m):
    """
    Generates m training points and fits models of degrees 1, 2, and 20. Plots the data and the curves for the models.
    """
    coeffs = generate_coefficients()
    X, y = generate_data(m, coeffs)
    plot_data(X, y)
    for d in [1, 2, 20]:
        model = fit_curve(X, y, d)
        plot_curve(d, model)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def mse(X, y, degree, model):
    """
    Returns the mean squared error for model (a polynomial of the specified degree) on X and y.
    """
    # calculate MSE for X and y and return both
    MSE_x = np.square(np.subtract(X, model[0])).mean()/len(X)
    MSE_y = np.square(np.subtract(y, model[1])).mean()/len(y)
    return MSE_x, MSE_y


def experiment_2(m):
    """
    Runs the following experiment 100 times:

    Generate m training data points
    Generate 100 testing data points (using the same coefficients)
    For each d from 1 through 30, fit a curve of degree d to the training data and measure its mse on the testing data.

    After the 100 runs, plots the average mse of each degree.
    """
    mses = {i: [] for i in range(1, 31)}
    for i in range(100):
        coeffs = generate_coefficients()
        X_train, y_train = generate_data(m, coeffs)
        X_test, y_test = generate_data(100, coeffs)
        for d in range(1, 31):
            model = fit_curve(X_train, y_train, d)
            mses[d] += [mse(X_test, y_test, d, model)]
    averages = [np.mean(mses[d]) for d in mses]
    plt.ylim(0, 5)
    plt.plot(range(1, 31), averages)
    plt.xlabel('Degree')
    plt.ylabel('Average MSE (100 runs)')
    plt.show()
