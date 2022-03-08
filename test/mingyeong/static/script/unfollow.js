function unfollow() {
    let myID = $( "#myID" ).text();
    let followingID = $( "#followingUserID" ).text();
    $.ajax({
        type: "POST",
        url: "/unfollow",
        data: {
                myID: myID,
                followingID: followingID
                },
        success: function (response) {
            alert(response['msg']);
            $('#followingsCard').remove()
            location.reload();
        }
    })
}