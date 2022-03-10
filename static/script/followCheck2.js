function followCheck2() {

    $.ajax({
        type: "GET",
        url: "/followCheck2",
        data: {},
        success: function (response) {
            const myID = response['id']
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

            // 3. RecommendsUserIDList 와 동일한 값을 가진 id를 조회, id 값과 name 값 뿌려주기
            for (let i = 0; i < RecommendsUserIDList.length; i++) {
                var returnValue = userList.find(function (data) {
                    return data.id == RecommendsUserIDList[i]
                });
                console.log(returnValue['id'],returnValue['name']);
                let temp_html = `<div class="col-sm-3">
                                    <div class="card text-white bg-dark mb-3" id="followingsCard">
                                        <div class="card-body">
                                            <h5 class="card-title" id="followingUserID">${returnValue['name']}</h5>
                                            <p class="card-text">${returnValue['job']}</p>
                                            <p class="badge">${returnValue['num']}</p>
                                            <div class="d-grid gap-2">
                                                <a href="#" class="btn btn-outline-primary" onclick="unfollow(this.id)" id="${returnValue['id']}">언팔로우</a>
                                            <div>
                                        </div>
                                    </div>
                                </div>`;
                $('#listFollowings').append(temp_html);
            }
        }
    })
}