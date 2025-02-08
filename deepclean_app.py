from flask import Flask, render_template, url_for, request, redirect, Response
from camera import VideoCamera

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main.html", result = url_for("deepClean"))

@app.route("/deepclean")
def deepClean():
    return render_template("result.html")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame
               + b'\r\n\r\n')

# @app.route("/result", methods=["GET", "POST"])
# def christmas_story():

#     return render_template("result.html")


@app.route("/video_feed")
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype = 'multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)