$(document).ready(function() {
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:80/api/specificApis/user/getUsername",
        type: "GET",
        success: function(data) {
            if (data.error) {
                // not login yet
                $("#user-name").text("游客");
                $("#userPic_1").attr("src", "../static/SelfStudySystem/assets/app/media/img/users/user.png");
                $("#userPic_2").attr("src", "../static/SelfStudySystem/assets/app/media/img/users/user.png");
                $(".login_out").attr("id", "login");
                $("#login_out").attr("href", "/login");
                $("#login_out").text("Login");
            } else {
                $("#user-name").text(data.result);
                $("#userPic_1").attr("src", "../static/SelfStudySystem/assets/app/media/img/users/user4.jpg");
                $("#userPic_2").attr("src", "../static/SelfStudySystem/assets/app/media/img/users/user4.jpg");
                $(".login_out").attr("id", "logout");

                $("#login_out").text("LogOut");

                $("#changePass").removeAttr("style");

                $("#logout").click(function() {
                    $(this).ajaxSubmit({
                        url: "http://127.0.0.1:80/api/specificApis/login/logout",
                        type: "GET",
                        success: function(data) {
                            if (data.error) {
                                alert("请求失败！");
                            } else {
                                console.log("logout success");
                                window.location.href = "http://127.0.0.1:80/index";
                            }
                        }
                    });
                });
            }
        }
    });
});

var sort = function(json, key) {
    return json.sort(function(a, b) {
        var x = parseInt(a[key]);
        var y = parseInt(b[key]);
        return ((x < y) ? -1 : ((x > y) ? 1 : 0));
    })
};

Date.prototype.format = function(fmt) {
    var o = {
        "M+": this.getMonth() + 1, //月份 
        "d+": this.getDate(), //日 
        "h+": this.getHours(), //小时 
        "m+": this.getMinutes(), //分 
        "s+": this.getSeconds(), //秒 
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度 
        "S": this.getMilliseconds() //毫秒 
    };
    if (/(y+)/.test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    }
    for (var k in o) {
        if (new RegExp("(" + k + ")").test(fmt)) {
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
        }
    }
    return fmt;
};