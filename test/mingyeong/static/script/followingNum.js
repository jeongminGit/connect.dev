function followingNum() {
    // myID 수정 필요함
    let myID = "snoopso"

    $.ajax({
        type: "GET",
        url: "/followingNum",
        data: {},
        success: function (response) {
            let recommendList = response['recommendList'];
            let userList = response['userList'];
            const followingList = [];
            const userIDList = [];
            const RecommendsUserIDList = [];

            // 1. 만약 내 아이디가 팔로우하고 있다면 해당 following 아이디를 출력
            for (let i = 0; i < recommendList.length; i++) {
                let userID = response['recommendList'][i]['user_id'];
                let followingID = response['recommendList'][i]['following_id'];
                if (myID == userID) {
                    followingList.push(followingID);
                }
            }
            console.log(followingList)

            // 2. 자기 자신일 경우 제외하고 RecommendsUserIDList Array 값 넣어주기
            for (let i = 0; i < followingList.length; i++) {
                if (followingList[i] !== myID) {
                    RecommendsUserIDList.push(followingList[i]);
                }
            }

            let followingNum = followingList.length
            $('#followingNum').text('('+followingNum+')')
            }
    })
}