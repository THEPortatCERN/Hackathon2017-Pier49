<%@ page contentType="text/html; charset=UTF-8" %>
<%@ include file="/common/header.jsp" %>
  
  <script type="text/javascript">
    $(document).ready(function(){
      $.get("status/balance.json?v=latest",
             function(d,s)
             {
               $('#balance').text(d.balance);
             }
      );
    });
  </script>

  <!-- BEGIN: content -->
  <div id="content">
    <h1>Current balance</h1>
    <div id="balance">
    </div>
  </div>
  <!-- END: content -->

<%@ include file="/common/footer.jsp" %>
