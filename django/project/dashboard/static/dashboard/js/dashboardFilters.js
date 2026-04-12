document.addEventListener('DOMContentLoaded', ()=>{
    const selectFilterFechaRegistro = document.getElementById("filter-fecha-registro")
    const selectFilterDiaSesion = document.getElementById("filter-dia-sesion")

   selectFilterFechaRegistro.addEventListener('change', () => {
        selectFilterFechaRegistro.form.submit()
    })

    selectFilterDiaSesion.addEventListener('change', () => {
        selectFilterDiaSesion.form.submit()
    })

})