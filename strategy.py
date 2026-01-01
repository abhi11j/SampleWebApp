class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"StrategyA processed {data}"

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"StrategyB processed {data}"

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_action(self, data):
        return self._strategy.execute(data)
