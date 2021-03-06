var signInButton = document.getElementById('btn-signin');
var resultContainer = document.getElementById('result');

function signInCallback(authResult) {
  if (authResult.code) {
    signInButton.style.display = 'none';

    $.ajax({
      type: 'POST',
      url: '/gconnect?state={{STATE}}',
      processData: false,
      data: authResult['code'],
      contentType: 'application/octet-stream; charset=utf-8',
      success: function (result) {
        if (result) {
          // The login was successful
          resultContainer.innerHTML = 'Login Successful!<br><br>Redirecting...';

          setTimeout(function () {
            window.location.href = "/";
          }, 4000);

        } else if (authResult['error']) {

          resultContainer.innerHTML = 'Error: ' + authResult['error'];

        } else {
          // something failed

          resultContainer.innerHTML = 'Check your configuration.';
        }
      }

    });
  }
}
