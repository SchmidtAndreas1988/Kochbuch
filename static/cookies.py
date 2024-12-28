from flask import Flask, make_response, request

def cookie():
    response = make_response("test")
    response.set_cookie("theme", "dark")
    return response


# def index():
#     # Rendere die HTML-Datei
#     response = make_response(render_template("index.html"))
    
#     # Setze das Cookie
#     response = create_cookie(response)
    
#     return response