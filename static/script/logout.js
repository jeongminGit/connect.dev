function logout() {
    $.removeCookie('mytoken', {path: '/'});
    alert('๋ก๊ทธ์์!');
    #("#beforeLoginNab").removeClass("hide");
    #("#afterLoginNab").addClass("hide");
    window.location.href = "/login1"
}