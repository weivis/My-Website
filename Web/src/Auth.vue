<script type="text/javascript">
    import Cookies from 'js-cookie'

    const LoginTokenID = 'LoginToken'
    const UserID = 'userID'

    function AuthUser() {
        // 如果 AuthUser为空 表示用户未登录
        console.log('>Auth: 获取用户登录状态')
        return Cookies.get(LoginTokenID)
    }

    function AuthUserData() {
        // 获取用户的登录数据
        console.log('>Auth: 获取用户登录缓存参数')
        return {
            token:Cookies.get(LoginTokenID),
            userid:Cookies.get(UserID)
        }
    }

    function Login_user(token, userid) {
        console.log('>Auth: 设置用户缓存参数')
        // 用户登录 Login_user(usertoken)
        Cookies.set(LoginTokenID, token)
        Cookies.set(UserID, userid)
        return
    }

    function Logout_user() {
        console.log('>Auth: 清空用户缓存参数')
        // 取消登录 Logout_user
        Cookies.remove(LoginTokenID)
        Cookies.remove(UserID)
        return
    }

    // 暴露出这些属性和方法
    export default {
        AuthUser,
        Login_user,
        Logout_user,
        LoginTokenID,
        AuthUserData
    }
</script>