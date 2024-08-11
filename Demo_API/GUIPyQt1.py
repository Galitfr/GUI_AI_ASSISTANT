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

# יצירת החלון הראשי
window = QWidget()
window.setWindowTitle("Your private assistant")
window.setGeometry(100, 100, 800, 900)

# יצירת באנר
banner_label = QLabel()
banner_pixmap = QPixmap("Data/banner_img.png")
banner_label.setPixmap(banner_pixmap.scaled(window.width(), 200, Qt.KeepAspectRatioByExpanding))  # שינוי גודל התמונה לגובה 20 פיקסלים
banner_label.setFixedHeight(200)  # הגדרת גובה קבוע לבאנר

# יצירת טאב וידג'ט
tabs = QTabWidget()

# יצירת הטאב הראשון ל chat
tab1 = QWidget()


# יצירת תיבת טקסט להזנת טקסט רב-שורות
text_input = QTextEdit(window)
text_input.setPlaceholderText("Write a question related to computers here")
text_input.setStyleSheet("background-color: #f0f0f0;")  # צבע רקע בהיר

# יצירת כפתור עם תווית "Start Chat!"
buttonChat = QPushButton("Start Chat!", window)

# יצירת תיבת טקסט להצגת התשובה
output_text = QTextEdit(window)
output_text.setReadOnly(True)  # הפיכת תיבת הטקסט לקריאה בלבד
output_text.setPlaceholderText("The answer will apear here...")
output_text.setStyleSheet("background-color: #e0f7fa;")  # צבע רקע אחר


# הגדרת פריסה אנכית לטאב הראשון
layout_chat = QVBoxLayout()
layout_chat.addWidget(text_input)
layout_chat.addWidget(buttonChat)
layout_chat.addWidget(output_text)

tab1.setLayout(layout_chat)

# קישור הפונקציה להצגת הטקסט לכפתור
def on_button_chat_clicked():
    prompt = text_input.toPlainText()  # קבלת הקלט מהמשתמש
    output_text.setPlainText(createText(prompt))  # הצגת הקלט בתווית

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



# יצירת הטאב השני   "Create Image"
tab2 = QWidget()


# יצירת תיבת טקסט להזנת טקסט רב-שורות
img_input = QTextEdit(window)
img_input.setPlaceholderText("Write a description of the image you want GPT to generate for you. You can also specify style and colors as you wish...")
img_input.setStyleSheet("background-color: #e7d2fa;")  # צבע רקע בהיר



# יצירת כפתור עם תווית "Generate Image!"
button_img = QPushButton("Generate Image!", window)

# הגדרת פריסה אנכית לטאב השני
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
    img_prompt= img_input.toPlainText() # קבלת הקלט מהמשתמש
    urlImage = createImage(img_prompt)
    urllib.request.urlretrieve(urlImage, "TempImageName.png") 
    img = Image.open("TempImageName.png") 
    img.show()

button_img.clicked.connect(on_button_img_clicked)



# הוספת הטאבים לווידג'ט הטאבים
tabs.addTab(tab1, "Chat about computers")
tabs.addTab(tab2, "Create Image")


# הגדרת פריסה כוללת לחלון והוספת וידג'ט הטאבים והלוגו
main_layout = QVBoxLayout()
main_layout.addWidget(tabs)
window.setLayout(main_layout)



# הוספת הבאנר והטאבים לפריסה הראשית
main_layout.addWidget(banner_label)
main_layout.addWidget(tabs)
window.setLayout(main_layout)

window.show()

sys.exit(app.exec_())
