% include('header.tpl', title='Upload')
<div class="row marketing">
  <div class="col-lg-6">

    % for k in topk:
    <h4>Venturing a guess...</h4>
    <p>{{k}}</p>
    % end

  </div>
</div>
% include('footer.tpl')
