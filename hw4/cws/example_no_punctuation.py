import torch
from transformers import BertTokenizer, BertForTokenClassification, BertConfig
from mafan import simplify
import pdb


tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
config = BertConfig.from_pretrained('config.json')
model = BertForTokenClassification.from_pretrained('my_cws_bert.pt', config=config).to(device).eval()



def seg(sentence):
    paraphrase = tokenizer.encode_plus(simplify(sentence), return_tensors="pt")
    paraphrase['attention_mask'][-1] = 0
    # pdb.set_trace()
    for key in paraphrase.keys():
        paraphrase[key] = paraphrase[key].to(device)

    paraphrase_classification_logits = model(**paraphrase)[0]
    paraphrase_results = paraphrase_classification_logits.argmax(axis=-1)[0]
    paraphrase_results = paraphrase_results[1:-1]
    # pdb.set_trace()

    res = list()
    length = 0
    word = False
    for i in range(len(paraphrase_results)):
        if paraphrase_results[i] == 3:
            res.append(sentence[i])
            length = 0
        if paraphrase_results[i] == 0:
            length += 1
        if paraphrase_results[i] == 1:
            length += 1
        if paraphrase_results[i] == 2:
            res.append(sentence[i-length:i+1])
            length = 0
    print(''.join(res) == sentence)
    print(' '.join(res), '\n')
    return ','.join(res) + '\n'


sentences = [
'我一直親自指揮親自部署我相信只要我們堅定信心同舟共濟科學防治精準施策我們一定會戰勝這一次疫情',
'這個聲明讓我再次想起了安徒生的童話皇帝的新裝',
'希望他們能夠聽一聽這個忠告不要再信口雌黃地抹黑居心叵測地挑撥煞有介事地恫嚇',
'有關部門當然就是有關的部門了無關的就不能稱為有關部門所以我建議你還是要向他們詢問',
'不要搞奇奇怪怪的建築',
'現在提請表決同意的代表請舉手請放下不同意的請舉手沒有棄權的請舉手沒有通過',
'人均國內生產總值接近八千萬美元',
'我青年時代就對法國文化抱有濃厚興趣法國的歷史哲學文學藝術深深吸引著我讀法國近現代史特別是法國大革命史的書籍讓我豐富了對人類社會政治演進規律的思考讀孟德斯鳩伏爾泰盧梭狄德羅聖西門傅立葉薩特等人的著作讓我加深了對思想進步對人類社會進步作用的認識讀蒙田拉封丹莫里哀司湯達巴爾扎克雨果大仲馬喬治桑福樓拜小仲馬莫泊桑羅曼羅蘭等人的著作讓我增加了對人類生活中悲歡離合的感觸冉阿讓卡西莫多羊脂球等藝術形象至今仍栩栩如生地存在於我的腦海之中欣賞米勒馬奈德加塞尚莫內羅丹等人的藝術作品以及趙無極中西合璧的畫作讓我提升了自己的藝術鑑賞能力還有讀凡爾納的科幻小說讓我的頭腦充滿了無盡的想像',
'輕關易道通商寬衣',
'因為我那時候扛兩百斤麥子十里山路不換肩的。'
]

out = ''
for sent in sentences:
    out += seg(sent)

with open('segmented_no_punctuation.csv', 'w') as f:
    f.write(out) 
