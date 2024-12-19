import unittest

from lib.utils.file import FileUtils

fu = FileUtils()


class TestFileUtils(unittest.TestCase):

    def test_build_path(self):
        self.assertEqual(fu.build_path('/', 'home', 'dphonor'), '/home/dphonor')

    def test_get_abs_path(self):
        self.assertEqual(fu.get_abs_path('test_file.py'), '/Users/dphonor/Documents/dirfuzzer/test/lib/utils'
                                                          '/test_file.py')

    def test_exists(self):
        self.assertEqual(fu.exists('test_file.py'), True)
        self.assertEqual(fu.exists('dphonor.py'), False)

    def test_is_empty(self):
        self.assertEqual(fu.is_empty('test_file.py'), False)
        self.assertEqual(fu.is_empty('__init__.py'), True)

    def test_can_write(self):
        # self.assertEqual()
        pass

    def test_can_read(self):
        self.assertEqual(fu.can_read('test_file.py'), True)
        self.assertEqual(fu.can_read('test_file1.py'), False)

    def test_read(self):
        self.assertEqual(fu.read('/Users/dphonor/Documents/dirfuzzer/test/other/test/test.txt'), '仅供测试')

    def test_get(self):
        self.assertEqual(fu.get_files('/Users/dphonor/Documents/dirfuzzer/test/other'),
                         ['/Users/dphonor/Documents/dirfuzzer/test/other/__init__.py',
                          '/Users/dphonor/Documents/dirfuzzer/test/other/test/test.txt',
                          '/Users/dphonor/Documents/dirfuzzer/test/other/test/demo.py',
                          '/Users/dphonor/Documents/dirfuzzer/test/other/test/__pycache__/demo.cpython-312.pyc'
                          ])
