from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import test_beautifulsoup1 as bs

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和图标
        self.setWindowTitle('抱枕R18 By 黑咖啡和冰月亮')
        self.setWindowIcon(QIcon('myHead.jpg'))  # 替换为实际的图标文件
        self.setGeometry(100,100,800,600)
        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建并设置标题
        title_label = QLabel('抱枕R18')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Comic Sans MS', 24, QFont.Bold))
        title_label.setStyleSheet("color: #FF69B4;")  # 粉色
        main_layout.addWidget(title_label)

        # 创建搜索框和按钮的水平布局
        search_layout = QHBoxLayout()

        # 创建搜索框
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('输入角色名...')
        self.search_input.setFont(QFont('Arial', 12))
        self.search_input.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border: 2px solid #FF69B4;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #FF1493;
            }
        """)
        search_layout.addWidget(self.search_input)

        # 创建搜索按钮
        search_button = QPushButton('搜索')
        search_button.setFont(QFont('Arial', 12))
        search_button.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                background-color: #FF69B4;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FF1493;
            }
        """)
        search_layout.addWidget(search_button)

        # 将搜索布局添加到主布局
        main_layout.addLayout(search_layout)
        # 创建并设置结果显示区域
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setFont(QFont('Arial', 12))
        self.result_text.setStyleSheet("""
                   QTextEdit {
                       padding: 5px;
                       border: 2px solid #FF69B4;
                       border-radius: 5px;
                       background-color: #FFF;
                   }
               """)
        main_layout.addWidget(self.result_text)
        # 设置主布局
        self.setLayout(main_layout)

        # 连接搜索按钮的点击事件
        search_button.clicked.connect(self.on_search)

        # 连接回车键事件
        self.search_input.returnPressed.connect(self.on_search)

    def on_search(self):
        query = self.search_input.text()
        if query:
            bs.view_preview_image(bs.find_photo(query))
            results = bs.website_url
            self.result_text.clear()
            self.result_text.append("为你找到以下网站:")
            for result in results:
                self.result_text.append(result)
        else:
            print("请输入搜索关键词")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())
