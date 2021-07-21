from flask import Flask, request
from main import app
import pytest
app = Flask(__name__)

def test_hello():
        response = app.test_client().get('/hello?name=Peter')
        assert response.status_code == 200
        assert response.data == b'Hello Peter'

def test_minmax():
    response = app.test_client().get('/minmax')
    assert response.status_code == 200

def test_grade():
    response = app.test_client().post('/calculate_exam_grade')
    assert response.status_code == 200

def test_sum():
    response = app.test_client().post('/sum?number1=2&number2=2')
    assert response.status_code == 200
    assert response.data == b'2 + 2 = 4.0'