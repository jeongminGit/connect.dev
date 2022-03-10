function logout() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!');
    #("#beforeLoginNab").removeClass("hide");
    #("#afterLoginNab").addClass("hide");
    window.location.href = "/login1"
}