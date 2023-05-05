# coding: utf-8

"""
    Amber API Server

    Boon Logic Amber API server

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TrainingConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'history_window': 'int',
        'buffering_samples': 'int',
        'learning_max_samples': 'int',
        'learning_max_clusters': 'int',
        'learning_rate_numerator': 'int',
        'learning_rate_denominator': 'int'
    }

    attribute_map = {
        'history_window': 'historyWindow',
        'buffering_samples': 'bufferingSamples',
        'learning_max_samples': 'learningMaxSamples',
        'learning_max_clusters': 'learningMaxClusters',
        'learning_rate_numerator': 'learningRateNumerator',
        'learning_rate_denominator': 'learningRateDenominator'
    }

    def __init__(self, history_window=None, buffering_samples=None, learning_max_samples=None, learning_max_clusters=None, learning_rate_numerator=None, learning_rate_denominator=None):
        """TrainingConfig - a model defined in Swagger"""
        self._history_window = None
        self._buffering_samples = None
        self._learning_max_samples = None
        self._learning_max_clusters = None
        self._learning_rate_numerator = None
        self._learning_rate_denominator = None
        self.discriminator = None
        if history_window is not None:
            self.history_window = history_window
        if buffering_samples is not None:
            self.buffering_samples = buffering_samples
        if learning_max_samples is not None:
            self.learning_max_samples = learning_max_samples
        if learning_max_clusters is not None:
            self.learning_max_clusters = learning_max_clusters
        if learning_rate_numerator is not None:
            self.learning_rate_numerator = learning_rate_numerator
        if learning_rate_denominator is not None:
            self.learning_rate_denominator = learning_rate_denominator

    @property
    def history_window(self):
        """Gets the history_window of this TrainingConfig.

        Number of past inferences to take into account when computing `warningLevel` at a given moment.

        :return: The history_window of this TrainingConfig.
        :rtype: int
        """
        return self._history_window

    @history_window.setter
    def history_window(self, history_window):
        """Sets the history_window of this TrainingConfig.

        Number of past inferences to take into account when computing `warningLevel` at a given moment.

        :param history_window: The history_window of this TrainingConfig.
        :type: int
        """

        self._history_window = history_window

    @property
    def buffering_samples(self):
        """Gets the buffering_samples of this TrainingConfig.

        Number of data vectors to collect during `Buffering`. These samples are used as data for `Autotuning`.

        :return: The buffering_samples of this TrainingConfig.
        :rtype: int
        """
        return self._buffering_samples

    @buffering_samples.setter
    def buffering_samples(self, buffering_samples):
        """Sets the buffering_samples of this TrainingConfig.

        Number of data vectors to collect during `Buffering`. These samples are used as data for `Autotuning`.

        :param buffering_samples: The buffering_samples of this TrainingConfig.
        :type: int
        """

        self._buffering_samples = buffering_samples

    @property
    def learning_max_samples(self):
        """Gets the learning_max_samples of this TrainingConfig.

        Maximum number of vectors to process during `Learning` before transitioning to `Monitoring`.

        :return: The learning_max_samples of this TrainingConfig.
        :rtype: int
        """
        return self._learning_max_samples

    @learning_max_samples.setter
    def learning_max_samples(self, learning_max_samples):
        """Sets the learning_max_samples of this TrainingConfig.

        Maximum number of vectors to process during `Learning` before transitioning to `Monitoring`.

        :param learning_max_samples: The learning_max_samples of this TrainingConfig.
        :type: int
        """

        self._learning_max_samples = learning_max_samples

    @property
    def learning_max_clusters(self):
        """Gets the learning_max_clusters of this TrainingConfig.

        Maximum number of clusters before model transitions from `Learning` to `Monitoring`.

        :return: The learning_max_clusters of this TrainingConfig.
        :rtype: int
        """
        return self._learning_max_clusters

    @learning_max_clusters.setter
    def learning_max_clusters(self, learning_max_clusters):
        """Sets the learning_max_clusters of this TrainingConfig.

        Maximum number of clusters before model transitions from `Learning` to `Monitoring`.

        :param learning_max_clusters: The learning_max_clusters of this TrainingConfig.
        :type: int
        """

        self._learning_max_clusters = learning_max_clusters

    @property
    def learning_rate_numerator(self):
        """Gets the learning_rate_numerator of this TrainingConfig.

        Switch to `Monitoring` if there were fewer than `learningRateNumerator` new clusters in the last `learningRateDenominator` inferences.

        :return: The learning_rate_numerator of this TrainingConfig.
        :rtype: int
        """
        return self._learning_rate_numerator

    @learning_rate_numerator.setter
    def learning_rate_numerator(self, learning_rate_numerator):
        """Sets the learning_rate_numerator of this TrainingConfig.

        Switch to `Monitoring` if there were fewer than `learningRateNumerator` new clusters in the last `learningRateDenominator` inferences.

        :param learning_rate_numerator: The learning_rate_numerator of this TrainingConfig.
        :type: int
        """

        self._learning_rate_numerator = learning_rate_numerator

    @property
    def learning_rate_denominator(self):
        """Gets the learning_rate_denominator of this TrainingConfig.

        See `learningRateNumerator`.

        :return: The learning_rate_denominator of this TrainingConfig.
        :rtype: int
        """
        return self._learning_rate_denominator

    @learning_rate_denominator.setter
    def learning_rate_denominator(self, learning_rate_denominator):
        """Sets the learning_rate_denominator of this TrainingConfig.

        See `learningRateNumerator`.

        :param learning_rate_denominator: The learning_rate_denominator of this TrainingConfig.
        :type: int
        """

        self._learning_rate_denominator = learning_rate_denominator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TrainingConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrainingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
