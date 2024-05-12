text = ["man" ,2 ,2 ,4, 5, " alfa " , "bet"]
text = list(filter(lambda x: isinstance(x,str), text))
print(text)