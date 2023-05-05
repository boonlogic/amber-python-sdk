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

class MAP(object):
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
        'm_autotune_range': 'bool',
        'm_autotune_pv': 'bool',
        'm_autotune_by_features': 'bool',
        'm_max_clusters': 'float',
        'm_features_to_tune_array': 'list[float]'
    }

    attribute_map = {
        'version_number': 'versionNumber',
        'm_autotune_range': 'm_AutotuneRange',
        'm_autotune_pv': 'm_AutotunePV',
        'm_autotune_by_features': 'm_AutotuneByFeatures',
        'm_max_clusters': 'm_MaxClusters',
        'm_features_to_tune_array': 'm_FeaturesToTuneArray'
    }

    def __init__(self, version_number=None, m_autotune_range=None, m_autotune_pv=None, m_autotune_by_features=None, m_max_clusters=None, m_features_to_tune_array=None):
        """MAP - a model defined in Swagger"""
        self._version_number = None
        self._m_autotune_range = None
        self._m_autotune_pv = None
        self._m_autotune_by_features = None
        self._m_max_clusters = None
        self._m_features_to_tune_array = None
        self.discriminator = None
        if version_number is not None:
            self.version_number = version_number
        self.m_autotune_range = m_autotune_range
        self.m_autotune_pv = m_autotune_pv
        self.m_autotune_by_features = m_autotune_by_features
        if m_max_clusters is not None:
            self.m_max_clusters = m_max_clusters
        if m_features_to_tune_array is not None:
            self.m_features_to_tune_array = m_features_to_tune_array

    @property
    def version_number(self):
        """Gets the version_number of this MAP.


        :return: The version_number of this MAP.
        :rtype: VersionNumber
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this MAP.


        :param version_number: The version_number of this MAP.
        :type: VersionNumber
        """

        self._version_number = version_number

    @property
    def m_autotune_range(self):
        """Gets the m_autotune_range of this MAP.


        :return: The m_autotune_range of this MAP.
        :rtype: bool
        """
        return self._m_autotune_range

    @m_autotune_range.setter
    def m_autotune_range(self, m_autotune_range):
        """Sets the m_autotune_range of this MAP.


        :param m_autotune_range: The m_autotune_range of this MAP.
        :type: bool
        """
        if m_autotune_range is None:
            raise ValueError("Invalid value for `m_autotune_range`, must not be `None`")

        self._m_autotune_range = m_autotune_range

    @property
    def m_autotune_pv(self):
        """Gets the m_autotune_pv of this MAP.


        :return: The m_autotune_pv of this MAP.
        :rtype: bool
        """
        return self._m_autotune_pv

    @m_autotune_pv.setter
    def m_autotune_pv(self, m_autotune_pv):
        """Sets the m_autotune_pv of this MAP.


        :param m_autotune_pv: The m_autotune_pv of this MAP.
        :type: bool
        """
        if m_autotune_pv is None:
            raise ValueError("Invalid value for `m_autotune_pv`, must not be `None`")

        self._m_autotune_pv = m_autotune_pv

    @property
    def m_autotune_by_features(self):
        """Gets the m_autotune_by_features of this MAP.


        :return: The m_autotune_by_features of this MAP.
        :rtype: bool
        """
        return self._m_autotune_by_features

    @m_autotune_by_features.setter
    def m_autotune_by_features(self, m_autotune_by_features):
        """Sets the m_autotune_by_features of this MAP.


        :param m_autotune_by_features: The m_autotune_by_features of this MAP.
        :type: bool
        """
        if m_autotune_by_features is None:
            raise ValueError("Invalid value for `m_autotune_by_features`, must not be `None`")

        self._m_autotune_by_features = m_autotune_by_features

    @property
    def m_max_clusters(self):
        """Gets the m_max_clusters of this MAP.


        :return: The m_max_clusters of this MAP.
        :rtype: float
        """
        return self._m_max_clusters

    @m_max_clusters.setter
    def m_max_clusters(self, m_max_clusters):
        """Sets the m_max_clusters of this MAP.


        :param m_max_clusters: The m_max_clusters of this MAP.
        :type: float
        """

        self._m_max_clusters = m_max_clusters

    @property
    def m_features_to_tune_array(self):
        """Gets the m_features_to_tune_array of this MAP.


        :return: The m_features_to_tune_array of this MAP.
        :rtype: list[float]
        """
        return self._m_features_to_tune_array

    @m_features_to_tune_array.setter
    def m_features_to_tune_array(self, m_features_to_tune_array):
        """Sets the m_features_to_tune_array of this MAP.


        :param m_features_to_tune_array: The m_features_to_tune_array of this MAP.
        :type: list[float]
        """

        self._m_features_to_tune_array = m_features_to_tune_array

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
        if issubclass(MAP, dict):
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
        if not isinstance(other, MAP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other