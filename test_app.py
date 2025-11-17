from app import app

def test_home():
    response=app.test_client().get("/")
    ### Check that the response status code is 200 and the response data is "Hello World!"

    assert response.status_code==200
    assert response.data== b"Hello World!"