from gmail import GMail, Message
from datetime import datetime
now = datetime.now()
hour_now = now.hour

if hour_now >= 7:
    html_content = '''
    <p>Hi Sếp,</p>
    <p>H&ocirc;m nay em ch&aacute;n l&agrave;m n&ecirc;n xin nghỉ&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" />.</p>
    <p>Vậy hoy.</p>
    <p>&nbsp;</p>'''
    gmail = GMail('baoanan90s@gmail.com', 'baoanan90s90s')
    msg = Message('Đơn xin nghỉ phép!', to='c4e.201708@gmail.com', html = html_content)
    gmail.send(msg)
