
class Config(object):
    def __init__(self):
        self.model = ModelConfig()
        self.training = TrainingConfig()


class ModelConfig(object):
    def __init__(self):
        self.path = ""
        self.cnn_filters = 128
        self.cnn_kernel_size = 3


class TrainingConfig(object):
    pass
