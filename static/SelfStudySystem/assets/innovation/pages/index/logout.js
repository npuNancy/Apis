$("#logout").click(function() {
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/login/logout",
        type: "GET",
        success: function(data) {
            if (data.error) {
                alert("请求失败");
            } else {
                console.log("logout success");
                window.location.href = "http://127.0.0.1:8000/index";
            }
        }
    });
});