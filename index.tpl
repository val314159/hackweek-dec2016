% include('header.tpl', title='Index')
<div class="jumbotron">
  <h1>Upload Me A Picture</h1>
  <p class="lead">Yeah, that's right.  Let's do some classifying!</p>
  <form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="hidden" name="name" value="default.jpg" />
    <div class="form-group">
      <label for="exampleInputFile">File input</label>
      <input type="file" name="data" accept="video/*;capture=camcorder" value="sdfdsg" />
      <p class="help-block">Hit the button above and click to queue up the picture!</p>
    </div>
    <div class="form-group">
      <p><input class="btn btn-lg btn-success" xhref="#" role="button" value="Send a Pic" type="submit" /></p>
    </div>
  </form>
</div>
% include('footer.tpl')
