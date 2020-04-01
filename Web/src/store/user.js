export function QueryUserInfo() {
    console.log('>localStorage: 获取用户数据')
    return {
        UserName: localStorage.getItem('UserName'),
        UserId: localStorage.getItem('UserId'),
        UserHead: localStorage.getItem('UserHead')
    }
}

export function StoreUserInfo(username, userid, userhead) {
    console.log('>localStorage: 写入用户数据')
    localStorage.setItem('UserName', username)
    localStorage.setItem('UserId', userid)
    localStorage.setItem('UserHead', userhead)
    return QueryUserInfo()
}

export function ChangeUserInfo(ItemName, newdata) {
    console.log('>localStorage: 更新用户数据')
    localStorage.setItem(String(ItemName), newdata)
    return QueryUserInfo()
}

export function RemoveUserInfo() {
    console.log('>localStorage: 清除用户数据')
    localStorage.removeItem('UserName');
    localStorage.removeItem('UserId');
    localStorage.removeItem('UserHead');
    localStorage.clear();
    return QueryUserInfo()
}