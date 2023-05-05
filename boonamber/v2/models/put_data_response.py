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

class PutDataResponse(object):
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
        'vector': 'dict(str, float)',
        'analytics': 'AnalyticResults',
        'status': 'ModelStatus'
    }

    attribute_map = {
        'vector': 'vector',
        'analytics': 'analytics',
        'status': 'status'
    }

    def __init__(self, vector=None, analytics=None, status=None):
        """PutDataResponse - a model defined in Swagger"""
        self._vector = None
        self._analytics = None
        self._status = None
        self.discriminator = None
        if vector is not None:
            self.vector = vector
        if analytics is not None:
            self.analytics = analytics
        if status is not None:
            self.status = status

    @property
    def vector(self):
        """Gets the vector of this PutDataResponse.

        The current fusion vector.

        :return: The vector of this PutDataResponse.
        :rtype: dict(str, float)
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """Sets the vector of this PutDataResponse.

        The current fusion vector.

        :param vector: The vector of this PutDataResponse.
        :type: dict(str, float)
        """

        self._vector = vector

    @property
    def analytics(self):
        """Gets the analytics of this PutDataResponse.


        :return: The analytics of this PutDataResponse.
        :rtype: AnalyticResults
        """
        return self._analytics

    @analytics.setter
    def analytics(self, analytics):
        """Sets the analytics of this PutDataResponse.


        :param analytics: The analytics of this PutDataResponse.
        :type: AnalyticResults
        """

        self._analytics = analytics

    @property
    def status(self):
        """Gets the status of this PutDataResponse.


        :return: The status of this PutDataResponse.
        :rtype: ModelStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PutDataResponse.


        :param status: The status of this PutDataResponse.
        :type: ModelStatus
        """

        self._status = status

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
        if issubclass(PutDataResponse, dict):
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
        if not isinstance(other, PutDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other