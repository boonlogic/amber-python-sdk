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

class MAutotune(object):
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
        'm_autotuning_in_progress': 'bool',
        'm_percent_complete': 'float',
        'm_autotuning_succeeded': 'bool',
        'm_num_patterns_to_autotune': 'float',
        'm_error_string_buffer': 'str',
        'm_features_to_tune_array': 'list[bool]',
        'm_ncp': 'MNCP',
        'm_ap': 'MAP'
    }

    attribute_map = {
        'version_number': 'versionNumber',
        'm_autotuning_in_progress': 'm_AutotuningInProgress',
        'm_percent_complete': 'm_PercentComplete',
        'm_autotuning_succeeded': 'm_AutotuningSucceeded',
        'm_num_patterns_to_autotune': 'm_NumPatternsToAutotune',
        'm_error_string_buffer': 'm_ErrorStringBuffer',
        'm_features_to_tune_array': 'm_FeaturesToTuneArray',
        'm_ncp': 'm_NCP',
        'm_ap': 'm_AP'
    }

    def __init__(self, version_number=None, m_autotuning_in_progress=None, m_percent_complete=None, m_autotuning_succeeded=None, m_num_patterns_to_autotune=None, m_error_string_buffer=None, m_features_to_tune_array=None, m_ncp=None, m_ap=None):
        """MAutotune - a model defined in Swagger"""
        self._version_number = None
        self._m_autotuning_in_progress = None
        self._m_percent_complete = None
        self._m_autotuning_succeeded = None
        self._m_num_patterns_to_autotune = None
        self._m_error_string_buffer = None
        self._m_features_to_tune_array = None
        self._m_ncp = None
        self._m_ap = None
        self.discriminator = None
        if version_number is not None:
            self.version_number = version_number
        if m_autotuning_in_progress is not None:
            self.m_autotuning_in_progress = m_autotuning_in_progress
        if m_percent_complete is not None:
            self.m_percent_complete = m_percent_complete
        if m_autotuning_succeeded is not None:
            self.m_autotuning_succeeded = m_autotuning_succeeded
        if m_num_patterns_to_autotune is not None:
            self.m_num_patterns_to_autotune = m_num_patterns_to_autotune
        if m_error_string_buffer is not None:
            self.m_error_string_buffer = m_error_string_buffer
        if m_features_to_tune_array is not None:
            self.m_features_to_tune_array = m_features_to_tune_array
        if m_ncp is not None:
            self.m_ncp = m_ncp
        self.m_ap = m_ap

    @property
    def version_number(self):
        """Gets the version_number of this MAutotune.


        :return: The version_number of this MAutotune.
        :rtype: VersionNumber
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this MAutotune.


        :param version_number: The version_number of this MAutotune.
        :type: VersionNumber
        """

        self._version_number = version_number

    @property
    def m_autotuning_in_progress(self):
        """Gets the m_autotuning_in_progress of this MAutotune.


        :return: The m_autotuning_in_progress of this MAutotune.
        :rtype: bool
        """
        return self._m_autotuning_in_progress

    @m_autotuning_in_progress.setter
    def m_autotuning_in_progress(self, m_autotuning_in_progress):
        """Sets the m_autotuning_in_progress of this MAutotune.


        :param m_autotuning_in_progress: The m_autotuning_in_progress of this MAutotune.
        :type: bool
        """

        self._m_autotuning_in_progress = m_autotuning_in_progress

    @property
    def m_percent_complete(self):
        """Gets the m_percent_complete of this MAutotune.


        :return: The m_percent_complete of this MAutotune.
        :rtype: float
        """
        return self._m_percent_complete

    @m_percent_complete.setter
    def m_percent_complete(self, m_percent_complete):
        """Sets the m_percent_complete of this MAutotune.


        :param m_percent_complete: The m_percent_complete of this MAutotune.
        :type: float
        """

        self._m_percent_complete = m_percent_complete

    @property
    def m_autotuning_succeeded(self):
        """Gets the m_autotuning_succeeded of this MAutotune.


        :return: The m_autotuning_succeeded of this MAutotune.
        :rtype: bool
        """
        return self._m_autotuning_succeeded

    @m_autotuning_succeeded.setter
    def m_autotuning_succeeded(self, m_autotuning_succeeded):
        """Sets the m_autotuning_succeeded of this MAutotune.


        :param m_autotuning_succeeded: The m_autotuning_succeeded of this MAutotune.
        :type: bool
        """

        self._m_autotuning_succeeded = m_autotuning_succeeded

    @property
    def m_num_patterns_to_autotune(self):
        """Gets the m_num_patterns_to_autotune of this MAutotune.


        :return: The m_num_patterns_to_autotune of this MAutotune.
        :rtype: float
        """
        return self._m_num_patterns_to_autotune

    @m_num_patterns_to_autotune.setter
    def m_num_patterns_to_autotune(self, m_num_patterns_to_autotune):
        """Sets the m_num_patterns_to_autotune of this MAutotune.


        :param m_num_patterns_to_autotune: The m_num_patterns_to_autotune of this MAutotune.
        :type: float
        """

        self._m_num_patterns_to_autotune = m_num_patterns_to_autotune

    @property
    def m_error_string_buffer(self):
        """Gets the m_error_string_buffer of this MAutotune.


        :return: The m_error_string_buffer of this MAutotune.
        :rtype: str
        """
        return self._m_error_string_buffer

    @m_error_string_buffer.setter
    def m_error_string_buffer(self, m_error_string_buffer):
        """Sets the m_error_string_buffer of this MAutotune.


        :param m_error_string_buffer: The m_error_string_buffer of this MAutotune.
        :type: str
        """

        self._m_error_string_buffer = m_error_string_buffer

    @property
    def m_features_to_tune_array(self):
        """Gets the m_features_to_tune_array of this MAutotune.


        :return: The m_features_to_tune_array of this MAutotune.
        :rtype: list[bool]
        """
        return self._m_features_to_tune_array

    @m_features_to_tune_array.setter
    def m_features_to_tune_array(self, m_features_to_tune_array):
        """Sets the m_features_to_tune_array of this MAutotune.


        :param m_features_to_tune_array: The m_features_to_tune_array of this MAutotune.
        :type: list[bool]
        """

        self._m_features_to_tune_array = m_features_to_tune_array

    @property
    def m_ncp(self):
        """Gets the m_ncp of this MAutotune.


        :return: The m_ncp of this MAutotune.
        :rtype: MNCP
        """
        return self._m_ncp

    @m_ncp.setter
    def m_ncp(self, m_ncp):
        """Sets the m_ncp of this MAutotune.


        :param m_ncp: The m_ncp of this MAutotune.
        :type: MNCP
        """

        self._m_ncp = m_ncp

    @property
    def m_ap(self):
        """Gets the m_ap of this MAutotune.


        :return: The m_ap of this MAutotune.
        :rtype: MAP
        """
        return self._m_ap

    @m_ap.setter
    def m_ap(self, m_ap):
        """Sets the m_ap of this MAutotune.


        :param m_ap: The m_ap of this MAutotune.
        :type: MAP
        """
        if m_ap is None:
            raise ValueError("Invalid value for `m_ap`, must not be `None`")

        self._m_ap = m_ap

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
        if issubclass(MAutotune, dict):
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
        if not isinstance(other, MAutotune):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
