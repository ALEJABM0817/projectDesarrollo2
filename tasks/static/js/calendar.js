document.addEventListener("DOMContentLoaded", function(event) {
    event.preventDefault();
    let button = document.querySelector('.save__event #save__button');

    button.addEventListener('click', function(e) {
            e.preventDefault();
            let titleText = document.querySelector('.save__event #save__title').value;
            let date = document.querySelector('.save__event #save__date').value;
            if (titleText && date) {
                let datesStorege = JSON.parse(localStorage.getItem('dates')) || [];

                let encontro = false;

                datesStorege.map(element => {
                    if (element.start == date) {
                        document.querySelector('.save__event .error').innerHTML = 'La fecha ya esta ocupada'
                        encontro = true;
                    }
                });

                if(encontro) return;

                datesStorege.push({
                    title: titleText,
                    start: date
                })

                localStorage.setItem("dates", JSON.stringify(datesStorege));
                document.querySelector('.save__event #save__title').value = '';
                document.querySelector('.save__event #save__date').value = '';

                document.querySelector('.save__event .error').innerHTML = ''
                document.querySelector('.save__event .exito').innerHTML = 'Su evento fue guardado con exito';
                setTimeout(() => {
                    document.querySelector('.save__event .exito').innerHTML = '';
                }, 3000);
            } else {
                document.querySelector('.save__event .error').innerHTML = 'Por favor ingrese ambos campos'
            }
        })
});