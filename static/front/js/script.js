function Select(choose, id, register_url, csrf) {
    var data;
    var csrftoken = csrf;
    var select = document.getElementById(choose);
    $(id).html("");       //每次重新选择当前列表框，就清空下一级列表框。
    for (i = 0; i < select.length; i++) {
        if (select[i].selected) {     //判断被选中项
            Name = select[i].text;
            data = {
                "name": Name
            };
            $.ajax({                       //发起ajax请求
                url: register_url,
                //加上csrf验证头，也可直接加在data里最前面
                headers: {"X-CSRFToken": csrftoken},
                type: "POST",
                data: JSON.stringify(data),
                contentType: "application/json; charset=UTF-8",
                success: function (data) {    //后端返回数据，是列表形式的
                    if (data) {
                        $("<option  value='--请选择--'></option>").appendTo(id);
                        for (i = 0; i < data.length; i++) {
                            $("<option value='" + data[i] + "'>" + data[i] + "</option>").appendTo(id)//将后端返回的数据逐项插入到下一级列表框中
                        }
                    } else {
                        alert('error');
                    }
                }
            });
        }
    }
}
