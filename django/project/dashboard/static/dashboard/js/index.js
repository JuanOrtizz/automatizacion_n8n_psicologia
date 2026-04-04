import {successAlert} from './alerts.js'

const msgAlert = sessionStorage.getItem('msgSuccess')
if(msgAlert){ // Si mensaje de exito existe y no es null
    successAlert(msgAlert) // Muestra la alerta de Consulta modificada con exito
    sessionStorage.removeItem('msgSuccess') // Elimina el par clave-valor del sessionStorage
}