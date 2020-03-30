export function QueryUserInfo() {
    return {
        UserName: localStorage.getItem('UserName'),
        UserId: localStorage.getItem('UserId'),
        UserHead: localStorage.getItem('UserHead')
    }
}

export function StoreUserInfo(username, userid, userhead) {
    localStorage.setItem('UserName', username)
    localStorage.setItem('UserId', userid)
    localStorage.setItem('UserHead', userhead)
    return QueryUserInfo()
}

export function ChangeUserInfo(ItemName, newdata) {
    localStorage.setItem(String(ItemName), newdata)
    return QueryUserInfo()
}

export function RemoveUserInfo() {
    localStorage.removeItem('UserName');
    localStorage.removeItem('UserId');
    localStorage.removeItem('UserHead');
    localStorage.clear();
    return QueryUserInfo()
}