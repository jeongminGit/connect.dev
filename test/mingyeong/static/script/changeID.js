function changeID() {
    $.ajax({
        type: "GET",
        url: "/myID",
        data: {},
        success: function (response) {
            let myID = response['myID'][0]['id'];
            console.log(myID);
            $( "#myID" ).text(myID)
        }
    })
}