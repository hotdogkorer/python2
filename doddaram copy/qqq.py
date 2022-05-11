from googletrans import Translator
translator = Translator(service_urls=[
'translate.google.com',
'translate.google.co.kr',
])
tr_results = translator.translate('안녕하세요.', src='ko', dest='ja')
print ('Trans(JA):', tr_results.text, tr_results.pronunciation)
