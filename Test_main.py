import unittest
from main import My_cite

class TestStringMethods(unittest.TestCase):

  def setUp(self):#объявление класса, методы которого мы хотим проверить
      self.my_cite=My_cite()

  def test_start(self):#тест на открытие правильной интернет-страницы
      self.assertEqual(self.my_cite.start(),"render_template('home.html')")

  def test_about(self):#тест на открытие правильной интернет-страницы
      self.assertEqual(self.my_cite.about(),"render_template('add_file.html')")

  def test_form(self):#тест на открытие и подсчёт слов в файле
      extension = 'test_test.txt'
      self.assertEqual(self.my_cite.form(extension), "render_template('add_file.html',result='В файле '"+extension+"' самое популярное слово 'replay' встречается '4' раз')")

  def test_form_rus(self): #тест на файл с кириллицей
      extension='test_1.txt'
      self.assertEqual(self.my_cite.form(extension),"render_template('add_file.html',result='В файле '"+extension+"' самое популярное слово 'я' встречается '9' раз')")

  def test_form_on_wrong_extension(self):#тест на неверное расширение файла
      extension = 'test_1.py'
      self.assertEqual(self.my_cite.form(extension),"render_template('add_file.html',result='Файл неподдерживаемого формата. Требуется:.txt Получено: '" + extension + ")")

  def test_form_on_wrong_filename(self):#тест на неверное имя файла (файл не найден)
      extension = 'testtt.txt'
      self.assertEqual(self.my_cite.form(extension), "File '" + extension + "' not found")
if __name__ == '__main__':
    unittest.main()