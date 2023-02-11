import random

from value import Value


class Generalization:

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []


class Cell(Generalization):

    def __init__(self, nin, non_lin=True):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        self.b = Value(0)
        self.non_lin = non_lin

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        return act.relu() if self.non_lin else act

    def parameters(self):
        return self.w + [self.b]


class Tissue(Generalization):

    def __init__(self, nin, nout, **kwargs):
        self.cells = [Cell(nin, **kwargs) for _ in range(nout)]

    def __call__(self, x):
        out = [n(x) for n in self.cells]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.cells for p in n.parameters()]


class Flesh(Generalization):

    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.tissues = [Tissue(sz[i], sz[i + 1], non_lin=i != len(nouts) - 1) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.tissues:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.tissues for p in layer.parameters()]

    @staticmethod
    def checkup(out, y):
        return sum((out[i] - y[i]) ** 2 for i in range(len(out)))
