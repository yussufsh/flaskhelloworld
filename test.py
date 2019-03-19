#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        name = 'User'
        rv = self.app.get('/hello/{0}'.format(name))
        self.assertEqual(rv.status, '200 OK')
        print(rv.data)
        self.assertIn(bytearray("{0}".format(name), 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()
