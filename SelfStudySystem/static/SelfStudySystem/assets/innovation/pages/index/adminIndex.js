$(document).ready(function() {
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/admin/gradeAdminGetAll",
        type: "GET",
        success: function(data) {
            if (!data.error) {
                show_grade_admin(data.result); // 显示年级管理员列表
                gradeAdminDelete(); // 删除年级管理员
                changePassword(); // 修改密码
                addGradeAdmin(); // 添加年级管理员
            } else {
                console.log(data.reason);
            }
        }
    });

    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/grade/gradeGetAll",
        type: "GET",
        success: function(data) {
            if (!data.error) {
                if_no_grade(data.result);
                show_grade(data.result);
                add_grade_toForm(data.result);
                gradeDelete(); // 删除年级
                gradeAdd(); // 添加年级
            } else {
                console.log(data.reason);
            }
        }
    });

    $("#log_out").click(function() {
        $(this).ajaxSubmit({
            url: "http://127.0.0.1:8000/api/specificApis/admin/logout",
            type: "GET",
            success: function(data) {
                if (data.error) {
                    alert("请求失败！");
                } else {
                    console.log("logout success");
                    window.location.href = "http://127.0.0.1:8000/adminIndex";
                }
            }
        });
    });
});


// 修改密码
var changePassword = function() {
    $("#change_pass").click(function() {
        var oldPass = $("#password-old").val();
        var pass1 = $("#password1").val();
        var pass2 = $("#password2").val();
        if (pass1 == '' || pass2 == '' || oldPass == '') {
            alert("密码不能为空")
        } else if (pass1 != pass2) {
            alert("2次密码不相同！");
        } else {
            var flag = false;
            $(this).ajaxSubmit({
                url: "http://127.0.0.1:8000/api/specificApis/admin/checkPass",
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
                    url: "http://127.0.0.1:8000/api/specificApis/admin/changePass",
                    type: "POST",
                    data: {
                        "password": pass1
                    },
                    success: function(data) {
                        if (!data.error) {
                            $("this").ajaxSubmit({
                                url: "http://127.0.0.1:8000/api/specificApis/admin/logout",
                                type: "GET"
                            })
                            window.location.href = "http://127.0.0.1:8000/adminLogin";
                        } else {
                            console.log(data.reason);
                        }
                    }
                })
            }
        }
    });
}

// 显示年级管理员列表
var show_grade_admin = function(gradeAdminList) {
    var tbody = $('#tbody_gradeAdmin');
    var html = '';
    for (i in gradeAdminList) {
        let username = gradeAdminList[i].username;
        let garde = gradeAdminList[i].grade;
        let text = '<tr data-username="' + username + '" >\n';
        text += '<th scope="row">' + username + '</th>\n';
        text += '<td>' + garde + '</td>\n';
        text += '<td><button type="button" class="btn btn-success gradeAdminDelete ">删除</button></td>\n</tr>\n';
        html += text;
    }
    tbody.append(html);
}

// 删除年级管理员
var gradeAdminDelete = function() {
    $(".gradeAdminDelete").click(function() {
        var yes = confirm("确认删除?")
        if (yes) {
            let tr = $(this).parents('tr');
            let username = tr.attr("data-username");
            $(this).ajaxSubmit({
                url: "http://127.0.0.1:8000/api/specificApis/admin/gradeAdminDelete",
                type: "POST",
                data: {
                    "username": username
                },
                success: function(data) {
                    if (!data.error) {
                        console.log("success");
                        window.location.href = "http://127.0.0.1:8000/adminIndex";
                    } else {
                        console.log(data.reason);
                        alert("失败！\n");
                    }
                }
            });
        }

    });
}

// 添加年级管理员
var addGradeAdmin = function() {
    $("#add_grade_user").click(function() {
        var username = $("#username_grade").val();
        var pass1 = $("#password_1").val();
        var pass2 = $("#password_2").val();
        var gradeId = $("#grade_Select1").val();
        if (pass1 == '' || pass2 == '' || username == '') {
            alert("用户名或密码不能为空")
        } else if (pass1 != pass2) {
            alert("2次密码不相同！");
        } else if (gradeId == '') {
            alert("请选择管理年级！");
        } else {
            $(this).ajaxSubmit({
                url: "http://127.0.0.1:8000/api/specificApis/admin/gradeAdminAdd",
                type: "POST",
                data: {
                    "username": username,
                    "password": pass1,
                    "gradeId": gradeId
                },
                success: function(data) {
                    if (!data.error) {
                        window.location.href = "http://127.0.0.1:8000/adminIndex";
                    } else {
                        alert("添加失败！");
                        console.log(data.reason);
                    }
                }
            })
        }

    });
}

// 如果没有年级，把添加年级管理员的按钮取消，并显示warning
var if_no_grade = function(gradeList) {
    if (!gradeList.length) {
        $("#add_grade_user").attr("disabled", true); //btn btn-metal
        $("#add_grade_user").removeClass('btn-primary');
        $("#add_grade_user").addClass('btn-metal');
        $(".m_modal_add_grade_admin_warning").show();
    }
}

// 把年级加入`添加年级管理员`的下拉列表中
var add_grade_toForm = function(gradeList) {
    var selectBody = $("#grade_Select1");
    let html = "";
    for (i in gradeList) {
        let gradeId = gradeList[i].id;
        let grade = gradeList[i].grade;
        let college = gradeList[i].college;
        html += '<option value="' + gradeId + '">' + grade + ' ' + college + ' </option>\n';
    }
    selectBody.append(html);
}

// 显示年级列表
var show_grade = function(gradeList) {
    var tbody = $('#tbody_grade');
    var html = '';
    for (i in gradeList) {
        let gradeId = gradeList[i].id;
        let grade = gradeList[i].grade;
        let college = gradeList[i].college;
        let text = '<tr data-gradeId="' + gradeId + '" >\n';
        text += '<th scope="row">' + grade + '</th>\n';
        text += '<td>' + college + '</td>\n';
        text += '<td><button type="button" class="btn btn-success gradeDelete">删除</button></td>\n</tr>\n';
        html += text;
    }
    tbody.append(html);
}

// 删除年级 
var gradeDelete = function() {
    $(".gradeDelete").click(function() {
        var yes = confirm("确认删除?")
        if (yes) {
            let tr = $(this).parents('tr');
            let gradeId = tr.attr("data-gradeId");
            $(this).ajaxSubmit({
                url: "http://127.0.0.1:8000/api/specificApis/grade/gradeDelete",
                type: "POST",
                data: {
                    "gradeId": gradeId
                },
                success: function(data) {
                    if (!data.error) {
                        console.log("success");
                        window.location.href = "http://127.0.0.1:8000/adminIndex";
                    } else {
                        console.log(data.reason);
                        alert("失败！\n");
                    }
                }
            });
        }
    })
}

// 添加年级
var gradeAdd = function() {
    $("#add_grade").click(function() {
        var grade = $("#grade_name").val();
        var college = $("#grade_college").val();
        if (grade == '' || college == '') {
            alert("不能为空!");
        } else {
            $(this).ajaxSubmit({
                url: "http://127.0.0.1:8000/api/specificApis/grade/gradeAdd",
                type: "POST",
                data: {
                    "grade": grade,
                    "college": college
                },
                success: function(data) {
                    if (!data.error) {
                        window.location.href = "http://127.0.0.1:8000/adminIndex";
                    } else {
                        alert("添加失败!")
                        console.log(data);
                    }
                }
            })
        }
    })
}