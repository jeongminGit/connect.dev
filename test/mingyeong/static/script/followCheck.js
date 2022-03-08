function followCheck() {
    // myID 수정 필요함
    let myID = "snoopso";

    $.ajax({
        type: "GET",
        url: "/followCheck",
        data: {},
        success: function (response) {
            let recommendList = response['recommendList'];
            let userList = response['userList'];
            const followingList = [];
            const userIDList = []
            const RecommendsUserIDList = []

            // 1. 만약 내 아이디가 팔로우하고 있다면 해당 following 아이디를 출력
            for (let i = 0; i < recommendList.length; i++) {
                let userID = response['recommendList'][i]['user_id'];
                let followingID = response['recommendList'][i]['following_id'];
                if (myID == userID) {
                    followingList.push(followingID);
                }
            }

            // 2. 만약 followingList의 내용과 동일한 아이디가 아닐 경우 출력
            for (let i = 0; i < userList.length; i++) {
                userIDList.push(userList[i]['id']);
            }
            let followID = userIDList.filter(x => !followingList.includes(x))

            // 3. 자기 자신일 경우 제외하고 RecommendsUserIDList Array 값 넣어주기
            for (let i = 0; i < followID.length; i++) {
                if (followID[i] !== myID) {
                    RecommendsUserIDList.push(followID[i]);
                }
            }

            // 4. RecommendsUserIDList 와 동일한 값을 가진 id를 조회, id 값과 name 값 뿌려주기
            for (let i = 0; i < RecommendsUserIDList.length; i++) {
                var returnValue = userList.find(function (data) {
                    return data.id == RecommendsUserIDList[i]
                });
                console.log(returnValue['id'], returnValue['name']);
                let temp_html = `<div class="col-sm-3">
                                      <div class="card text-white bg-dark mb-3" id="recommendsCard">
                                          <div class="card-body">
                                              <h5 class="card-title" id="recommendUserID">${returnValue['id']}</h5>
                                              <p class="card-text">${returnValue['name']}</p>
                                              <a href="#" class="btn btn-primary" onclick="follow()">팔로우</a>
                                          </div>
                                      </div>
                                  </div>`;
                $('#listRecommends').append(temp_html);

            }
        }
    })
}