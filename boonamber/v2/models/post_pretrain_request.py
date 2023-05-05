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

class PostPretrainRequest(object):
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
        'data': 'str',
        'format': 'str'
    }

    attribute_map = {
        'data': 'data',
        'format': 'format'
    }

    def __init__(self, data=None, format='csv'):
        """PostPretrainRequest - a model defined in Swagger"""
        self._data = None
        self._format = None
        self.discriminator = None
        self.data = data
        if format is not None:
            self.format = format

    @property
    def data(self):
        """Gets the data of this PostPretrainRequest.

        Data in one of two formats: 1) A flat list of comma-separated values. 2) The string that results from flattening the dataset, packing the values into a byte buffer as float32s (little-endian), and base-64 encoding the buffer.  Datasets which are too large to send in one request may be sent in multiple chunks using the header parameters for chunked uploads (`txnId` and `chunkspec`).  The total number of data values sent for pretraining must be a multiple of the number of features in the configuration.

        :return: The data of this PostPretrainRequest.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PostPretrainRequest.

        Data in one of two formats: 1) A flat list of comma-separated values. 2) The string that results from flattening the dataset, packing the values into a byte buffer as float32s (little-endian), and base-64 encoding the buffer.  Datasets which are too large to send in one request may be sent in multiple chunks using the header parameters for chunked uploads (`txnId` and `chunkspec`).  The total number of data values sent for pretraining must be a multiple of the number of features in the configuration.

        :param data: The data of this PostPretrainRequest.
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def format(self):
        """Gets the format of this PostPretrainRequest.

        Format specifier for `data`.

        :return: The format of this PostPretrainRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PostPretrainRequest.

        Format specifier for `data`.

        :param format: The format of this PostPretrainRequest.
        :type: str
        """
        allowed_values = ["csv", "b64float", "packed-float"]
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

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
        if issubclass(PostPretrainRequest, dict):
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
        if not isinstance(other, PostPretrainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
