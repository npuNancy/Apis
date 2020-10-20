$(document).ready(function() {
    $(".btn-accent").click(function() {
        var oldPass = $("#password-old").val();
        var pass1 = $("#password1").val();
        var pass2 = $("#password2").val();
        if (pass1 == '' || pass2 == '' || oldPass == '') {
            alert("密码不能为空")
        } else if (pass1 != pass2) {
            alert("2次密码不相同！");
        } else {
            console.log("#####")
            console.log(pass1)
            console.log(pass2)
            var flag = false;
            $(this).ajaxSubmit({
                url: "http://121.196.42.250/api/specificApis/user/checkPass",
                type: "POST",
                data: {
                    "password": oldPass
                },
                async: false,
                success: function(data) {
                    if (!data.error) {
                        flag = true;
                    } else if (data.error == 3) {
                        alert("原密码错误!");
                    } else {
                        console.log(data.reason);
                    }
                }
            });
            if (flag) {
                $(this).ajaxSubmit({
                    url: "http://121.196.42.250/api/specificApis/user/changePass",
                    type: "POST",
                    data: {
                        "password": pass1
                    },
                    success: function(data) {
                        if (!data.error) {
                            $("this").ajaxSubmit({
                                url: "http://121.196.42.250/api/specificApis/login/logout",
                                type: "GET"
                            })
                            window.location.href = "http://121.196.42.250/login";
                        } else {
                            console.log(data.reason);
                        }
                    }
                })
            }
        }
    });
});