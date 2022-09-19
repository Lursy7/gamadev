from flask import Flask, render_template
from random import randint

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html', randint=randint)

@app.route('/bots')
def bots():
    bots = {'GAMABOT (RPG)': 'https://cdn.discordapp.com/avatars/894263121521311835/762f20e8e8aeb461ad047d828b147973.webp?size=80', 'GAMABOT': 'https://cdn.discordapp.com/avatars/894263121521311835/762f20e8e8aeb461ad047d828b147973.webp?size=80', 'GAMABOT2': 'https://cdn.discordapp.com/avatars/894263121521311835/762f20e8e8aeb461ad047d828b147973.webp?size=80', 'GAMABOT3': 'https://cdn.discordapp.com/avatars/894263121521311835/762f20e8e8aeb461ad047d828b147973.webp?size=80'}
    return render_template('bots.html', bots = bots, randint=randint)

if __name__ == '__main__':
    app.run(debug=True)
