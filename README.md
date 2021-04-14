# django_tailwind

ขั้นตอนการติดตั้ง Django project ร่วมกับ Tailwind CSS
----
Step 1: สร้าง enviroment
--
python -m venv env

Step 2: Activate env
--
env\Scripts\activate

Step 3: ติดตั้ง Django
--
pip install django

ดูรายละเอียดของ package ที่ติดตั้งไว้ใน project
--
pip list

Step 4: สร้างโปรเจ็กต์
--
django-admin startproject myblog

Step 5: ทดสอบรันโปรเจ็กต์
---
python manage.py runserver

Step 6: สร้างแอพ
---
python manage.py startapp blog

Step 7: การติดตั้ง Tailwind CSS
---
cd jstools

npm init -y && npm install tailwindcss autoprefixer clean-css-cli && npx tailwindcss init -p

Step 8: config การ build ไฟล์ tailwind ที่ package.json
---
"build": "tailwind build ../static/css/tailwind.css -o ../static/css/style.css && cleancss -o ../static/css/style.min.css ../static/css/style.css"

Step 9: สร้างไฟล์ tailwind.css ไว้ใน static/css/tailwind.css
---
@tailwind base;
@tailwind components;
@tailwind utilities;


Step 10: config  ไฟล์ tailwind.config.js
---
module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: false, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
}

Step 11: build tailwind css
---
npm run build

Step 12: config path ในไฟล์ settings.py
----
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

บริษัท ไอทีจีเนียส เอ็นจิเนียริ่ง จำกัด
บริการอบรมพัฒนาเว็บไซต์ และรับทำเว็บไซต์ งานกราฟฟิก
