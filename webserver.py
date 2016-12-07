#!/usr/bin/env python
import os, sys, time
from bottle import route, run, template, static_file, request, response

import classify_image as ci

def predict(image):
  ci.run_inference_on_image(image)

@route('/')
def index():
  return ['''
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="text" name="name" value="default.jpg" />
    <input type="file" name="data" accept="video/*;capture=camcorder" />
</form>
''']

@route('/static/<path:path>')
def server_static(path):
  return static_file(path, root='./static/')

@route('/upload', method='POST')
def do_upload():
  name = request.forms.name
  data = request.files.data
  if name and data and data.file:
    pathname = 'static/'+name
    new_pathname = 'static/'+time.ctime().replace(' ','-')+'.'+name
    print("SAVING FILE:"+new_pathname)
    data.save(new_pathname,overwrite=True)
    filename = data.filename
    print("WORKING ON PREDICTING")
    predict(new_pathname)
    print("DONE PREDICTING")
    return """Hello %s! You uploaded %s (%s).
<a href="%s">%s</a>
""" % (
  name, pathname, filename, new_pathname, new_pathname)
    return "You missed a field."

def main():
  ci.xmain()
  try:
    os.mkdir('static')
  except:
    pass
  ci.maybe_download_and_extract()
  predict('default7.jpg') # prime the pump
  return run(host='', port=80)

if __name__=='__main__': main()
