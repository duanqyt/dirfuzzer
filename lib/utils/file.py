import os
from typing import AnyStr, LiteralString, Union, List


class FileUtils:
    @staticmethod
    def build_path(*path_components: str) -> Union[LiteralString, str, bytes]:
        if path_components:
            path = os.path.join(*path_components)
        else:
            path = ""
        return path

    @staticmethod
    def get_abs_path(filename: str) -> str:
        return os.path.abspath(filename)

    @staticmethod
    def exists(filename: str) -> bool:
        return os.access(filename, os.F_OK)  # 路径是否存在

    @staticmethod
    def is_empty(filename: str) -> bool:
        return os.stat(filename).st_size == 0  # stat获取文件状态

    @staticmethod
    def can_read(filename: str) -> bool:
        try:
            with open(filename):
                pass
        except OSError:
            return False
        return True

    @classmethod
    def can_write(cls, path) -> bool:
        while not cls.exists(path):
            path = cls.parent(path)
        return os.access(path, os.W_OK)

    @staticmethod
    def read(filename: str) -> AnyStr:
        """
        读取文件到str
        :param filename: filename (绝对路径)
        :return: 文件内容字符串
        """
        return open(filename).read()

    @classmethod
    def get_files(cls, path) -> list:
        """
        遍历文件到列表
        :param path: 绝对路径字符串
        :return: 文件列表
        """
        files = []
        try:
            for root, dirs, filenames in os.walk(path):
                for filename in filenames:
                    file = os.path.join(root, filename)
                    files.append(file)
        except OSError as e:
            raise OSError
        finally:
            return files

    @staticmethod
    def get_lines(file_name: str) -> list[str]:
        with open(file_name, mode='r', errors='replace') as f:
            return f.read().splitlines()

    @staticmethod
    def is_dir(path: str) -> bool:
        return os.path.isdir(path)

    @staticmethod
    def is_file(path: str) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def parent(path, depth=1) -> str:
        for _ in range(depth):
            path = os.path.dirname(path)
        return path

    @classmethod
    def create_dir(cls, path: str) -> None:
        try:
            if not cls.exists(path):
                os.makedirs(path, exist_ok=True)
        except OSError as e:
            raise OSError

    @staticmethod
    def write_lines(file_name: str, lines: Union[List[str], str], overwrite: bool = False) -> None:
        """
        将字符串列表写入文件，可以选择覆盖现有内容或追加到文件末尾。

        参数:
            file_name (str): 要写入的文件路径。
            lines (Union[List[str], str]): 要写入的字符串列表或单个字符串。
            overwrite (bool, 可选): 如果为 True，则覆盖现有文件内容；否则追加到文件末尾。默认是 False。

        异常:
            FileNotFoundError: 如果文件路径无效。
            PermissionError: 如果没有权限写入文件。
            TypeError: 如果 `lines` 不是列表或字符串。
        """
        if isinstance(lines, str):
            lines = [lines]  # 将单个字符串转换为列表

        if not isinstance(lines, list):
            raise TypeError("lines must be a list of strings or a single string")
            # 日志记录
        try:
            mode = "w" if overwrite else "a"
            with open(file_name, mode, encoding='utf-8') as f:
                for line in lines:
                    f.write(line + os.linesep)
        except FileNotFoundError:
            raise FileNotFoundError  # 日志
        except PermissionError:
            raise PermissionError  # 日志
        except Exception as e:
            raise Exception  #日志


class File:
    def __init__(self, *path_components: str) -> None:
        self._path = FileUtils.build_path(*path_components)

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, path: str) -> None:
        raise NotImplementedError

    def is_valid(self):
        return FileUtils.exists(self.path)


