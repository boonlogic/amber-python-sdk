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

class PostOauth2AccessRequest(object):
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
        'license_key': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'license_key': 'licenseKey',
        'secret_key': 'secretKey'
    }

    def __init__(self, license_key=None, secret_key=None):
        """PostOauth2AccessRequest - a model defined in Swagger"""
        self._license_key = None
        self._secret_key = None
        self.discriminator = None
        self.license_key = license_key
        self.secret_key = secret_key

    @property
    def license_key(self):
        """Gets the license_key of this PostOauth2AccessRequest.

        Amber account license.

        :return: The license_key of this PostOauth2AccessRequest.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this PostOauth2AccessRequest.

        Amber account license.

        :param license_key: The license_key of this PostOauth2AccessRequest.
        :type: str
        """
        if license_key is None:
            raise ValueError("Invalid value for `license_key`, must not be `None`")

        self._license_key = license_key

    @property
    def secret_key(self):
        """Gets the secret_key of this PostOauth2AccessRequest.

        Amber account secret key.

        :return: The secret_key of this PostOauth2AccessRequest.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this PostOauth2AccessRequest.

        Amber account secret key.

        :param secret_key: The secret_key of this PostOauth2AccessRequest.
        :type: str
        """
        if secret_key is None:
            raise ValueError("Invalid value for `secret_key`, must not be `None`")

        self._secret_key = secret_key

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
        if issubclass(PostOauth2AccessRequest, dict):
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
        if not isinstance(other, PostOauth2AccessRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
