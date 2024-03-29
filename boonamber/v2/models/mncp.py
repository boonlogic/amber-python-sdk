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

class MNCP(object):
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
        'version_number': 'VersionNumber',
        'num_of_features': 'float',
        'm_numeric_format': 'float',
        'm_percent_variation': 'float',
        'm_accuracy': 'float',
        'm_streaming_window_size': 'float'
    }

    attribute_map = {
        'version_number': 'versionNumber',
        'num_of_features': 'numOfFeatures',
        'm_numeric_format': 'm_NumericFormat',
        'm_percent_variation': 'm_PercentVariation',
        'm_accuracy': 'm_Accuracy',
        'm_streaming_window_size': 'm_StreamingWindowSize'
    }

    def __init__(self, version_number=None, num_of_features=None, m_numeric_format=None, m_percent_variation=None, m_accuracy=None, m_streaming_window_size=None):
        """MNCP - a model defined in Swagger"""
        self._version_number = None
        self._num_of_features = None
        self._m_numeric_format = None
        self._m_percent_variation = None
        self._m_accuracy = None
        self._m_streaming_window_size = None
        self.discriminator = None
        if version_number is not None:
            self.version_number = version_number
        if num_of_features is not None:
            self.num_of_features = num_of_features
        if m_numeric_format is not None:
            self.m_numeric_format = m_numeric_format
        if m_percent_variation is not None:
            self.m_percent_variation = m_percent_variation
        if m_accuracy is not None:
            self.m_accuracy = m_accuracy
        if m_streaming_window_size is not None:
            self.m_streaming_window_size = m_streaming_window_size

    @property
    def version_number(self):
        """Gets the version_number of this MNCP.


        :return: The version_number of this MNCP.
        :rtype: VersionNumber
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this MNCP.


        :param version_number: The version_number of this MNCP.
        :type: VersionNumber
        """

        self._version_number = version_number

    @property
    def num_of_features(self):
        """Gets the num_of_features of this MNCP.


        :return: The num_of_features of this MNCP.
        :rtype: float
        """
        return self._num_of_features

    @num_of_features.setter
    def num_of_features(self, num_of_features):
        """Sets the num_of_features of this MNCP.


        :param num_of_features: The num_of_features of this MNCP.
        :type: float
        """

        self._num_of_features = num_of_features

    @property
    def m_numeric_format(self):
        """Gets the m_numeric_format of this MNCP.


        :return: The m_numeric_format of this MNCP.
        :rtype: float
        """
        return self._m_numeric_format

    @m_numeric_format.setter
    def m_numeric_format(self, m_numeric_format):
        """Sets the m_numeric_format of this MNCP.


        :param m_numeric_format: The m_numeric_format of this MNCP.
        :type: float
        """

        self._m_numeric_format = m_numeric_format

    @property
    def m_percent_variation(self):
        """Gets the m_percent_variation of this MNCP.


        :return: The m_percent_variation of this MNCP.
        :rtype: float
        """
        return self._m_percent_variation

    @m_percent_variation.setter
    def m_percent_variation(self, m_percent_variation):
        """Sets the m_percent_variation of this MNCP.


        :param m_percent_variation: The m_percent_variation of this MNCP.
        :type: float
        """

        self._m_percent_variation = m_percent_variation

    @property
    def m_accuracy(self):
        """Gets the m_accuracy of this MNCP.


        :return: The m_accuracy of this MNCP.
        :rtype: float
        """
        return self._m_accuracy

    @m_accuracy.setter
    def m_accuracy(self, m_accuracy):
        """Sets the m_accuracy of this MNCP.


        :param m_accuracy: The m_accuracy of this MNCP.
        :type: float
        """

        self._m_accuracy = m_accuracy

    @property
    def m_streaming_window_size(self):
        """Gets the m_streaming_window_size of this MNCP.


        :return: The m_streaming_window_size of this MNCP.
        :rtype: float
        """
        return self._m_streaming_window_size

    @m_streaming_window_size.setter
    def m_streaming_window_size(self, m_streaming_window_size):
        """Sets the m_streaming_window_size of this MNCP.


        :param m_streaming_window_size: The m_streaming_window_size of this MNCP.
        :type: float
        """

        self._m_streaming_window_size = m_streaming_window_size

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
        if issubclass(MNCP, dict):
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
        if not isinstance(other, MNCP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
