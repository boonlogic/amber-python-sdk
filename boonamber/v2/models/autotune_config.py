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

class AutotuneConfig(object):
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
        'range': 'bool',
        'percent_variation': 'bool'
    }

    attribute_map = {
        'range': 'range',
        'percent_variation': 'percentVariation'
    }

    def __init__(self, range=True, percent_variation=True):
        """AutotuneConfig - a model defined in Swagger"""
        self._range = None
        self._percent_variation = None
        self.discriminator = None
        if range is not None:
            self.range = range
        if percent_variation is not None:
            self.percent_variation = percent_variation

    @property
    def range(self):
        """Gets the range of this AutotuneConfig.


        :return: The range of this AutotuneConfig.
        :rtype: bool
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this AutotuneConfig.


        :param range: The range of this AutotuneConfig.
        :type: bool
        """

        self._range = range

    @property
    def percent_variation(self):
        """Gets the percent_variation of this AutotuneConfig.


        :return: The percent_variation of this AutotuneConfig.
        :rtype: bool
        """
        return self._percent_variation

    @percent_variation.setter
    def percent_variation(self, percent_variation):
        """Sets the percent_variation of this AutotuneConfig.


        :param percent_variation: The percent_variation of this AutotuneConfig.
        :type: bool
        """

        self._percent_variation = percent_variation

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
        if issubclass(AutotuneConfig, dict):
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
        if not isinstance(other, AutotuneConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
