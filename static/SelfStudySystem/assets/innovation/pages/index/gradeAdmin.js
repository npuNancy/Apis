$(document).ready(function() {

    $(this).ajaxSubmit({
        url: "/api/specificApis/gradeAdmin/GAgetClasses",
        type: "GET",
        success: function(data) {
            if (!data.error) {
                $("#my_grade").text("负责年级：" + data.grade);
                show_class(data.classes);
                show_users(data.users);
                classDelete(); // 删除班级
            } else {
                console.log(data.reason);
            }
        }
    });

    classAdd(); // 添加班级
    infoAdd(); // 批量添加学生信息
    changePassword(); // 更改密码
    logout();
});

// 显示班级列表
var show_class = function(classList) {
    var tbody = $("#tbody_class");
    var html = '';
    for (i in classList) {
        let classNum = classList[i].classNumber_id;
        let grade = classList[i].grade_id;
        let text = '<tr data-classId="' + classNum + '" >\n';
        text += '<th scope="row">' + classNum + '</th>\n';
        text += '<td>' + grade + '</td>\n';
        text += '<td><button type="button" class="btn btn-success classDelete">删除</button></td>\n</tr>\n';
        html += text;
    }
    tbody.append(html);
}

// 显示班级负责人列表
var show_users = function(userList) {
    var tbody = $("#tbody_user");
    var html = '';
    for (i in userList) {
        let username = userList[i].user;
        let classNum = userList[i].class;
        let text = '<tr data-username="' + username + '" >\n';
        text += '<th scope="row">' + username + '</th>\n';
        text += '<td>' + classNum + '</td>\n';
        // text += '<td><button type="button" class="btn btn-success classDelete">删除</button></td>\n';
        text += '</tr>\n';
        html += text;
    }
    tbody.append(html);
}

// 删除班级
var classDelete = function() {
    $(".classDelete").click(function() {
        var yes = confirm("确认删除?\n(若班级还存在学生，将拒绝级联删除！)")
        if (yes) {
            let tr = $(this).parents('tr');
            let classNumber = tr.attr("data-classId");
            $(this).ajaxSubmit({
                url: "/api/specificApis/gradeAdmin/GAclassDelete",
                type: "POST",
                data: {
                    "classNumber": classNumber
                },
                success: function(data) {
                    if (!data.error) {
                        console.log("success");
                        window.location.href = "/gradeAdminIndex";
                    } else {
                        console.log(data.reason);
                        alert("失败！\n");
                    }
                }
            });
        }
    });
}

// 添加班级
var classAdd = function() {
    $("#add_class").click(function() {
        var class_ = $("#class_name").val();
        if (class_ == '') {
            alert("不能为空!");
        } else {
            $(this).ajaxSubmit({
                url: "/api/specificApis/gradeAdmin/GAclassAdd",
                type: "POST",
                data: {
                    "classNumber": class_,
                },
                success: function(data) {
                    if (!data.error) {
                        window.location.href = "/gradeAdminIndex";
                    } else {
                        alert("添加失败!")
                        console.log(data);
                    }
                }
            })
        }
    })
}

// 注销
var logout = function() {
    $("#log_out").click(function() {
        $(this).ajaxSubmit({
            url: "/api/specificApis/gradeAdmin/gradeAdminLogout",
            type: "GET",
            success: function(data) {
                if (data.error) {
                    alert("请求失败！");
                } else {
                    console.log("logout success");
                    window.location.href = "/gradeAdminIndex";
                }
            }
        });
    });
}

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
            $(this).ajaxSubmit({
                url: "/api/specificApis/gradeAdmin/GAchangePass",
                type: "POST",
                data: {
                    "password_old": oldPass,
                    "password_new": pass1
                },
                success: function(data) {
                    if (!data.error) {
                        $("#log_out").click();
                    } else if (data.error == 3) {
                        alert("原密码错误!");
                    } else {
                        console.log(data.reason);
                    }
                }
            });
        }
    });
}

// 批量添加
var infoAdd = function() {
    $("#addInfos").click(function() {
        $("#form_addInfo").ajaxSubmit(function(data) {
            if (!data.error) {
                alert("导入成功");
                window.location.href = "adminIndex";
                console.log("success");
            } else if (data.error == -2) {
                alert("未上传文件");
            } else if (data.error == -3) {
                alert("添加失败, 需要上传.xlsx类型文件");
            } else if (data.error == -4) {
                alert("学号存在重复！请检查后再次上传");
            } else if (data.error == -5) {
                alert("班级不存在，请先创建班级后，再次上次");
            } else {
                alert("添加失败,请检查以下问题：\n1.需要上传.xlsx类型文件\n2.学号存在重复\n3.班级不存在，请先创建班级后，再次上次");
                console.log(data.reason);
            }
        })
    });
}