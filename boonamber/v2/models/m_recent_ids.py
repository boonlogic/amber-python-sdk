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

class MRecentIDs(object):
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
        'm_values': 'list[float]'
    }

    attribute_map = {
        'version_number': 'versionNumber',
        'm_values': 'm_Values'
    }

    def __init__(self, version_number=None, m_values=None):
        """MRecentIDs - a model defined in Swagger"""
        self._version_number = None
        self._m_values = None
        self.discriminator = None
        if version_number is not None:
            self.version_number = version_number
        self.m_values = m_values

    @property
    def version_number(self):
        """Gets the version_number of this MRecentIDs.


        :return: The version_number of this MRecentIDs.
        :rtype: VersionNumber
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this MRecentIDs.


        :param version_number: The version_number of this MRecentIDs.
        :type: VersionNumber
        """

        self._version_number = version_number

    @property
    def m_values(self):
        """Gets the m_values of this MRecentIDs.


        :return: The m_values of this MRecentIDs.
        :rtype: list[float]
        """
        return self._m_values

    @m_values.setter
    def m_values(self, m_values):
        """Sets the m_values of this MRecentIDs.


        :param m_values: The m_values of this MRecentIDs.
        :type: list[float]
        """
        if m_values is None:
            raise ValueError("Invalid value for `m_values`, must not be `None`")

        self._m_values = m_values

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
        if issubclass(MRecentIDs, dict):
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
        if not isinstance(other, MRecentIDs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
