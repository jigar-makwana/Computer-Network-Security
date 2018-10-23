import unittest
from sclient import SimpleHttpClient


class TestTransform(unittest.TestCase):
  def test_transform_input_file_path_null(self):
    client = SimpleHttpClient("www.cnn.com")
    self.assertIsNotNone(sclient.get('index.html'))


  def test_transform_input_file_path_null(self):
    client = SimpleHttpClient("www.google.com")
    self.assertIsNotNone(sclient.get('index.html'))
