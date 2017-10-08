<%@ page contentType="text/html; charset=UTF-8" %>
<html>
  <head>
    <title>
      TrashWeCan - UI
    </title>
    <script type="text/javascript"
            src="js/jquery-3.2.1.js">
    </script>
    <link rel="stylesheet" 
          type="text/css" 
          href="css/ui.css" />
  </head>

  <!-- BEGIN: header -->
  <div id="header">
    <script type="text/javascript">
      
      function updateUI ()
      {
        console.log("updating display");
        $.get({
          url: "status/case_no.json?v=latest",
          type: "GET",
          success: function(d,s)
               {
                 $('#userid').text("Welcome user " + d.case_no);
                 $('#ctrl_logout').show();
                 $('#ctrl_balance').show();
               },
          error:  function(d)
               {
                 $('#userid').text("No user logge in");
                 $('#ctrl_logout').hide();
                 $('#ctrl_balance').hide();
               }

        });
      }
      $(document).ready(function(){
        setInterval(updateUI,3000);
      });
    </script>
    <div id="welcome">
      <span id="userid">
        No user logged in
      </span>
    </div>
  </div>
  <!-- END: header -->
 
  <body>
