$(document).ready(function() {
    $(this).ajaxSubmit({
        url: "http://121.196.42.250/api/specificApis/user/getUsername",
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
                        url: "http://121.196.42.250/api/specificApis/login/logout",
                        type: "GET",
                        success: function(data) {
                            if (data.error) {
                                alert("请求失败！");
                            } else {
                                console.log("logout success");
                                window.location.href = "http://121.196.42.250/index";
                            }
                        }
                    });
                });
            }
        }
    });
});