import {successAlert} from './alerts.js'

const msgAlert = sessionStorage.getItem('msgSuccess')
if(msgAlert){
    successAlert(msgAlert)
    sessionStorage.removeItem('msgSuccess')
}