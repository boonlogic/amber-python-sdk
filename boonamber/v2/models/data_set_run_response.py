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

class DataSetRunResponse(object):
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
        'status': 'str',
        'message': 'str',
        'progress': 'float',
        'testing_results_url': 'str',
        'features': 'list[PresignedURL]',
        'results': 'list[PresignedURL]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'progress': 'progress',
        'testing_results_url': 'testingResultsUrl',
        'features': 'features',
        'results': 'results'
    }

    def __init__(self, status='None', message=None, progress=None, testing_results_url=None, features=None, results=None):
        """DataSetRunResponse - a model defined in Swagger"""
        self._status = None
        self._message = None
        self._progress = None
        self._testing_results_url = None
        self._features = None
        self._results = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if progress is not None:
            self.progress = progress
        if testing_results_url is not None:
            self.testing_results_url = testing_results_url
        if features is not None:
            self.features = features
        if results is not None:
            self.results = results

    @property
    def status(self):
        """Gets the status of this DataSetRunResponse.


        :return: The status of this DataSetRunResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataSetRunResponse.


        :param status: The status of this DataSetRunResponse.
        :type: str
        """
        allowed_values = ["None", "Error", "Training", "Trained", "Testing", "Tested"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this DataSetRunResponse.

        Error description

        :return: The message of this DataSetRunResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DataSetRunResponse.

        Error description

        :param message: The message of this DataSetRunResponse.
        :type: str
        """

        self._message = message

    @property
    def progress(self):
        """Gets the progress of this DataSetRunResponse.


        :return: The progress of this DataSetRunResponse.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DataSetRunResponse.


        :param progress: The progress of this DataSetRunResponse.
        :type: float
        """

        self._progress = progress

    @property
    def testing_results_url(self):
        """Gets the testing_results_url of this DataSetRunResponse.

        url used for downloading test data plus analytics

        :return: The testing_results_url of this DataSetRunResponse.
        :rtype: str
        """
        return self._testing_results_url

    @testing_results_url.setter
    def testing_results_url(self, testing_results_url):
        """Sets the testing_results_url of this DataSetRunResponse.

        url used for downloading test data plus analytics

        :param testing_results_url: The testing_results_url of this DataSetRunResponse.
        :type: str
        """

        self._testing_results_url = testing_results_url

    @property
    def features(self):
        """Gets the features of this DataSetRunResponse.


        :return: The features of this DataSetRunResponse.
        :rtype: list[PresignedURL]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this DataSetRunResponse.


        :param features: The features of this DataSetRunResponse.
        :type: list[PresignedURL]
        """

        self._features = features

    @property
    def results(self):
        """Gets the results of this DataSetRunResponse.


        :return: The results of this DataSetRunResponse.
        :rtype: list[PresignedURL]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DataSetRunResponse.


        :param results: The results of this DataSetRunResponse.
        :type: list[PresignedURL]
        """

        self._results = results

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
        if issubclass(DataSetRunResponse, dict):
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
        if not isinstance(other, DataSetRunResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other