import sys
import os
import json
import types

import web
import unittest2 as unittest
from mock import patch
from webtest import TestApp

import blog
from blog import model


class indexTest(unittest.TestCase):

  def setUp(self):
    middleware = []
    self.app = TestApp(blog.app.wsgifunc(*middleware))


  @patch.object(model, "get_posts", autospec=True)
  def testGETIndex(self, get_posts_mock):
    response = self.app.get("/", status="*", expect_errors=True)
    headers = dict(response.headers)
    self.assertIn(headers["Content-Type"], "text/html; charset=utf-8")
    self.assertEqual(response.status, "200 OK")
    self.assertIsInstance(response.body, types.StringTypes)
    self.assertTrue(get_posts_mock.called)



class viewTest(unittest.TestCase):

  def setUp(self):
    middleware = []
    self.app = TestApp(blog.app.wsgifunc(*middleware))


  @patch.object(model, "get_post", autospec=True)
  def testGETIndex(self, get_post_mock):
    response = self.app.get("/view/1", status="*", expect_errors=True)
    headers = dict(response.headers)
    self.assertIn(headers["Content-Type"], "text/html; charset=utf-8")
    self.assertEqual(response.status, "200 OK")
    self.assertIsInstance(response.body, types.StringTypes)
    get_post_mock.assert_called_once_with(1)



class newTest(unittest.TestCase):


  def setUp(self):
    middleware = []
    self.app = TestApp(blog.app.wsgifunc(*middleware))


  def testGETNew(self):
    response = self.app.get("/new", status="*", expect_errors=True)
    form = response.form
    headers = dict(response.headers)
    self.assertIn(headers["Content-Type"], "text/html; charset=utf-8")
    self.assertEqual(response.status, "200 OK")
    self.assertIsInstance(response.body, types.StringTypes)
    self.assertEqual(form.fields.keys(), ["title", "content", "Post entry"])



  @patch.object(model, "new_post", autospec=True)
  def testPOSTNew(self, new_post_mock):
    responseGET = self.app.get("/new", status="*", expect_errors=True)
    form = responseGET.form
    form["title"] = "test title"
    form["content"] = "test description"
    responsePOST = form.submit('submit')
    self.assertTrue(new_post_mock.called)
    headers = dict(responsePOST.headers)
    self.assertIn(headers["Content-Type"], "text/html")
    self.assertEqual(responsePOST.status, "303 See Other")



class deleteTest(unittest.TestCase):


  def setUp(self):
    middleware = []
    self.app = TestApp(blog.app.wsgifunc(*middleware))


  def testDELETE(self):
    #TODO
    pass
if __name__ == "__main__":
  unittest.main()

