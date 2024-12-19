import unittest

from lib.parse.config import ConfigParser

config_data = """
[test]
name = dphonor
integer = 1
float = 6.66
boolean = True
list = ["dp", "jiang"]
list2 = test
[test2]
name = duan
float = 8.88
boolean = False
[test3]
# JSON 格式的用户角色列表
user-roles = ["admin", "user", "guest"]

# 逗号分隔的字符串形式的用户角色列表
user-roles-string = admin,user,guest

# 包含不允许值的用户角色列表
invalid-roles = ["admin", "superuser"]

# 空的用户角色列表
empty-roles = []

# 不存在的选项
nonexistent =

"""

config = ConfigParser()
config.read_string(config_data)


class TestConfig(unittest.TestCase):
    def test_safe_get(self):
        self.assertEqual(config.safe_get('test', 'name'), 'dphonor')
        self.assertEqual(config.safe_get('test2', 'name'), 'duan')

    def test_safe_getfloat(self):
        self.assertEqual(config.safe_getfloat('test', 'float'), 6.66)
        self.assertEqual(config.safe_getfloat('test2', 'float'), 8.88)

    def test_safe_getint(self):
        self.assertEqual(config.safe_getint('test', 'integer'), 1)
        self.assertEqual(config.safe_getint('test', 'no-integer', default=2), 2)
        self.assertEqual(config.safe_getint('test', 'integer', allowed=(1, 2, 3, 4)), 1)

    def test_safe_getboolean(self):
        self.assertEqual(config.safe_getboolean('test', 'boolean'), True)
        self.assertEqual(config.safe_getboolean('test2', 'boolean'), False)
        self.assertEqual(config.safe_getboolean('test2', 'boolean', allowed=(True, False)), False)

    def test_safe_getlist(self):
        self.assertEqual(config.safe_getlist('test3', 'user-roles'), ["admin", "user", "guest"])
        self.assertEqual(config.safe_getlist('test3', 'user-roles-string'), ["admin", "user", "guest"])
