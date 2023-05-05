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

class PutDataRequest(object):
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
        'vector': 'list[FusionFeature]',
        'fusion_rule': 'str'
    }

    attribute_map = {
        'vector': 'vector',
        'fusion_rule': 'fusionRule'
    }

    def __init__(self, vector=None, fusion_rule='default'):
        """PutDataRequest - a model defined in Swagger"""
        self._vector = None
        self._fusion_rule = None
        self.discriminator = None
        self.vector = vector
        if fusion_rule is not None:
            self.fusion_rule = fusion_rule

    @property
    def vector(self):
        """Gets the vector of this PutDataRequest.

        Updates to apply to the current fusion vector.

        :return: The vector of this PutDataRequest.
        :rtype: list[FusionFeature]
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """Sets the vector of this PutDataRequest.

        Updates to apply to the current fusion vector.

        :param vector: The vector of this PutDataRequest.
        :type: list[FusionFeature]
        """
        if vector is None:
            raise ValueError("Invalid value for `vector`, must not be `None`")

        self._vector = vector

    @property
    def fusion_rule(self):
        """Gets the fusion_rule of this PutDataRequest.

        If `submit`, the fusion vector will be submitted for inference on this request. If `nosubmit`, this request will not trigger an inference. If `default`, follow the rules for the submitted features.

        :return: The fusion_rule of this PutDataRequest.
        :rtype: str
        """
        return self._fusion_rule

    @fusion_rule.setter
    def fusion_rule(self, fusion_rule):
        """Sets the fusion_rule of this PutDataRequest.

        If `submit`, the fusion vector will be submitted for inference on this request. If `nosubmit`, this request will not trigger an inference. If `default`, follow the rules for the submitted features.

        :param fusion_rule: The fusion_rule of this PutDataRequest.
        :type: str
        """
        allowed_values = ["default", "submit", "nosubmit"]
        if fusion_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `fusion_rule` ({0}), must be one of {1}"
                .format(fusion_rule, allowed_values)
            )

        self._fusion_rule = fusion_rule

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
        if issubclass(PutDataRequest, dict):
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
        if not isinstance(other, PutDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
