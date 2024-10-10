import requests
import os
from flask import Flask, render_template, redirect, request
from replit import web

app = Flask(__name__)

users = web.UserStore()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  url = 'https://discord.com/' + path
  # url = url.replace('//', '/')
  site = url.split('://')[0] + url.split('://')[1].split('/')[0]

  page = requests.get(url)

  text = page.text
  text = text.replace('href="/', f'href="{url}/')
  text = text.replace('src="/', f'src="{url}/')
  text = text.replace('/app/assets/', '/assets/')

  text = text.replace('</head>', '<base href="' + site + '" /></head>' )

  return text

web.run(app)