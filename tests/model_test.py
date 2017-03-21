import web
from blog import model
import unittest2 as unittest
from mock import patch, Mock, MagicMock


class ModelTest(unittest.TestCase):

  @patch.object(model,'get_db')
  def test_get_posts(self, get_db_mock):
    mock_db = get_db_mock()
    result = model.get_posts()
    self.assertTrue(mock_db.select.called)

  @patch.object(model,'get_db')
  def test_get_post(self, get_db_mock):
    mock_db = get_db_mock()
    id = 1
    result = model.get_post(id)
    self.assertTrue(mock_db.select.called)

  @patch.object(model,'get_db')
  def test_new_post(self, get_db_mock):
    mock_db = get_db_mock()
    title = "foo_title"
    text = "foo_text"
    result = model.new_post(title=title, text = text)
    self.assertTrue(mock_db.insert.called)

  @patch.object(model,'get_db')
  def test_del_post(self, get_db_mock):
    mock_db = get_db_mock()
    id = 1
    result = model.del_post(id=id)
    self.assertTrue(mock_db.delete.called)

if __name__ == "__main__":
  unittest.main()

