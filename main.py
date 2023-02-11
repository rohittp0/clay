from flesh import Flesh


def main():
    flesh = Flesh(6, [6, 12, 6])

    with open("w.txt", "r") as f:
        w = f.read().split(" ")
        for param in flesh.parameters():
            param.data = float(w.pop(0))

    while True:
        inp = input("Hi 👋: ")[:6]

        if inp == "exit":
            break

        if len(inp) < 6:
            inp += " " * (6 - len(inp))

        print("".join([chr(round(c.data * 255)) for c in flesh([ord(c) / 255 for c in inp])]))


if __name__ == '__main__':
    main()


# import random
#
# from flesh import Flesh
# from value import Value
#
#
# # data = [((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6))]
#
#
# def main(data):
#     flesh = Flesh(6, [6, 12, 6])
#     lr = 0.001
#
#     for _ in range(0, 500):
#         flesh.zero_grad()
#         mse = Value(0)
#
#         for x, y in random.sample(data, 30):
#             out = flesh(x)
#             mse += flesh.checkup(out, y)
#
#         mse.backward()
#
#         if _ % 100 == 0:
#             print(mse.data)
#             lr *= 0.5
#
#         for param in flesh.parameters():
#             param.data -= lr * param.grad
#
#     # write all the weights to a file
#     with open("w.txt", "w") as f:
#         for param in flesh.parameters():
#             f.write(str(param.data) + " ")
#
#     print("".join([chr(round(c.data * 255)) for c in flesh(p)]))
#     print("".join([chr(round(c.data * 255)) for c in flesh([ord(c) / 255 for c in "hello!"])]))
#
#
# if __name__ == '__main__':
#
#     data = []
#
#     n = [ord(c) / 255 for c in "neuron"]
#     m = [ord(c) / 255 for c in "This bread is my "]
#
#
#     for i in range(1000):
#         # rand_sequence = [random.random() for _ in range(6)]
#         data.append((p, l))
#         # data.append((m, f))
#
#     main(data)
#
#     # print(data)

