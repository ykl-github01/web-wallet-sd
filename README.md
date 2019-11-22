## TM
* <span id = "strategy">全局策略</span>

    * 接口地址：/p/global/strategy

    * 请求方式：Post

    * 接口备注：通过用户信息，请求获得全局策略。

    * 请求参数说明：

        | 名称 | 类型 | 必填 |说明|
        |----- |------| ---- |----|
        |marking |string|true|企业标识|
        |<font color=red>account | string |true|用户名|
        |<font color=red>pw | string |true|用户密码|

    * JSON返回示例：

             {
                 "rt": 0,
                 "data": {
                     "identify_method": "3",
                     "send_url": "www.jianshu.com"
                 }
             }


---

