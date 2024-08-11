# QtPy5 is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import openai
from openai import OpenAI
import io
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt

app = QApplication(sys.argv)

# ����� ����� �����
window = QWidget()
window.setWindowTitle("Your private assistant")
window.setGeometry(100, 100, 800, 900)

# ����� ����
banner_label = QLabel()
banner_pixmap = QPixmap("Data/banner_img.png")
banner_label.setPixmap(banner_pixmap.scaled(window.width(), 200, Qt.KeepAspectRatioByExpanding))  # ����� ���� ������ ����� 20 �������
banner_label.setFixedHeight(200)  # ����� ���� ���� �����

# ����� ��� ����'�
tabs = QTabWidget()

# ����� ���� ������ � chat
tab1 = QWidget()


# ����� ���� ���� ����� ���� ��-�����
text_input = QTextEdit(window)
text_input.setPlaceholderText("Write a question related to computers here")
text_input.setStyleSheet("background-color: #f0f0f0;")  # ��� ��� ����

# ����� ����� �� ����� "Start Chat!"
buttonChat = QPushButton("Start Chat!", window)

# ����� ���� ���� ����� ������
output_text = QTextEdit(window)
output_text.setReadOnly(True)  # ����� ���� ����� ������ ����
output_text.setPlaceholderText("The answer will apear here...")
output_text.setStyleSheet("background-color: #e0f7fa;")  # ��� ��� ���


# ����� ����� ����� ���� ������
layout_chat = QVBoxLayout()
layout_chat.addWidget(text_input)
layout_chat.addWidget(buttonChat)
layout_chat.addWidget(output_text)

tab1.setLayout(layout_chat)

# ����� �������� ����� ����� ������
def on_button_chat_clicked():
    prompt = text_input.toPlainText()  # ���� ���� �������
    output_text.setPlainText(createText(prompt))  # ���� ���� ������

buttonChat.clicked.connect(on_button_chat_clicked)

client = OpenAI()

def createText(prompt):
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are an expert in computers and can only answer questions related to computers. If asked about another topic, you will respond that you are unable to answer and would be happy to answer questions related to computers."},
        {"role": "user", "content": prompt}
      ]
    )
    return completion.choices[0].message.content



# ����� ���� ����   "Create Image"
tab2 = QWidget()


# ����� ���� ���� ����� ���� ��-�����
img_input = QTextEdit(window)
img_input.setPlaceholderText("Write a description of the image you want GPT to generate for you. You can also specify style and colors as you wish...")
img_input.setStyleSheet("background-color: #e7d2fa;")  # ��� ��� ����



# ����� ����� �� ����� "Generate Image!"
button_img = QPushButton("Generate Image!", window)

# ����� ����� ����� ���� ����
layoutImg = QVBoxLayout()
layoutImg.addWidget(img_input)
layoutImg.addWidget(button_img)

tab2.setLayout(layoutImg)



def createImage(img_prompt):
    prefixPrompt = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: "
    response = client.images.generate(
      model="dall-e-3",
      prompt=img_prompt,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    return response.data[0].url


def on_button_img_clicked():
    img_prompt= img_input.toPlainText() # ���� ���� �������
    urlImage = createImage(img_prompt)
    urllib.request.urlretrieve(urlImage, "TempImageName.png") 
    img = Image.open("TempImageName.png") 
    img.show()

button_img.clicked.connect(on_button_img_clicked)



# ����� ������ ������'� ������
tabs.addTab(tab1, "Chat about computers")
tabs.addTab(tab2, "Create Image")


# ����� ����� ����� ����� ������ ����'� ������ ������
main_layout = QVBoxLayout()
main_layout.addWidget(tabs)
window.setLayout(main_layout)



# ����� ����� ������� ������ ������
main_layout.addWidget(banner_label)
main_layout.addWidget(tabs)
window.setLayout(main_layout)

window.show()

sys.exit(app.exec_())
