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

class MBufferStats(object):
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
        'total_bytes_written': 'float',
        'total_bytes_processed': 'float',
        'load_buffer_length': 'float',
        'load_buffer_capacity': 'float'
    }

    attribute_map = {
        'version_number': 'versionNumber',
        'total_bytes_written': 'TotalBytesWritten',
        'total_bytes_processed': 'TotalBytesProcessed',
        'load_buffer_length': 'LoadBufferLength',
        'load_buffer_capacity': 'LoadBufferCapacity'
    }

    def __init__(self, version_number=None, total_bytes_written=None, total_bytes_processed=None, load_buffer_length=None, load_buffer_capacity=None):
        """MBufferStats - a model defined in Swagger"""
        self._version_number = None
        self._total_bytes_written = None
        self._total_bytes_processed = None
        self._load_buffer_length = None
        self._load_buffer_capacity = None
        self.discriminator = None
        if version_number is not None:
            self.version_number = version_number
        if total_bytes_written is not None:
            self.total_bytes_written = total_bytes_written
        if total_bytes_processed is not None:
            self.total_bytes_processed = total_bytes_processed
        if load_buffer_length is not None:
            self.load_buffer_length = load_buffer_length
        if load_buffer_capacity is not None:
            self.load_buffer_capacity = load_buffer_capacity

    @property
    def version_number(self):
        """Gets the version_number of this MBufferStats.


        :return: The version_number of this MBufferStats.
        :rtype: VersionNumber
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this MBufferStats.


        :param version_number: The version_number of this MBufferStats.
        :type: VersionNumber
        """

        self._version_number = version_number

    @property
    def total_bytes_written(self):
        """Gets the total_bytes_written of this MBufferStats.


        :return: The total_bytes_written of this MBufferStats.
        :rtype: float
        """
        return self._total_bytes_written

    @total_bytes_written.setter
    def total_bytes_written(self, total_bytes_written):
        """Sets the total_bytes_written of this MBufferStats.


        :param total_bytes_written: The total_bytes_written of this MBufferStats.
        :type: float
        """

        self._total_bytes_written = total_bytes_written

    @property
    def total_bytes_processed(self):
        """Gets the total_bytes_processed of this MBufferStats.


        :return: The total_bytes_processed of this MBufferStats.
        :rtype: float
        """
        return self._total_bytes_processed

    @total_bytes_processed.setter
    def total_bytes_processed(self, total_bytes_processed):
        """Sets the total_bytes_processed of this MBufferStats.


        :param total_bytes_processed: The total_bytes_processed of this MBufferStats.
        :type: float
        """

        self._total_bytes_processed = total_bytes_processed

    @property
    def load_buffer_length(self):
        """Gets the load_buffer_length of this MBufferStats.


        :return: The load_buffer_length of this MBufferStats.
        :rtype: float
        """
        return self._load_buffer_length

    @load_buffer_length.setter
    def load_buffer_length(self, load_buffer_length):
        """Sets the load_buffer_length of this MBufferStats.


        :param load_buffer_length: The load_buffer_length of this MBufferStats.
        :type: float
        """

        self._load_buffer_length = load_buffer_length

    @property
    def load_buffer_capacity(self):
        """Gets the load_buffer_capacity of this MBufferStats.


        :return: The load_buffer_capacity of this MBufferStats.
        :rtype: float
        """
        return self._load_buffer_capacity

    @load_buffer_capacity.setter
    def load_buffer_capacity(self, load_buffer_capacity):
        """Sets the load_buffer_capacity of this MBufferStats.


        :param load_buffer_capacity: The load_buffer_capacity of this MBufferStats.
        :type: float
        """

        self._load_buffer_capacity = load_buffer_capacity

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
        if issubclass(MBufferStats, dict):
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
        if not isinstance(other, MBufferStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
