$(document).ready(function() {
    $(this).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/studentData/getClassStudents",
        type: "GET",
        success: function(data) {
            if (!data.error) {
                var stu = data.result;
                stu = sort(stu, 'studentId');
                details(stu)
                signOut();
                signIn();
                askLeave();
            } else {
                console.log(data.reason);
            }
        }
    });
});

// 页面载入时加载这个班所有同学
var details = function(students) {
    var tbody = $("#tbody");
    var html = '';
    for (i in students) {
        let studentId = students[i].studentId;
        let ret = getState(studentId);
        let state = ret.state;
        let st = '';
        let et = '';
        let dataId = '';
        let btn1_color = '';
        let btn2_color = '';
        let btn1_name = '';
        let btn1_text = '开始';
        let btn1_dis = '';
        let btn2_dis = '';
        let points = '';
        // 空格
        if (ret.state == 0) {
            btn1_color = 'btn-success ';
            btn1_name = 'btn-Start ';
            btn2_color = 'btn-primary '
        } else if (ret.state == 1) {
            btn1_dis = 'disabled ';
            btn2_dis = 'disabled ';
        } else if (ret.state == 2) {
            btn1_color = 'btn-danger ';
            btn1_name = 'btn-End ';
            btn1_text = '结束';
            btn2_dis = 'disabled ';
            dataId = ret.dataId;
            st = new Date(ret.starttime + ' GMT+00:00');
            st = st.format("yyyy-MM-dd hh:mm:ss");
        } else if (ret.state == 3) {
            btn1_color = 'btn-success ';
            btn1_name = 'btn-Start ';
            btn2_dis = 'disabled ';
            st = new Date(ret.starttime + ' GMT+00:00');
            et = new Date(ret.endtime + ' GMT+00:00');
            st = st.format("yyyy-MM-dd hh:mm:ss");
            et = et.format("yyyy-MM-dd hh:mm:ss");
            points = String(ret.points);
        }
        let text = '<tr data-state=' + state + ' data-studentId=' + studentId + ' data-dataid=' + dataId + '>\n';
        text += '<th scope="row">' + studentId + '</th>\n';
        text += '<td>' + students[i].name + '</td>\n';
        text += '<td class="sT">' + st + '</td>\n';
        text += '<td class="eT">' + et + '</td>\n';
        text += '<td>' + points + '</td>\n';
        text += '<td><button type="button" class="btn ' + btn1_color + btn1_name + '"' + btn1_dis + '>' + btn1_text + '</button></td>\n';
        text += '<td><button type="button" class="btn ' + btn2_color + ' btn-askLeave"' + btn2_dis + '>请假</button></td>\n</tr>\n';
        html += text;
    }
    tbody.append(html)
};

var getState = function(studentId) {
    var ret;
    $(document).ajaxSubmit({
        url: "http://127.0.0.1:8000/api/specificApis/studentData/getStudentstates",
        type: "POST",
        async: false,
        data: {
            'studentId': studentId
        },
        success: function(data) {
            if (!data.error) {
                ret = data
            } else {
                console.log(data.reason);
            }
        }
    });
    return ret;
}

var askLeave = function() {
    $(".btn-askLeave").click(function() {
        var tr = $(this).parents('tr');
        var studentId = tr.attr('data-studentId');
        $(this).ajaxSubmit({
            url: "http://127.0.0.1:8000/api/specificApis/studentData/askLeave",
            type: "POST",
            data: {
                "studentId": studentId
            },
            success: function(data) {
                if (!data.error) {
                    var info = data.values;
                    tr.attr('data-dataid', info.id);
                    tr.find(".btn-Start").removeClass('btn-success');
                    tr.find(".btn-Start").attr('disabled', true);
                    tr.find(".btn-askLeave").removeClass('btn-primary');
                    tr.find(".btn-askLeave").attr('disabled', true);
                } else {
                    console.log(data.reason);
                }
            }
        });
        window.location.reload();
    });
};

var signIn = function() {
    $(".btn-Start").click(function() {
        var tr = $(this).parents('tr');
        var studentId = tr.attr('data-studentId');
        $(this).ajaxSubmit({
            url: "http://127.0.0.1:8000/api/specificApis/studentData/signIn",
            type: "POST",
            data: {
                "studentId": studentId
            },
            success: function(data) {
                if (!data.error) {
                    var info = data.values;
                    var t = new Date(info.startTime + ' GMT+00:00');
                    tr.attr('data-dataid', info.id);
                    tr.attr('data-state', info.state);
                    tr.find(".sT").text(t.format("yyyy-MM-dd hh:mm:ss")); //开始时间

                    tr.find(".btn-Start").text("结束");
                    tr.find(".btn-Start").addClass('btn-danger btn-End');
                    tr.find(".btn-Start").removeClass('btn-success btn-Start');

                    tr.find(".btn-askLeave").removeClass('btn-primary'); //请假按钮
                    tr.find(".btn-askLeave").attr('disabled', true);

                    window.location.reload();
                } else if (data.error == 2) {
                    alert("不在规定时间内！请在18:30-22:30执行此操作");
                } else {
                    console.log(data.reason);
                }
            }
        });
    });
};

var signOut = function() {
    $('.btn-End').click(function() {
        var tr = $(this).parents('tr');
        var studentId = tr.attr('data-studentId');
        var dataId = tr.attr('data-dataid');
        $(this).ajaxSubmit({
            url: "http://127.0.0.1:8000/api/specificApis/studentData/signOut",
            type: "POST",
            data: {
                "studentId": studentId,
                "dataId": dataId
            },
            success: function(data) {
                if (!data.error) {
                    var info = data.values;
                    var t = new Date(info.endTime + ' GMT+00:00');
                    tr.attr('data-dataid', '');
                    tr.attr('data-state', info.state);
                    tr.find(".eT").text(t.format("yyyy-MM-dd hh:mm:ss")); //开始时间

                    tr.find(".btn-End").text("开始");
                    tr.find(".btn-End").addClass('btn-success btn-Start');
                    tr.find(".btn-End").removeClass('btn-danger btn-End');

                    window.location.reload();
                } else {
                    console.log(data.reason);
                }
            }
        });
    });
};