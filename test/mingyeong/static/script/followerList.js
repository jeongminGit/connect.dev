function followCheck2() {
    // myID 수정 필요함
    let myID = "snoopso"

    $.ajax({
        type: "GET",
        url: "/followCheck2",
        data: {},
        success: function (response) {
            let recommendList = response['recommendList'];
            let userList = response['userList'];
            const followerList = [];
            const userIDList = [];
            const RecommendsUserIDList = [];

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

            // 3. RecommendsUserIDList 와 동일한 값을 가진 id를 조회, id 값과 name 값 뿌려주기
            for (let i = 0; i < FollowerUserIDList.length; i++) {
                var returnValue = userList.find(function (data) {
                    return data.id == FollowerUserIDList[i]
                });
                console.log(returnValue['id'],returnValue['name']);
                let temp_html = `<div class="col-sm-3">
                                    <div class="card text-white bg-dark mb-3" id="followingsCard">
                                        <div class="card-body">
                                            <h5 class="card-title" id="followingUserID">${returnValue['id']}</h5>
                                            <p class="card-text">${returnValue['name']}</p>
                                            <a href="#" class="btn btn-outline-primary" onclick="unfollow()">언팔로우</a>
                                        </div>
                                    </div>
                                </div>`;
                $('#listFollowings').append(temp_html);
            }
        }
    })
}