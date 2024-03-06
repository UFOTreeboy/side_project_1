from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Optional

class MyForm(FlaskForm):
    profession = SelectField('您的職業類別',choices=[('ff01','學生'),
        ('ff02','金融與服務業'),('ff03','製造與工業'),('ff04','資訊與科技業'),
        ('ff05','農林漁牧業'),('ff06','旅遊與娛樂業'),('ff07','醫療與保健業'),
        ('ff08','自由業'),('ff09','教育業'),('ff10','其他')])
    content = TextAreaField('內文', validators=[DataRequired()])
    submit = SubmitField('確認')