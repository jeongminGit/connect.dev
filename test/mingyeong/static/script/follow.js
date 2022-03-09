function follow(followingID) {
    let myID = $( "#myID" ).text();
    $.ajax({
        type: "POST",
        url: "/follow",
        data: {
                myID: myID,
                followingID: followingID
                },
        success: function (response) {
            alert(response['msg']);
            $('#recommendsCard').remove()
            location.reload();
        }
    })
}