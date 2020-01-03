from tools.config import *
from tensorflow.keras import layers
from tensorflow.keras import regularizers


class AlphaZeroModel(object):
    def __init__(self, config: Config):
        self.config = config
        self.model = None

    def build(self):
        mc = self.config.model

        input1 = layers.Input(shape=(2, 6, 7))
        x = layers.Conv2D(
            filters=mc.cnn_filters,
            kernel_size=mc.cnn_kernel_size,
            padding="same",
            data_format="channels_first",
            kernel_regularizer=regularizers.l2()
        )(input1)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)
