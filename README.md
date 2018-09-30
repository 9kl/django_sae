# django_sae
django会话认证引擎，django多系统间会话、用户认证引擎。

## 安装
    pip install django-saengine

## 配置
在各个django web settings.py如下配置项
    
    AUTHENTICATION_BACKENDS = ('django_sae.auth.backends.ModelBackend',)
    
    SESSION_ENGINE = 'django_sae.session.backends.db'
    
    SAE_SESSION_SERVICE_URL = 'http://47.93.190.107:9107/session/'
    SAE_AUTHENTICATE_SERVICE_URL = 'http://47.93.190.107:9107/user/'
    SAE_ACCESS_TOKEN_SECRET = 'linkeddt.com'  # api访问者的身份认证，可以在api服务端为访问者身份进行安全认证
    
## django sae 接口开发
### session
1、接口必须返回的字段

- session_key 会话key
- session_data 会话数据
- expire_date 到期时间

2、接口需实现以下方法

- get_one(session_key)
- get_all()
- add(entity)
- modify(entity)
- delete(session_key)
- get_page_query(limit, offset, sort=None, order=None)
- exist_modify(entity)
- tran_delete(pks)
- clear()
- clear_expired()
- exists(session_key)

3、url 配置

    url(r'^session/$', AuthSessionList.as_view()),
    url(r'^session/pager/$', AuthSessionList.as_view(),
        {'MIME_TYPE': 'page_query'}),
    url(r'^session/exists_modify/$', AuthSessionList.as_view(),
        {'MIME_TYPE': 'exists_modify'}),
    url(r'^session/clear/$', AuthSessionList.as_view(),
        {'MIME_TYPE': 'clear'}),
    url(r'^session/clear_expired/$', AuthSessionList.as_view(),
        {'MIME_TYPE': 'clear_expired'}),
    url(r'^session/tran_delete/$', AuthSessionList.as_view(),
        {'MIME_TYPE': 'tran_delete'}),
    url(r'^session/(?P<pk>.*)/$', AuthSessionDetail.as_view()),
    
 ### 用户认证
1、接口必须返回的字段
- id 用户id
- login_name 登录名
- login_password 登陆密码
- user_name 用户名
- is_active  是否激活
- is_superuser 是否超级管理员
- is_read 是否只有只读权限
- photo 头像 （预留，后期可在主框架中显示头像）
- roles 所属角色

**建议字段：**

- first_name 姓氏
- last_name 名字
- is_leader 是否是领导
- is_dba 数据管理高级权限
- phone_number 手机号码
- email邮箱
- create_date 创建时间
- last_login_date 最后登陆时间
- last_login_ip 最后登陆ip
- wechat_json 微信绑定时间
- extend_json 扩展信息
- remark 备注


2、接口需要实现的方法
- get_one(user_id)
- get_all()
- authenticate(login_name, login_pwd)
- modify_pwd(user_id, old_pwd, new_pwd)

3、url配置

    url(r'^user/$', AuthUserList.as_view()),
    url(r'^user/authenticate/$', AuthUserList.as_view(),
        {'MIME_TYPE': 'authenticate'}),
    url(r'^user/(?P<pk>.*)/modify_pwd/$',
        AuthUserDetail.as_view(), {'MIME_TYPE': 'modify_pwd'}),
    url(r'^user/(?P<pk>.*)/$', AuthUserDetail.as_view()),


