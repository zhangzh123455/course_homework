# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
from sqlalchemy.sql.ddl import CreateTable

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:zzh223236@127.0.0.1:3306/奶茶'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "zzh223"
app.config['ENV'] = 'development'
db = SQLAlchemy(app)



class MilkteaGood(db.Model):
    __tablename__ = 'milktea_good'

    shopid = db.Column(db.ForeignKey('milktea_shop.shopid', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    title = db.Column(db.String(200), primary_key=True, nullable=False)
    price = db.Column(db.Float(asdecimal=True))
    value = db.Column(db.Float(asdecimal=True))

    milktea_shop = db.relationship('MilkteaShop', primaryjoin='MilkteaGood.shopid == MilkteaShop.shopid', backref='milktea_goods')



class MilkteaShop(db.Model):
    __tablename__ = 'milktea_shop'

    shopid = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(35), nullable=False)
    areaname = db.Column(db.String(35))
    backCateName = db.Column(db.String(20))
    avgprice = db.Column(db.Float(asdecimal=True))
    avgscore = db.Column(db.Float(asdecimal=True))
    latitude = db.Column(db.Float(asdecimal=True), nullable=False)
    longitude = db.Column(db.Float(asdecimal=True), nullable=False)
    comments = db.Column(db.BigInteger)
    historyCouponCount = db.Column(db.BigInteger)
    city = db.Column(db.String(20), nullable=False)




