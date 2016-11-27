// /* This example will only work in the latest browsers */
// const initApp = () => {
//   const registryToken = "4db6bb62-45e1-4451-a4f1-b8a8d3b1330b";
//
//   const login = () => {
//     Rosefire.signIn(registryToken, (err, rfUser) => {
//       if (err) {
//         return;
//       }
//       window.location.replace('/login?token=' + rfUser.token);
//     });
//   };
//   const loginButton = document.getElementById('login');
//   if (loginButton) {
//     loginButton.onclick = login;
//   }
// };

// window.onload = initApp;

var rosefire_login_click;
rosefire_login_click = function () {
    const registryToken = "4db6bb62-45e1-4451-a4f1-b8a8d3b1330b";
    Rosefire.signIn(registryToken, function (err, rfUser) {
        console.log('hit');
        if (err) {
            console.error(err);
        }
        window.location.replace('/login?token=' + rfUser.token);
    });
};

$(document).ready(function () {

});