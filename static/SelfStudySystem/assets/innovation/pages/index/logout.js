$("#logout").click(function() {
    $(this).ajaxSubmit({
        url: "http://121.196.42.250/api/specificApis/login/logout",
        type: "GET",
        success: function(data) {
            if (data.error) {
                alert("请求失败");
            } else {
                console.log("logout success");
                window.location.href = "http://121.196.42.250/index";
            }
        }
    });
});