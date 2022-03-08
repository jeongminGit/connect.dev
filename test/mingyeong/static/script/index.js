$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "/myID",
        data: {},
        success: function (response) {
            let myID = response['myID'][0]['id']
            $( "#myID" ).text(myID)
        }
    })

    let followingList = [];
    $.ajax({
        type: "GET",
        url: "/followCheck",
        data: {},
        success: function (response) {
            let recommendList = response['recommendList'];
            for (let i = 0; i < recommendList.length; i++){
                let myID = $("#myID").text();
                let userID = response['recommendList'][i]['user_id'];
                let followingID = response['recommendList'][i]['following_id'];
                console.log(userID, followingID)

                if (myID == userID) {
                    followingList.push(followingID);
                }
            }
        }
    })

    console.log(followingList)

    // $.ajax({
    //     type: "GET",
    //     url: "/recommendList",
    //     data: {},
    //     success: function (response) {
    //         let recommendList = response['listID'];
    //         for (let i = 0; i < recommendList.length; i++){
    //             let recommendID = response['listID'][i]['id'];
    //             console.log(followingList);
    //             console.log(recommendID);
    //             if (myID == userID) {
    //                 followingList.push(followingID);
    //                 let temp_html = `<div class="col-sm-3">
    //                                 <div class="card text-white bg-dark mb-3" id="recommendsCard">
    //                                     <div class="card-body">
    //                                         <h5 class="card-title" id="recommendUserID">${recommendID}</h5>
    //                                         <p class="card-text">Recommend</p>
    //                                         <a href="#" class="btn btn-primary" onclick="follow()">팔로우</a>
    //                                     </div>
    //                                 </div>
    //                             </div>`;
    //                 $('#listRecommends').append(temp_html);
    //             }
    //         }
    //     }
    // })
});