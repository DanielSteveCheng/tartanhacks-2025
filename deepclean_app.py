from flask import Flask, render_template, url_for, request, redirect, Response
from camera import VideoCamera
import cv2

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main.html", result = url_for("deepClean"))

@app.route("/deepclean")
def deepClean():
    return render_template("result.html", home = url_for("main_page"))

def gen(camera):
    while True:
        frame = camera.get_frame()
        # timer = cv2.getTickCount()
        # fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
        # cv2.putText(frame, str(int(fps)), (75,58), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
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