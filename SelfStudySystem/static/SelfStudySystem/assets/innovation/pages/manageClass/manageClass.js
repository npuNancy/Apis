// 请求返回classnumber
$(document).ready(function() {
    var classNumber;
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/user/getUserClassNumber",
        type: "POST",
        async: false,
        success: function(data) {
            if (!data.error) {
                classNumber = data.classNumber;
                $('.classId').text('班号：' + data.classNumber)
            } else {
                console.log(data.reason);
            }
        }
    });
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/show/getClassData",
        type: "POST",
        data: {
            'classNumber': classNumber
        },
        success: function(data) {
            if (!data.error) {
                var students = data.data;
                details(students);
                btn_delete();
                btn_edit()
            } else {
                console.log(data.reason);
            }
        }
    });
});

var details = function(students) {
    var html = '';
    for (i in students) {
        let stuId = students[i].studentId;
        let name = students[i].name;
        html += '<tr data-studentId="' + stuId + '">\n';
        html += '<th scope="row">' + stuId + '</th>\n';
        html += '<td>' + name + '</td>\n';
        html += '<td><button type="button" class="btn btn-primary btn-edit">编辑</button></td>\n';
        html += '<td><button type="button" class="btn btn-danger btn-delete">删除</button></td>\n</tr>\n'
    }
    $('#tbody').append(html);
};


var btn_edit = function() {
    $(".btn-edit").click(function() {
        var tr = $(this).parents('tr');
        var studentId = tr.attr('data-studentId');
        // 转到编辑页面
        window.location.href = 'http://127.0.0.1:8000/studentEdit?studentId=' + studentId;
    });
};

var btn_delete = function() {
    $(".btn-delete").click(function() {
        var yes = confirm("确认删除?")
        if (yes) {
            var tr = $(this).parents('tr');
            var studentId = tr.attr('data-studentId');
            $(this).ajaxSubmit({
                url: "http://127.0.0.1:8000/api/specificApis/student/delete",
                type: "POST",
                data: {
                    "studentId": studentId
                },
                success: function(data) {
                    if (!data.error) {
                        console.log("success");
                        window.location.href = 'http://127.0.0.1:8000/manageClass'
                    } else {
                        console.log(data.reason);
                        alert("失败！\n原因：" + data.reason);
                    }
                }
            });
            window.location.reload();
        }
    });
};