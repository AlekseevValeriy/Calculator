class C:
    def __init__(self, var):
        self.var = var

    def _dec(fn):
        def f(self, *args, **kwargs):
            fn(self, *args, **kwargs)
            print(self.var)

        return f

    @_dec
    def bar(self):
        print('bar')

c = C(42);
c.bar()