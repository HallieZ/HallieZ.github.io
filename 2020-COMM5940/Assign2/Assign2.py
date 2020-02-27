#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template
import requests
    
app = Flask(__name__)

@app.route("/")
def home():
    user = {"name":"小说作品影视化"}
    headers = {'Authorization': 'Bearer keyoJSNH4UrvVdyMK',}
    params = (('view', 'Grid view'),)

    r = requests.get('https://api.airtable.com/v0/appRx9bziWSLTJcoZ/%E4%B9%A6%E6%9C%AC%E5%BD%B1%E8%A7%86%E5%8C%96?api_key=keyoJSNH4UrvVdyMK', headers=headers, params=params)
    dict = r.json()
    dataset = []
    for i in dict["records"]:
        dict = i['fields']
        dataset.append(dict)
    return render_template('assign2.html',album_user=user, dataset=dataset)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9010, app)
# if __name__ == '__main__':
   # app.run(debug = True)


# In[ ]:




