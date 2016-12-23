import abc
import logging


class QAModel:
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(__name__)

    @abc.abstractmethod
    def encode_data_instance(self, instance):
        """
        Encode a single data instance in a format acceptable by the model.
        A data instance is a list of possible graphs.

        :param instance: a list of possible graphs for a single question.
        :return: a tuple that represents the instance in the model format.
        """

    @abc.abstractmethod
    def test(self, data_with_targets, verbose=False):
        raise NotImplementedError

    @abc.abstractmethod
    def apply_on_batch(self, data_batch):
        raise NotImplementedError

    @abc.abstractmethod
    def apply_on_instance(self, instance):
        raise NotImplementedError


class TrainableQAModel(QAModel):
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        super(TrainableQAModel, self).__init__(**kwargs)

    @abc.abstractmethod
    def train(self, data_with_targets):
        raise NotImplementedError

    @abc.abstractmethod
    def encode_data_for_training(self, data_with_targets):
        raise NotImplementedError
