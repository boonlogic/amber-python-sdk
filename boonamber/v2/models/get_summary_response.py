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

class GetSummaryResponse(object):
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
        'magic_number': 'MagicNumber',
        'version_number': 'VersionNumber',
        'm_nano': 'MNano',
        'm_buffer_stats': 'MBufferStats',
        'm_autotune': 'MAutotune',
        'm_autotuning_elbow_cluster_counts': 'list[float]',
        'm_autotuning_elbow_pv_array': 'list[float]',
        'm_streaming_parameters': 'MStreamingParameters',
        'm_amber_status': 'MAmberStatus',
        'm_training': 'MTraining',
        'm_anomaly_threshold': 'float',
        'm_amber_warning_critical_value': 'float',
        'm_amber_alert_critical_value': 'float',
        'm_error_string_buffer': 'str',
        'm_clustering_parameters_initialized': 'bool',
        'm_streaming_mode': 'bool',
        'm_streaming_mode_status': 'float',
        'm_modified_at': 'float',
        'm_anomaly_metric_by_anomaly_count': 'list[float]',
        'm_recent_anomaly_count': 'float',
        'm_results_id_array': 'list[float]',
        'm_training_samples': 'MRecentSamples',
        'm_recent_samples': 'MRecentSamples',
        'm_recent_raw_samples': 'MRecentSamples',
        'm_recent_times': 'MRecentTimes',
        'm_recent_sis': 'MRecentAnalytics',
        'm_recent_ris': 'MRecentAnalytics',
        'm_recent_ads': 'MRecentAnalytics',
        'm_recent_ahs': 'MRecentAnalytics',
        'm_recent_ids': 'MRecentIDs',
        'm_recent_ams': 'MRecentAMs',
        'm_recent_aws': 'MRecentAnalytics'
    }

    attribute_map = {
        'magic_number': 'magicNumber',
        'version_number': 'versionNumber',
        'm_nano': 'm_Nano',
        'm_buffer_stats': 'm_BufferStats',
        'm_autotune': 'm_Autotune',
        'm_autotuning_elbow_cluster_counts': 'm_AutotuningElbowClusterCounts',
        'm_autotuning_elbow_pv_array': 'm_AutotuningElbowPVArray',
        'm_streaming_parameters': 'm_StreamingParameters',
        'm_amber_status': 'm_AmberStatus',
        'm_training': 'm_Training',
        'm_anomaly_threshold': 'm_AnomalyThreshold',
        'm_amber_warning_critical_value': 'm_AmberWarningCriticalValue',
        'm_amber_alert_critical_value': 'm_AmberAlertCriticalValue',
        'm_error_string_buffer': 'm_ErrorStringBuffer',
        'm_clustering_parameters_initialized': 'm_ClusteringParametersInitialized',
        'm_streaming_mode': 'm_StreamingMode',
        'm_streaming_mode_status': 'm_StreamingModeStatus',
        'm_modified_at': 'm_ModifiedAt',
        'm_anomaly_metric_by_anomaly_count': 'm_AnomalyMetricByAnomalyCount',
        'm_recent_anomaly_count': 'm_RecentAnomalyCount',
        'm_results_id_array': 'm_ResultsIDArray',
        'm_training_samples': 'm_TrainingSamples',
        'm_recent_samples': 'm_RecentSamples',
        'm_recent_raw_samples': 'm_RecentRawSamples',
        'm_recent_times': 'm_RecentTimes',
        'm_recent_sis': 'm_RecentSIs',
        'm_recent_ris': 'm_RecentRIs',
        'm_recent_ads': 'm_RecentADs',
        'm_recent_ahs': 'm_RecentAHs',
        'm_recent_ids': 'm_RecentIDs',
        'm_recent_ams': 'm_RecentAMs',
        'm_recent_aws': 'm_RecentAWs'
    }

    def __init__(self, magic_number=None, version_number=None, m_nano=None, m_buffer_stats=None, m_autotune=None, m_autotuning_elbow_cluster_counts=None, m_autotuning_elbow_pv_array=None, m_streaming_parameters=None, m_amber_status=None, m_training=None, m_anomaly_threshold=None, m_amber_warning_critical_value=None, m_amber_alert_critical_value=None, m_error_string_buffer=None, m_clustering_parameters_initialized=None, m_streaming_mode=None, m_streaming_mode_status=None, m_modified_at=None, m_anomaly_metric_by_anomaly_count=None, m_recent_anomaly_count=None, m_results_id_array=None, m_training_samples=None, m_recent_samples=None, m_recent_raw_samples=None, m_recent_times=None, m_recent_sis=None, m_recent_ris=None, m_recent_ads=None, m_recent_ahs=None, m_recent_ids=None, m_recent_ams=None, m_recent_aws=None):
        """GetSummaryResponse - a model defined in Swagger"""
        self._magic_number = None
        self._version_number = None
        self._m_nano = None
        self._m_buffer_stats = None
        self._m_autotune = None
        self._m_autotuning_elbow_cluster_counts = None
        self._m_autotuning_elbow_pv_array = None
        self._m_streaming_parameters = None
        self._m_amber_status = None
        self._m_training = None
        self._m_anomaly_threshold = None
        self._m_amber_warning_critical_value = None
        self._m_amber_alert_critical_value = None
        self._m_error_string_buffer = None
        self._m_clustering_parameters_initialized = None
        self._m_streaming_mode = None
        self._m_streaming_mode_status = None
        self._m_modified_at = None
        self._m_anomaly_metric_by_anomaly_count = None
        self._m_recent_anomaly_count = None
        self._m_results_id_array = None
        self._m_training_samples = None
        self._m_recent_samples = None
        self._m_recent_raw_samples = None
        self._m_recent_times = None
        self._m_recent_sis = None
        self._m_recent_ris = None
        self._m_recent_ads = None
        self._m_recent_ahs = None
        self._m_recent_ids = None
        self._m_recent_ams = None
        self._m_recent_aws = None
        self.discriminator = None
        if magic_number is not None:
            self.magic_number = magic_number
        if version_number is not None:
            self.version_number = version_number
        self.m_nano = m_nano
        if m_buffer_stats is not None:
            self.m_buffer_stats = m_buffer_stats
        self.m_autotune = m_autotune
        self.m_autotuning_elbow_cluster_counts = m_autotuning_elbow_cluster_counts
        self.m_autotuning_elbow_pv_array = m_autotuning_elbow_pv_array
        self.m_streaming_parameters = m_streaming_parameters
        self.m_amber_status = m_amber_status
        self.m_training = m_training
        self.m_anomaly_threshold = m_anomaly_threshold
        self.m_amber_warning_critical_value = m_amber_warning_critical_value
        self.m_amber_alert_critical_value = m_amber_alert_critical_value
        if m_error_string_buffer is not None:
            self.m_error_string_buffer = m_error_string_buffer
        if m_clustering_parameters_initialized is not None:
            self.m_clustering_parameters_initialized = m_clustering_parameters_initialized
        if m_streaming_mode is not None:
            self.m_streaming_mode = m_streaming_mode
        if m_streaming_mode_status is not None:
            self.m_streaming_mode_status = m_streaming_mode_status
        if m_modified_at is not None:
            self.m_modified_at = m_modified_at
        if m_anomaly_metric_by_anomaly_count is not None:
            self.m_anomaly_metric_by_anomaly_count = m_anomaly_metric_by_anomaly_count
        if m_recent_anomaly_count is not None:
            self.m_recent_anomaly_count = m_recent_anomaly_count
        if m_results_id_array is not None:
            self.m_results_id_array = m_results_id_array
        if m_training_samples is not None:
            self.m_training_samples = m_training_samples
        self.m_recent_samples = m_recent_samples
        self.m_recent_raw_samples = m_recent_raw_samples
        self.m_recent_times = m_recent_times
        self.m_recent_sis = m_recent_sis
        self.m_recent_ris = m_recent_ris
        self.m_recent_ads = m_recent_ads
        self.m_recent_ahs = m_recent_ahs
        if m_recent_ids is not None:
            self.m_recent_ids = m_recent_ids
        if m_recent_ams is not None:
            self.m_recent_ams = m_recent_ams
        self.m_recent_aws = m_recent_aws

    @property
    def magic_number(self):
        """Gets the magic_number of this GetSummaryResponse.


        :return: The magic_number of this GetSummaryResponse.
        :rtype: MagicNumber
        """
        return self._magic_number

    @magic_number.setter
    def magic_number(self, magic_number):
        """Sets the magic_number of this GetSummaryResponse.


        :param magic_number: The magic_number of this GetSummaryResponse.
        :type: MagicNumber
        """

        self._magic_number = magic_number

    @property
    def version_number(self):
        """Gets the version_number of this GetSummaryResponse.


        :return: The version_number of this GetSummaryResponse.
        :rtype: VersionNumber
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this GetSummaryResponse.


        :param version_number: The version_number of this GetSummaryResponse.
        :type: VersionNumber
        """

        self._version_number = version_number

    @property
    def m_nano(self):
        """Gets the m_nano of this GetSummaryResponse.


        :return: The m_nano of this GetSummaryResponse.
        :rtype: MNano
        """
        return self._m_nano

    @m_nano.setter
    def m_nano(self, m_nano):
        """Sets the m_nano of this GetSummaryResponse.


        :param m_nano: The m_nano of this GetSummaryResponse.
        :type: MNano
        """
        if m_nano is None:
            raise ValueError("Invalid value for `m_nano`, must not be `None`")

        self._m_nano = m_nano

    @property
    def m_buffer_stats(self):
        """Gets the m_buffer_stats of this GetSummaryResponse.


        :return: The m_buffer_stats of this GetSummaryResponse.
        :rtype: MBufferStats
        """
        return self._m_buffer_stats

    @m_buffer_stats.setter
    def m_buffer_stats(self, m_buffer_stats):
        """Sets the m_buffer_stats of this GetSummaryResponse.


        :param m_buffer_stats: The m_buffer_stats of this GetSummaryResponse.
        :type: MBufferStats
        """

        self._m_buffer_stats = m_buffer_stats

    @property
    def m_autotune(self):
        """Gets the m_autotune of this GetSummaryResponse.


        :return: The m_autotune of this GetSummaryResponse.
        :rtype: MAutotune
        """
        return self._m_autotune

    @m_autotune.setter
    def m_autotune(self, m_autotune):
        """Sets the m_autotune of this GetSummaryResponse.


        :param m_autotune: The m_autotune of this GetSummaryResponse.
        :type: MAutotune
        """
        if m_autotune is None:
            raise ValueError("Invalid value for `m_autotune`, must not be `None`")

        self._m_autotune = m_autotune

    @property
    def m_autotuning_elbow_cluster_counts(self):
        """Gets the m_autotuning_elbow_cluster_counts of this GetSummaryResponse.


        :return: The m_autotuning_elbow_cluster_counts of this GetSummaryResponse.
        :rtype: list[float]
        """
        return self._m_autotuning_elbow_cluster_counts

    @m_autotuning_elbow_cluster_counts.setter
    def m_autotuning_elbow_cluster_counts(self, m_autotuning_elbow_cluster_counts):
        """Sets the m_autotuning_elbow_cluster_counts of this GetSummaryResponse.


        :param m_autotuning_elbow_cluster_counts: The m_autotuning_elbow_cluster_counts of this GetSummaryResponse.
        :type: list[float]
        """
        if m_autotuning_elbow_cluster_counts is None:
            raise ValueError("Invalid value for `m_autotuning_elbow_cluster_counts`, must not be `None`")

        self._m_autotuning_elbow_cluster_counts = m_autotuning_elbow_cluster_counts

    @property
    def m_autotuning_elbow_pv_array(self):
        """Gets the m_autotuning_elbow_pv_array of this GetSummaryResponse.


        :return: The m_autotuning_elbow_pv_array of this GetSummaryResponse.
        :rtype: list[float]
        """
        return self._m_autotuning_elbow_pv_array

    @m_autotuning_elbow_pv_array.setter
    def m_autotuning_elbow_pv_array(self, m_autotuning_elbow_pv_array):
        """Sets the m_autotuning_elbow_pv_array of this GetSummaryResponse.


        :param m_autotuning_elbow_pv_array: The m_autotuning_elbow_pv_array of this GetSummaryResponse.
        :type: list[float]
        """
        if m_autotuning_elbow_pv_array is None:
            raise ValueError("Invalid value for `m_autotuning_elbow_pv_array`, must not be `None`")

        self._m_autotuning_elbow_pv_array = m_autotuning_elbow_pv_array

    @property
    def m_streaming_parameters(self):
        """Gets the m_streaming_parameters of this GetSummaryResponse.


        :return: The m_streaming_parameters of this GetSummaryResponse.
        :rtype: MStreamingParameters
        """
        return self._m_streaming_parameters

    @m_streaming_parameters.setter
    def m_streaming_parameters(self, m_streaming_parameters):
        """Sets the m_streaming_parameters of this GetSummaryResponse.


        :param m_streaming_parameters: The m_streaming_parameters of this GetSummaryResponse.
        :type: MStreamingParameters
        """
        if m_streaming_parameters is None:
            raise ValueError("Invalid value for `m_streaming_parameters`, must not be `None`")

        self._m_streaming_parameters = m_streaming_parameters

    @property
    def m_amber_status(self):
        """Gets the m_amber_status of this GetSummaryResponse.


        :return: The m_amber_status of this GetSummaryResponse.
        :rtype: MAmberStatus
        """
        return self._m_amber_status

    @m_amber_status.setter
    def m_amber_status(self, m_amber_status):
        """Sets the m_amber_status of this GetSummaryResponse.


        :param m_amber_status: The m_amber_status of this GetSummaryResponse.
        :type: MAmberStatus
        """
        if m_amber_status is None:
            raise ValueError("Invalid value for `m_amber_status`, must not be `None`")

        self._m_amber_status = m_amber_status

    @property
    def m_training(self):
        """Gets the m_training of this GetSummaryResponse.


        :return: The m_training of this GetSummaryResponse.
        :rtype: MTraining
        """
        return self._m_training

    @m_training.setter
    def m_training(self, m_training):
        """Sets the m_training of this GetSummaryResponse.


        :param m_training: The m_training of this GetSummaryResponse.
        :type: MTraining
        """
        if m_training is None:
            raise ValueError("Invalid value for `m_training`, must not be `None`")

        self._m_training = m_training

    @property
    def m_anomaly_threshold(self):
        """Gets the m_anomaly_threshold of this GetSummaryResponse.


        :return: The m_anomaly_threshold of this GetSummaryResponse.
        :rtype: float
        """
        return self._m_anomaly_threshold

    @m_anomaly_threshold.setter
    def m_anomaly_threshold(self, m_anomaly_threshold):
        """Sets the m_anomaly_threshold of this GetSummaryResponse.


        :param m_anomaly_threshold: The m_anomaly_threshold of this GetSummaryResponse.
        :type: float
        """
        if m_anomaly_threshold is None:
            raise ValueError("Invalid value for `m_anomaly_threshold`, must not be `None`")

        self._m_anomaly_threshold = m_anomaly_threshold

    @property
    def m_amber_warning_critical_value(self):
        """Gets the m_amber_warning_critical_value of this GetSummaryResponse.


        :return: The m_amber_warning_critical_value of this GetSummaryResponse.
        :rtype: float
        """
        return self._m_amber_warning_critical_value

    @m_amber_warning_critical_value.setter
    def m_amber_warning_critical_value(self, m_amber_warning_critical_value):
        """Sets the m_amber_warning_critical_value of this GetSummaryResponse.


        :param m_amber_warning_critical_value: The m_amber_warning_critical_value of this GetSummaryResponse.
        :type: float
        """
        if m_amber_warning_critical_value is None:
            raise ValueError("Invalid value for `m_amber_warning_critical_value`, must not be `None`")

        self._m_amber_warning_critical_value = m_amber_warning_critical_value

    @property
    def m_amber_alert_critical_value(self):
        """Gets the m_amber_alert_critical_value of this GetSummaryResponse.


        :return: The m_amber_alert_critical_value of this GetSummaryResponse.
        :rtype: float
        """
        return self._m_amber_alert_critical_value

    @m_amber_alert_critical_value.setter
    def m_amber_alert_critical_value(self, m_amber_alert_critical_value):
        """Sets the m_amber_alert_critical_value of this GetSummaryResponse.


        :param m_amber_alert_critical_value: The m_amber_alert_critical_value of this GetSummaryResponse.
        :type: float
        """
        if m_amber_alert_critical_value is None:
            raise ValueError("Invalid value for `m_amber_alert_critical_value`, must not be `None`")

        self._m_amber_alert_critical_value = m_amber_alert_critical_value

    @property
    def m_error_string_buffer(self):
        """Gets the m_error_string_buffer of this GetSummaryResponse.


        :return: The m_error_string_buffer of this GetSummaryResponse.
        :rtype: str
        """
        return self._m_error_string_buffer

    @m_error_string_buffer.setter
    def m_error_string_buffer(self, m_error_string_buffer):
        """Sets the m_error_string_buffer of this GetSummaryResponse.


        :param m_error_string_buffer: The m_error_string_buffer of this GetSummaryResponse.
        :type: str
        """

        self._m_error_string_buffer = m_error_string_buffer

    @property
    def m_clustering_parameters_initialized(self):
        """Gets the m_clustering_parameters_initialized of this GetSummaryResponse.


        :return: The m_clustering_parameters_initialized of this GetSummaryResponse.
        :rtype: bool
        """
        return self._m_clustering_parameters_initialized

    @m_clustering_parameters_initialized.setter
    def m_clustering_parameters_initialized(self, m_clustering_parameters_initialized):
        """Sets the m_clustering_parameters_initialized of this GetSummaryResponse.


        :param m_clustering_parameters_initialized: The m_clustering_parameters_initialized of this GetSummaryResponse.
        :type: bool
        """

        self._m_clustering_parameters_initialized = m_clustering_parameters_initialized

    @property
    def m_streaming_mode(self):
        """Gets the m_streaming_mode of this GetSummaryResponse.


        :return: The m_streaming_mode of this GetSummaryResponse.
        :rtype: bool
        """
        return self._m_streaming_mode

    @m_streaming_mode.setter
    def m_streaming_mode(self, m_streaming_mode):
        """Sets the m_streaming_mode of this GetSummaryResponse.


        :param m_streaming_mode: The m_streaming_mode of this GetSummaryResponse.
        :type: bool
        """

        self._m_streaming_mode = m_streaming_mode

    @property
    def m_streaming_mode_status(self):
        """Gets the m_streaming_mode_status of this GetSummaryResponse.


        :return: The m_streaming_mode_status of this GetSummaryResponse.
        :rtype: float
        """
        return self._m_streaming_mode_status

    @m_streaming_mode_status.setter
    def m_streaming_mode_status(self, m_streaming_mode_status):
        """Sets the m_streaming_mode_status of this GetSummaryResponse.


        :param m_streaming_mode_status: The m_streaming_mode_status of this GetSummaryResponse.
        :type: float
        """

        self._m_streaming_mode_status = m_streaming_mode_status

    @property
    def m_modified_at(self):
        """Gets the m_modified_at of this GetSummaryResponse.


        :return: The m_modified_at of this GetSummaryResponse.
        :rtype: float
        """
        return self._m_modified_at

    @m_modified_at.setter
    def m_modified_at(self, m_modified_at):
        """Sets the m_modified_at of this GetSummaryResponse.


        :param m_modified_at: The m_modified_at of this GetSummaryResponse.
        :type: float
        """

        self._m_modified_at = m_modified_at

    @property
    def m_anomaly_metric_by_anomaly_count(self):
        """Gets the m_anomaly_metric_by_anomaly_count of this GetSummaryResponse.


        :return: The m_anomaly_metric_by_anomaly_count of this GetSummaryResponse.
        :rtype: list[float]
        """
        return self._m_anomaly_metric_by_anomaly_count

    @m_anomaly_metric_by_anomaly_count.setter
    def m_anomaly_metric_by_anomaly_count(self, m_anomaly_metric_by_anomaly_count):
        """Sets the m_anomaly_metric_by_anomaly_count of this GetSummaryResponse.


        :param m_anomaly_metric_by_anomaly_count: The m_anomaly_metric_by_anomaly_count of this GetSummaryResponse.
        :type: list[float]
        """

        self._m_anomaly_metric_by_anomaly_count = m_anomaly_metric_by_anomaly_count

    @property
    def m_recent_anomaly_count(self):
        """Gets the m_recent_anomaly_count of this GetSummaryResponse.


        :return: The m_recent_anomaly_count of this GetSummaryResponse.
        :rtype: float
        """
        return self._m_recent_anomaly_count

    @m_recent_anomaly_count.setter
    def m_recent_anomaly_count(self, m_recent_anomaly_count):
        """Sets the m_recent_anomaly_count of this GetSummaryResponse.


        :param m_recent_anomaly_count: The m_recent_anomaly_count of this GetSummaryResponse.
        :type: float
        """

        self._m_recent_anomaly_count = m_recent_anomaly_count

    @property
    def m_results_id_array(self):
        """Gets the m_results_id_array of this GetSummaryResponse.


        :return: The m_results_id_array of this GetSummaryResponse.
        :rtype: list[float]
        """
        return self._m_results_id_array

    @m_results_id_array.setter
    def m_results_id_array(self, m_results_id_array):
        """Sets the m_results_id_array of this GetSummaryResponse.


        :param m_results_id_array: The m_results_id_array of this GetSummaryResponse.
        :type: list[float]
        """

        self._m_results_id_array = m_results_id_array

    @property
    def m_training_samples(self):
        """Gets the m_training_samples of this GetSummaryResponse.


        :return: The m_training_samples of this GetSummaryResponse.
        :rtype: MRecentSamples
        """
        return self._m_training_samples

    @m_training_samples.setter
    def m_training_samples(self, m_training_samples):
        """Sets the m_training_samples of this GetSummaryResponse.


        :param m_training_samples: The m_training_samples of this GetSummaryResponse.
        :type: MRecentSamples
        """

        self._m_training_samples = m_training_samples

    @property
    def m_recent_samples(self):
        """Gets the m_recent_samples of this GetSummaryResponse.


        :return: The m_recent_samples of this GetSummaryResponse.
        :rtype: MRecentSamples
        """
        return self._m_recent_samples

    @m_recent_samples.setter
    def m_recent_samples(self, m_recent_samples):
        """Sets the m_recent_samples of this GetSummaryResponse.


        :param m_recent_samples: The m_recent_samples of this GetSummaryResponse.
        :type: MRecentSamples
        """
        if m_recent_samples is None:
            raise ValueError("Invalid value for `m_recent_samples`, must not be `None`")

        self._m_recent_samples = m_recent_samples

    @property
    def m_recent_raw_samples(self):
        """Gets the m_recent_raw_samples of this GetSummaryResponse.


        :return: The m_recent_raw_samples of this GetSummaryResponse.
        :rtype: MRecentSamples
        """
        return self._m_recent_raw_samples

    @m_recent_raw_samples.setter
    def m_recent_raw_samples(self, m_recent_raw_samples):
        """Sets the m_recent_raw_samples of this GetSummaryResponse.


        :param m_recent_raw_samples: The m_recent_raw_samples of this GetSummaryResponse.
        :type: MRecentSamples
        """
        if m_recent_raw_samples is None:
            raise ValueError("Invalid value for `m_recent_raw_samples`, must not be `None`")

        self._m_recent_raw_samples = m_recent_raw_samples

    @property
    def m_recent_times(self):
        """Gets the m_recent_times of this GetSummaryResponse.


        :return: The m_recent_times of this GetSummaryResponse.
        :rtype: MRecentTimes
        """
        return self._m_recent_times

    @m_recent_times.setter
    def m_recent_times(self, m_recent_times):
        """Sets the m_recent_times of this GetSummaryResponse.


        :param m_recent_times: The m_recent_times of this GetSummaryResponse.
        :type: MRecentTimes
        """
        if m_recent_times is None:
            raise ValueError("Invalid value for `m_recent_times`, must not be `None`")

        self._m_recent_times = m_recent_times

    @property
    def m_recent_sis(self):
        """Gets the m_recent_sis of this GetSummaryResponse.


        :return: The m_recent_sis of this GetSummaryResponse.
        :rtype: MRecentAnalytics
        """
        return self._m_recent_sis

    @m_recent_sis.setter
    def m_recent_sis(self, m_recent_sis):
        """Sets the m_recent_sis of this GetSummaryResponse.


        :param m_recent_sis: The m_recent_sis of this GetSummaryResponse.
        :type: MRecentAnalytics
        """
        if m_recent_sis is None:
            raise ValueError("Invalid value for `m_recent_sis`, must not be `None`")

        self._m_recent_sis = m_recent_sis

    @property
    def m_recent_ris(self):
        """Gets the m_recent_ris of this GetSummaryResponse.


        :return: The m_recent_ris of this GetSummaryResponse.
        :rtype: MRecentAnalytics
        """
        return self._m_recent_ris

    @m_recent_ris.setter
    def m_recent_ris(self, m_recent_ris):
        """Sets the m_recent_ris of this GetSummaryResponse.


        :param m_recent_ris: The m_recent_ris of this GetSummaryResponse.
        :type: MRecentAnalytics
        """
        if m_recent_ris is None:
            raise ValueError("Invalid value for `m_recent_ris`, must not be `None`")

        self._m_recent_ris = m_recent_ris

    @property
    def m_recent_ads(self):
        """Gets the m_recent_ads of this GetSummaryResponse.


        :return: The m_recent_ads of this GetSummaryResponse.
        :rtype: MRecentAnalytics
        """
        return self._m_recent_ads

    @m_recent_ads.setter
    def m_recent_ads(self, m_recent_ads):
        """Sets the m_recent_ads of this GetSummaryResponse.


        :param m_recent_ads: The m_recent_ads of this GetSummaryResponse.
        :type: MRecentAnalytics
        """
        if m_recent_ads is None:
            raise ValueError("Invalid value for `m_recent_ads`, must not be `None`")

        self._m_recent_ads = m_recent_ads

    @property
    def m_recent_ahs(self):
        """Gets the m_recent_ahs of this GetSummaryResponse.


        :return: The m_recent_ahs of this GetSummaryResponse.
        :rtype: MRecentAnalytics
        """
        return self._m_recent_ahs

    @m_recent_ahs.setter
    def m_recent_ahs(self, m_recent_ahs):
        """Sets the m_recent_ahs of this GetSummaryResponse.


        :param m_recent_ahs: The m_recent_ahs of this GetSummaryResponse.
        :type: MRecentAnalytics
        """
        if m_recent_ahs is None:
            raise ValueError("Invalid value for `m_recent_ahs`, must not be `None`")

        self._m_recent_ahs = m_recent_ahs

    @property
    def m_recent_ids(self):
        """Gets the m_recent_ids of this GetSummaryResponse.


        :return: The m_recent_ids of this GetSummaryResponse.
        :rtype: MRecentIDs
        """
        return self._m_recent_ids

    @m_recent_ids.setter
    def m_recent_ids(self, m_recent_ids):
        """Sets the m_recent_ids of this GetSummaryResponse.


        :param m_recent_ids: The m_recent_ids of this GetSummaryResponse.
        :type: MRecentIDs
        """

        self._m_recent_ids = m_recent_ids

    @property
    def m_recent_ams(self):
        """Gets the m_recent_ams of this GetSummaryResponse.


        :return: The m_recent_ams of this GetSummaryResponse.
        :rtype: MRecentAMs
        """
        return self._m_recent_ams

    @m_recent_ams.setter
    def m_recent_ams(self, m_recent_ams):
        """Sets the m_recent_ams of this GetSummaryResponse.


        :param m_recent_ams: The m_recent_ams of this GetSummaryResponse.
        :type: MRecentAMs
        """

        self._m_recent_ams = m_recent_ams

    @property
    def m_recent_aws(self):
        """Gets the m_recent_aws of this GetSummaryResponse.


        :return: The m_recent_aws of this GetSummaryResponse.
        :rtype: MRecentAnalytics
        """
        return self._m_recent_aws

    @m_recent_aws.setter
    def m_recent_aws(self, m_recent_aws):
        """Sets the m_recent_aws of this GetSummaryResponse.


        :param m_recent_aws: The m_recent_aws of this GetSummaryResponse.
        :type: MRecentAnalytics
        """
        if m_recent_aws is None:
            raise ValueError("Invalid value for `m_recent_aws`, must not be `None`")

        self._m_recent_aws = m_recent_aws

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
        if issubclass(GetSummaryResponse, dict):
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
        if not isinstance(other, GetSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other