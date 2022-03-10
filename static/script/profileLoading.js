function profileLoading() {
            var url_string = window.location.href;
            var url = new URL(url_string);
            var param = url.searchParams.get("id");
        // $.ajax({
        //     type: "GET",
        //     url: "/profileEach/?id="+param,
        //     data: {},
        //     success: function (response) {
        //         alert('hellow');
        //     }
        // })
    }