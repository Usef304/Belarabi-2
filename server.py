from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# المسار للصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')  # تأكد من أن ملف index.html موجود في مجلد templates

# مسار تحليل الكلمة
@app.route('/classify', methods=['get','POST'])
def classify():
    data = request.get_json()
    word = data.get('word', '').strip()

    verbs = [
    "كتب", "قرأ", "ذهب", "عاد", "أكل", "شرب", "لعب", "نام", "جلس", "وقف", "ياكل",
    "يكتب", "يقرأ", "يذهب", "يعود", "يأكل", "يشرب", "يلعب", "ينام", "يجلس", "يقف",
    "اكتب", "اقرأ", "اذهب", "عد", "كل", "اشرب", "العب", "نم", "اجلس", "قف",
    "سافر", "استمع", "شاهد", "تفحص", "رسم", "نسخ", "خطّ", "سار", "مشى", "ركض"
]
    nouns =  [
    "محمد", "علي", "فاطمة", "خالد", "سارة", "أحمد", "مريم", "يوسف", "هند", "عمر", "يارا",  "روضه",
    "ليلى", "زينب", "عبدالله", "نورة", "إبراهيم", "أمينة", "سعيد", "جميلة", "حسن", "منى", "تفاحة",
    "كتاب", "قلم", "سيارة", "منزل", "شجرة", "كرسي", "طاولة", "نافذة", "باب", "حديقة", "ملك", "ابوالعلا",
    "مكتب", "حاسوب", "هاتف", "مصباح", "ساعة", "سرير", "دراجة", "طائرة", "قطار", "سفينة",
    "مكتبة", "ثلاجة", "فرن", "مغسلة", "مرآة", "خزانة", "مروحة", "تلفاز", "راديو", "كاميرا"
]
    particles = [
    "من", "إلى", "عن", "على", "في", "الباء", "اللام", "الكاف", "واو القسم", "تاء القسم",
    "رُبّ", "مذ", "منذ", "حتى", "خلا", "عدا", "حاشا", "كي", "لعل", "متى"
]
    # ضمائر المتكلم
    first_person_pronouns = ["أنا", "نحن","انا"]

    # ضمائر المخاطب
    second_person_pronouns = ["انت", "أنت", "أنتما", "أنتم", "أنتن"]

    # ضمائر الغائب
    third_person_pronouns = ["هو", "هي", "هما", "هم", "هن"]

    # ضمائر النصب المنفصلة
    accusative_independent_pronouns = ["إياي", "إيانا", "إياكَ", "إياكِ", "إياكما", "إياكم", "إياكن", "إياه", "إياها", "إياهما", "إياهم", "إياهن"]

    # ضمائر الرفع المتصلة
    nominative_attached_pronouns = ["تاء المتحركة", "نا الفاعلين", "نون النسوة", "ألف الاثنين", "واو الجماعة", "ياء المخاطبة"]

    # ضمائر النصب المتصلة
    accusative_attached_pronouns = ["هاء الغيبة", "كاف الخطاب", "ياء المتكلم", "نا المتكلمين"]

    # ضمائر الجر المتصلة
    genitive_attached_pronouns = ["عنه", "لها", "إلينا", "عليك", "فيها", "منها"]


    if word in verbs:
        result = f'الكلمة "{word}" هي فعل.'
    elif word in nouns:
        result = f'الكلمة "{word}" هي اسم.'
    elif word in particles:
        result = f'الكلمة "{word}" هي حرف.'
    elif word in first_person_pronouns:
        result = f'الكلمة "{word}" هي  ضمائر المتكلم.'
    elif word in second_person_pronouns:
        result = f'الكلمة "{word}" هي ضمائر المخاطب.'
    elif word in third_person_pronouns:
        result = f'الكلمة "{word}" هي ضمائر الغائب.'
    elif word in accusative_independent_pronouns:
        result = f'الكلمة "{word}" هي ضمائر النصب المنفصلة.'
    else:
        result = f'الكلمة "{word}" غير معروفة في قاعدة البيانات.'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
