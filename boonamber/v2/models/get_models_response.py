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

class GetModelsResponse(object):
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
        'model_list': 'list[Model]'
    }

    attribute_map = {
        'model_list': 'modelList'
    }

    def __init__(self, model_list=None):
        """GetModelsResponse - a model defined in Swagger"""
        self._model_list = None
        self.discriminator = None
        if model_list is not None:
            self.model_list = model_list

    @property
    def model_list(self):
        """Gets the model_list of this GetModelsResponse.


        :return: The model_list of this GetModelsResponse.
        :rtype: list[Model]
        """
        return self._model_list

    @model_list.setter
    def model_list(self, model_list):
        """Sets the model_list of this GetModelsResponse.


        :param model_list: The model_list of this GetModelsResponse.
        :type: list[Model]
        """

        self._model_list = model_list

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
        if issubclass(GetModelsResponse, dict):
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
        if not isinstance(other, GetModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
