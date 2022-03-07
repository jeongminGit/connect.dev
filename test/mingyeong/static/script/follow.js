function follow() {
    let myID = $( "#myID" ).text();
    let followingID = $( "#recommendUserID" ).text();
    $.ajax({
        type: "POST",
        url: "/follow",
        data: {
                myID: myID,
                followingID: followingID
                },
        success: function (response) {
            alert(response['msg']);

        }
    })
}