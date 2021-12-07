class MockRequest:
    def __init__(self, method, args, form):
        self.method = method
        self.args = args
        self.form = form
