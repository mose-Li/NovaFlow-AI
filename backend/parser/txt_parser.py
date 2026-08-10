from pathlib import Path


class TxtParser:

    def parse(self, file_path: str) -> str:
        """
        解析 TXT 文件
        """

        path = Path(file_path)

        # UTF-8 优先
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            pass

        # GBK 兼容
        try:
            return path.read_text(encoding="gbk")
        except UnicodeDecodeError:
            pass

        # Latin-1 保底
        return path.read_text(encoding="latin1")