import configparser
import json
from typing import Optional, Any


class ConfigParser(configparser.ConfigParser):

    # 重写safe_get
    def safe_get(self,
                 section: str,
                 option: str,
                 default: Optional[str] = None,
                 allowed: Optional[tuple[str, ...]] = None,
                 ) -> Optional[str]:
        try:
            value = self.get(section, option)
            if allowed and value not in allowed:
                return default
            return value
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    # 重写safe_getfloat
    def safe_getfloat(self,
                      section: str,
                      option: str,
                      default: Optional[str] = None,
                      allowed: Optional[tuple[float, ...]] = None,
                      ) -> Optional[float]:
        try:
            value = self.getfloat(section, option)
            if allowed and value not in allowed:
                return default
            return value
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    # 重写safe_getint
    def safe_getint(self,
                    section: str,
                    option: str,
                    default: Optional[str] = None,
                    allowed: Optional[tuple[int, ...]] = None,
                    ) -> Optional[int]:
        try:
            value = self.getint(section, option)
            if allowed and value not in allowed:
                return default
            return value
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def safe_getboolean(self,
                        section: str,
                        option: str,
                        default: Optional[bool] = None,
                        allowed: Optional[tuple[True, False]] = None,
                        ) -> Optional[bool]:
        try:
            value = self.getboolean(section, option)
            if allowed and value not in allowed:
                return default
            return value
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def safe_getlist(self,
                     section: str,
                     option: str,
                     default: Optional[list[Any]] = None,
                     allowed: Optional[tuple[str, ...]] = None,
                     ) -> list[Any]:
        try:
            raw_value = self.get(section, option)
            try:
                # 尝试将json解析为JSON列表
                value = json.loads(raw_value)
                if not isinstance(value, list):
                    raise ValueError("Paserd value is not a list")
            except (json.JSONDecodeError, ValueError):
                # 如果解析失败，尝试将其视为都好分割的字符串
                value = [item.strip() for item in raw_value.split(',')]
            if allowed and not all(item in allowed for item in value):
                return default
            return value
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default
