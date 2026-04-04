import {successAlert, errorAlert, confirmAlert} from './alerts.js'

document.addEventListener('DOMContentLoaded', () => {
    const btnsDelete = document.querySelectorAll('.btn-delete')

    // Evento para evitar que se mande el form
    btnsDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault()
            const sesionId = btn.getAttribute("data-id")
            const csrfToken = btn.closest('form').querySelector('[name=csrfmiddlewaretoken]').value
            confirmAlert("¿Estás seguro que querés eliminar esta sesión?", "Eliminar", () => {
                btn.disabled = true
                btn.textContent = "Eliminando..."
                deleteForm(sesionId, csrfToken, btn)
            })
        })
    })
})

// funcion async para utilizar await y manejar asincronia
async function deleteForm(sesionId, csrfToken, btn) {
    try {
        const response = await fetch(`/eliminar-sesion/${sesionId}/`, {
            method:"POST",
            headers:{
                "X-CSRFToken": csrfToken
            }
        })
        const data = await response.json()
        if(data.success) {
            const sesionTr = document.getElementById(`sesion-${sesionId}`)
            const sesionCard = document.getElementById(`sesion-card-${sesionId}`)
            if(sesionTr && sesionCard) {
                sesionTr.remove()
                sesionCard.remove()
                successAlert(data.message)

                // Verificar si quedan sesiones
                const elements = document.querySelectorAll(".sesion-item")
                console.log(elements.length)
                // Verificar si ya no queda ninguno
                if (elements.length === 0) {
                    const containerNoSesions = document.getElementById("no-sesions-message")
                    containerNoSesions.classList.remove("d-none")
                }

            }
        } else {
            const errors = data.errors
            if (typeof errors === "string") {
                errorAlert(data.errors)
            }
        }
    } catch(error) {
        errorAlert("Ocurrió un error inesperado. Intentá más tarde.")
    } finally {
        btn.disabled = false
        btn.textContent = "Eliminar"
    }
}