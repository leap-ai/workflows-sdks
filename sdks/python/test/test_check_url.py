# coding: utf-8

"""
    Leap Workflows API

    The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

    The version of the OpenAPI document: 1.0
    Contact: help@tryleap.ai
    Created by: https://tryleap.ai/
"""

import unittest
from leap_workflows.configuration import check_url
from leap_workflows.exceptions import InvalidHostConfigurationError


class TestIsValidUrl(unittest.TestCase):
    def test_valid_urls(self):
        valid_urls = [
            "http://www.example.com",
            "https://www.example.com",
            "http://example.com",
            "https://example.com/path/to/resource",
            "http://example.com:8080",
            "https://example.co.uk",
            "https://subdomain.example.com",
            "https://api.example.com/v1/resource",
            "https://example.com/path/to/resource/123",
            "https://www.example.com:8080",
            "https://www.example.com:8080/path/to/resource",
            "http://sub.example.com:8080",
            "http://deep.sub.domain.example.com",
            "http://127.0.0.1:4010",
            "https://deep.sub.domain.example.com:8080/path",
            "http://example.io",
            "https://example.app",
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(check_url(url))

    def test_invalid_urls(self):
        invalid_urls = [
            "not_a_url",
            "http:/example.com",
            "http://",
            "http://.com",
            "example.com",
            "http://example.com#fragment",
            "www.example.com",
            "https://example.com/path/to/resource?query=value",
            "https://example.com/path/to/resource?query=value&key2=value2",
            "https://",
            "ftp://files.example.com",
            "//example.com",
            "https://example,com",
            "https:/example.com",
            "https:// example.com",
            "https://example.com path",
            "http://..com",
            "https://..example.com",
            "http://example..com",
            "https://example.com./path",
            "https://example.com..",
            "http://:8080",
            "https://example.com:",
            "http://example.com:abc",
            "https://.example.com",
            "http://example.",
            "https:// example:8080.com",
            "http:// example.com:8080/path",
            "https://:8080/path",
        ]
        for url in invalid_urls:
            with self.subTest(url=url):
                with self.assertRaises(InvalidHostConfigurationError):
                    check_url(url)
                    raise Exception("URL should be invalid: " + url)


if __name__ == "__main__":
    unittest.main()
