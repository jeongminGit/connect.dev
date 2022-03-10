function followerNum() {
    // myID 수정 필요함
    let myID = "snoopso"

    $.ajax({
        type: "GET",
        url: "/followerNum",
        data: {},
        success: function (response) {
            let recommendList = response['recommendList'];
            let userList = response['userList'];
            const followerList = [];
            const userIDList = [];
            const FollowerUserIDList = [];

            // 1. 만약 내 아이디를 팔로우하고 있다면 해당 follower 아이디를 출력
            for (let i = 0; i < recommendList.length; i++) {
                let followerID = response['recommendList'][i]['user_id'];
                let userID = response['recommendList'][i]['following_id'];
                if (myID == userID) {
                    followerList.push(followerID);
                }
            }
            console.log(followerList)

            // 2. 자기 자신일 경우 제외하고 FollowerUserIDList Array 값 넣어주기
            for (let i = 0; i < followerList.length; i++) {
                FollowerUserIDList.push(followerList[i]);
            }

            let followerNum = FollowerUserIDList.length
            $('#followerNum').text('('+followerNum+')')
            }


    })
}