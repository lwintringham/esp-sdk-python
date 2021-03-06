# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):
    """ TeamsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.teams_api.TeamsApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Create a(n) Team
        """
        pass

    def test_destroy(self):
        """
        Test case for destroy

        Remove a(n) Team
        """
        pass

    def test_list(self):
        """
        Test case for list

        Get a list of Teams
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single Team
        """
        pass

    def test_update(self):
        """
        Test case for update

        Update a(n) Team
        """
        pass


if __name__ == '__main__':
    unittest.main()
