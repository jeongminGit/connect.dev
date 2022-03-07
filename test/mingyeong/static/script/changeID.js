function changeID() {
    $.ajax({
        type: "GET",
        url: "/myID",
        data: {},
        success: function (response) {
            let myID = response['myID'][0]['id']
            $( "#myID" ).text(myID)
        }
    })
}