// funcion para validar el formulario
export function validateForm(formData){
    let isValid = true // al comienzo siempre va a ser valido

    // capturo el formulario para limpiar los errores anteriores
    const form = document.getElementById("form")
    form.querySelectorAll(".is-invalid").forEach(el => {
        clearErrorText(el)
    })

    // recorre cada input del formulario y realiza las validaciones con sus metodos
    for(let [llave, valor] of formData.entries()){
        const input = document.getElementById(`id_${llave}`)
        if (!input) {
            continue
        }

        if (!input.dataset.listener){
            input.addEventListener('focus', ()=>{
                clearErrorText(input)
            })
            input.dataset.listener = "true"
        }

        valor = valor.trim()
        if(!valor){
            textErrorInput(input, "El campo está vacío")
            isValid = false
        }
        else if (llave === "nombre"){
            if(!validateInputNombre(input, valor)) isValid = false
        }
        else if (llave === "dia_preferido"){
            if(!validateSelectDiaPreferido(input, valor)) isValid = false
        }
        else if (llave === "telefono"){
            if(!validateInputTelefono(input, valor)) isValid = false
        }
    }
    return isValid
}

// Validaciones propias para cada campo
// validar input nombre
function validateInputNombre(input, valor){
    const patron = /^[a-záéíóúñ]+(?:\s[a-záéíóúñ]+)*$/i // verifica si es un nombre con solo letras Upper y Lower y espacios
    if(valor.length >= 2 && valor.length <= 100){
        if (!patron.test(valor)){
            textErrorInput(input, "El nombre no es válido")
            return false
        }
    }else{
        textErrorInput(input, "Nombre: de 2 a 100 caracteres")
        return false
    }
    return true
}

// Validar select dia preferido
function validateSelectDiaPreferido(input, valor){
    if (valor && valor !== ""){
        clearErrorText(input)
        return true
    }else{
        textErrorInput(input, "Seleccione un día preferido")
        return false
    }
}

//validar input telefono
function validateInputTelefono(input, valor){
    const patron =  /^\+?[0-9]{6,25}$/ // verifica si es un celular valido
    if(valor.length >= 6 && valor.length <= 25){
        if (!patron.test(valor)){
            textErrorInput(input, "El celular no es válido")
            return false
        }
    }else{
        textErrorInput(input, "Celular: de 6 a 25 caracteres")
        return false
    }
    return true
}

export function textErrorInput(input, msj){
    const errorText = document.getElementById(input.name + "-error")
    input.classList.add("is-invalid")
    if ( errorText ){
        errorText.textContent = msj
    }
}

export function clearErrorText(input){
    const errorText = document.getElementById(input.name + "-error")
    input.classList.remove("is-invalid")
    if ( errorText ){
        errorText.textContent = ""
    }
}