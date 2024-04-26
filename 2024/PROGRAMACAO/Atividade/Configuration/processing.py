
import re

def processing(text, *args, **kwargs):
    while True:
        if '.' in text:
            try:
                text = re.sub(r' mil inscritos', '00', text)
                text = re.sub(r'K subscribers', '00', text)
                text = re.sub(r' mi de inscritos', '00000', text)
                text = re.sub(r'M subscribers', '00000', text)
                text = re.sub(r' mil visualizações', '00', text)
                text = re.sub(r'K views', '00', text)
                text = re.sub(r' mi de visualizações', '00000', text)
                text = re.sub(r'M views', '00000', text)
                text = re.sub(r' mil vídeos', '00', text)
                text = re.sub(r'K videos', '00', text)
                text = re.sub(r' mi de vídeos', '00000', text)
                text = re.sub(r'M videos', '00000', text)
                text = re.sub('/[.,\/#!$%\^&\*;:{}=\-_`~()]/g',"", text)
                text = re.sub('/\s{2,}/g', "", text)
                text =  int(''.join(filter(str.isdigit, text)))
                #text = re.sub('[^A-Za-z0-9]+', ' ', text)
            except:
                text = 0
            return text
        else:
            try:
                text = re.sub(r' mil inscritos', '000', text)
                text = re.sub(r'K subscribers', '000', text)
                text = re.sub(r' mi de inscritos', '000000', text)
                text = re.sub(r'M subscribers', '000000', text)
                text = re.sub(r'Um inscrito', '1', text)
                text = re.sub(r'One subscriber', '1', text)
                text = re.sub(r' inscritos', '', text)
                text = re.sub(r' subscribers', '', text)
                text = re.sub(r' inscrito', '', text)
                text = re.sub(r' subscriber', '', text)
                text = re.sub(r' mil visualizações', '000', text)
                text = re.sub(r'K views', '000', text)
                text = re.sub(r' mi de visualizações', '000000', text)
                text = re.sub(r'M views', '000000', text)
                text = re.sub(r'Uma visualização', '', text)
                text = re.sub(r'One view', '', text)
                text = re.sub(r' visualizações', '', text)
                text = re.sub(r' views', '', text)
                text = re.sub(r' visualização', '', text)
                text = re.sub(r' view', '', text)
                text = re.sub(r' mil vídeos', '000', text)
                text = re.sub(r'K videos', '000', text)
                text = re.sub(r' mi de vídeos', '000000', text)
                text = re.sub(r'M videos', '000000', text)
                text = re.sub(r'Um vídeo', '1', text)
                text = re.sub(r'One video', '1', text)
                text = re.sub(r' vídeos', '', text)
                text = re.sub(r' videos', '', text)
                text = re.sub(r' vídeo', '', text)
                text = re.sub(r' video', '', text)
                text = re.sub('/[.,\/#!$%\^&\*;:{}=\-_`~()]/g',"", text)
                text = re.sub('/\s{2,}/g', "", text)
                text =  int(''.join(filter(str.isdigit, text)))
                #text = re.sub('[^A-Za-z0-9]+', ' ', text)
            except:
                text = 0
            return text

def processing2(text, *args, **kwargs):
    while True:
        text = re.sub('\\n', ' ', text)
        text = re.sub("/[.,\/#!$%\^&\*;:{}=\-_`~()]/g","", text)
        text = re.sub('/\s{2,}/g', "", text)
        text = re.sub('//', '', text)
        #text = re.sub('[^A-Za-z0-9]+', ' ', text)
        return text
