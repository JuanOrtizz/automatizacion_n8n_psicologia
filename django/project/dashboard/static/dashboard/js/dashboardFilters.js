document.addEventListener('DOMContentLoaded', ()=>{
    const selectFilter = document.getElementById("filter-sessions")
    selectFilter.addEventListener('change',()=>{
        selectFilter.form.submit()
    })
})