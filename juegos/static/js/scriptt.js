document.addEventListener('DOMContentLoaded', function() { //Se asegura que el script no se ejecuta hasta que todo el contenido del DOM haya sido completamente cargado. (por ejemplo los 'select' de región y comuna)
    var form = document.getElementById('registerForm'); //se crea la variable form, la cual guarda el formulario con el ID 'registerForm'. Dicha variable será usada más adelante

    // Se agregan los datos para el dropdown de región. Se define un arreglo 'regiones' la que contiene las regiones de Chile, esta variable/arreglo se usará para el dropdown (menú desplegable) de regiones del formulario
    var regiones = [
        'Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama', 
        'Coquimbo', 'Valparaíso', 'Metropolitana', "O'Higgins", 
        'Maule', 'Ñuble', 'Biobío', 'La Araucanía', 
        'Los Ríos', 'Los Lagos', 'Aysén', 'Magallanes'
    ];

    // Se agregan los datos para el dropdown de comuna. Se define un arreglo 'comunas' la que contiene las comunas de Chile, esta variable/arreglo se usará para el dropdown (menú desplegable) de comunas del formulario
    var comunas = {
        'Arica y Parinacota': ['Arica', 'Camarones', 'Putre', 'General Lagos'],
        'Tarapacá': ['Iquique', 'Alto Hospicio', 'Pozo Almonte', 'Huara', 'Camiña', 'Colchane', 'Pica'],
        'Antofagasta': ['Antofagasta', 'Mejillones', 'Sierra Gorda', 'Taltal', 'Calama', 'Ollagüe', 'San Pedro de Atacama'],
        'Atacama': ['Copiapó', 'Caldera', 'Tierra Amarilla', 'Chañaral', 'Diego de Almagro', 'Vallenar', 'Huasco', 'Freirina', 'Alto del Carmen'],
        'Coquimbo': ['La Serena', 'Coquimbo', 'Andacollo', 'La Higuera', 'Vicuña', 'Illapel', 'Canela', 'Los Vilos', 'Salamanca', 'Ovalle', 'Monte Patria', 'Combarbalá', 'Punitaqui', 'Río Hurtado'],
        'Valparaíso': ['Valparaíso', 'Viña del Mar', 'Concón', 'Quilpué', 'Villa Alemana', 'Quillota', 'La Cruz', 'La Calera', 'Hijuelas', 'Nogales', 'San Antonio', 'Cartagena', 'El Tabo', 'El Quisco', 'Algarrobo', 'Santo Domingo', 'Los Andes', 'San Felipe', 'Llay-Llay', 'Putaendo', 'Santa María', 'Panquehue', 'Petorca', 'La Ligua', 'Cabildo', 'Papudo', 'Zapallar', 'Casablanca', 'San Esteban'],
        'Metropolitana': ['Santiago', 'Cerrillos', 'Cerro Navia', 'Conchalí', 'El Bosque', 'Estación Central', 'Huechuraba', 'Independencia', 'La Cisterna', 'La Florida', 'La Granja', 'La Pintana', 'La Reina', 'Las Condes', 'Lo Barnechea', 'Lo Espejo', 'Lo Prado', 'Macul', 'Maipú', 'Ñuñoa', 'Pedro Aguirre Cerda', 'Peñalolén', 'Providencia', 'Pudahuel', 'Quilicura', 'Quinta Normal', 'Recoleta', 'Renca', 'San Joaquín', 'San Miguel', 'San Ramón', 'Vitacura'],
        "O'Higgins": ['Rancagua', 'Machalí', 'Graneros', 'Mostazal', 'Requínoa', 'Rengo', 'Coinco', 'Coltauco', 'Doñihue', 'Olivar', 'Peumo', 'Pichidegua', 'Quinta de Tilcoco', 'San Vicente', 'Pichilemu', 'Marchigüe', 'Navidad', 'La Estrella', 'Litueche', 'Paredones', 'San Fernando', 'Chépica', 'Chimbarongo', 'Lolol', 'Nancagua', 'Palmilla', 'Peralillo', 'Placilla', 'Pumanque', 'Santa Cruz'],
        'Maule': ['Talca', 'San Clemente', 'Pelarco', 'Pencahue', 'Maule', 'San Rafael', 'Curepto', 'Constitución', 'Empedrado', 'Río Claro', 'Linares', 'San Javier', 'Villa Alegre', 'Yerbas Buenas', 'Colbún', 'Parral', 'Retiro', 'Longaví', 'Cauquenes', 'Chanco', 'Pelluhue', 'Curicó', 'Teno', 'Romeral', 'Molina', 'Sagrada Familia', 'Hualañé', 'Licantén', 'Vichuquén'],
        'Ñuble': ['Chillán', 'Bulnes', 'Cobquecura', 'Coelemu', 'Coihueco', 'El Carmen', 'Ninhue', 'Ñiquén', 'Pemuco', 'Pinto', 'Portezuelo', 'Quillón', 'Quirihue', 'Ránquil', 'San Carlos', 'San Fabián', 'San Ignacio', 'San Nicolás', 'Treguaco', 'Yungay'],
        'Biobío': ['Concepción', 'Coronel', 'Chiguayante', 'Florida', 'Hualqui', 'Lota', 'Penco', 'San Pedro de la Paz', 'Santa Juana', 'Talcahuano', 'Tomé', 'Hualpén', 'Lebu', 'Arauco', 'Cañete', 'Contulmo', 'Curanilahue', 'Los Álamos', 'Tirúa', 'Los Ángeles', 'Antuco', 'Cabrero', 'Laja', 'Mulchén', 'Nacimiento', 'Negrete', 'Quilaco', 'Quilleco', 'San Rosendo', 'Santa Bárbara', 'Tucapel', 'Yumbel', 'Alto Biobío'],
        'La Araucanía': ['Temuco', 'Carahue', 'Cunco', 'Curarrehue', 'Freire', 'Galvarino', 'Gorbea', 'Lautaro', 'Loncoche', 'Melipeuco', 'Nueva Imperial', 'Padre Las Casas', 'Perquenco', 'Pitrufquén', 'Pucón', 'Saavedra', 'Teodoro Schmidt', 'Toltén', 'Vilcún', 'Villarrica', 'Cholchol', 'Angol', 'Collipulli', 'Curacautín', 'Ercilla', 'Lonquimay', 'Los Sauces', 'Lumaco', 'Purén', 'Renaico', 'Traiguén', 'Victoria'],
        'Los Ríos': ['Valdivia', 'Corral', 'Lanco', 'Los Lagos', 'Máfil', 'Mariquina', 'Paillaco', 'Panguipulli', 'La Unión', 'Futrono', 'Lago Ranco', 'Río Bueno'],
        'Los Lagos': ['Puerto Montt', 'Calbuco', 'Cochamó', 'Fresia', 'Frutillar', 'Llanquihue', 'Los Muermos', 'Maullín', 'Puerto Varas', 'Castro', 'Ancud', 'Chonchi', 'Curaco de Vélez', 'Dalcahue', 'Puqueldón', 'Queilén', 'Quellón', 'Quemchi', 'Quinchao', 'Osorno', 'Puerto Octay', 'Purranque', 'Puyehue', 'Río Negro', 'San Juan de la Costa', 'San Pablo', 'Chaitén', 'Futaleufú', 'Hualaihué', 'Palena'],
        'Aysén': ['Coyhaique', 'Lago Verde', 'Aysén', 'Cisnes', 'Guaitecas', 'Cochrane', 'O\'Higgins', 'Tortel', 'Chile Chico', 'Río Ibáñez'],
        'Magallanes': ['Punta Arenas', 'Laguna Blanca', 'Río Verde', 'San Gregorio', 'Cabo de Hornos', 'Antártica', 'Porvenir', 'Primavera', 'Timaukel', 'Natales', 'Torres del Paine']
    };

      // Añadir regiones al Dropdown
    var regionDropdown = document.getElementById('region'); //obtiene el elemento 'select' del DOM que tiene el ID 'region', de modo de guardarlo en la variable regionDropdown
    regiones.forEach(function(region) { //recorre el arreglo/variable 'regiones usando .forEach para en la siguiente crear un elemento 'option' en cada región
        var option = document.createElement('option');
        option.value = region; //establece el valor de cada región (que es el nombre de la región)
        option.text = region; //establece el texto de cada región (que es el nombre de la región)
        regionDropdown.appendChild(option); //añade a cada opción con su respectivo valor y texto al dropdown de regiones 'regionDropdown'
    });


        // Actualizar las comunas cuando se selecciona una región
    var comunaDropdown = document.getElementById('comuna'); //obtiene el elemento 'select' del DOM que tiene el ID 'comuna', de modo de guardarlo en la variable 'comunaDropdown'
    regionDropdown.addEventListener('change', function() { //Se añade un event listener al dropdown de regiones. De modo de escuchar el evento 'change' cada vez que el usuario selecciona una región diferente en el dropdown de regiones
        var selectedRegion = this.value; //dentro de la función del evento 'change', this. hace referencia al elemento que activó el evento, donde this.value obtiene el valor de la región seleccionada y lo almacena en 'selectedRegion'
        var comunasPorRegion = comunas[selectedRegion] || [];  //busca en el objeto 'comunas' definido previamente' el arreglo/variable(Región) que contiene dichas comunas asociadas. Si esque no se seleccionó ninguna 'comuna' entonces se le asigna un valor vacio [] a 'comunasPorRegion'

        // Limpiar las opciones actuales del dropdown de comuna
        comunaDropdown.innerHTML = '<option value="">Selecciona tu comuna</option>'; // .innerHTML es una propiedad que permite establecer o obtener el contenido html de un elemento. 
        //Este elemento '<option>' es un elemento con valor vacio ' value="" ', es decir no tiene un valor real asociado, mas que nada se usa para que el usuario sepa que debe seleccionar algo


        // Añadir nuevas opciones de comuna, permite la actualización dinamica del contenido del formulario
        comunasPorRegion.forEach(function(comuna) {    //.forEach ejecuta una función por cada elemento del array 'comunasPorRegion'. El parametro 'comuna' representa el nombre de cada comuna del array
            var option = document.createElement('option');  //crea un elemento llamado '<option>' de HTML. Este elemento es utilizado para representar una opción en un dropdown '<selec7>'
            option.value = comuna;  //se establece el valor de la comuna
            option.text = comuna;   //se establece el texto que se mostrará en el dropdown para esa opción
            comunaDropdown.appendChild(option);  //añade el elemento '<option>' al dropdown 'comunaDropdown'
        });
    });


    // Validación en tiempo real para los campos
    form.addEventListener('input', function(event) { //form es la variable que hace referencia al formulario 'registerform'. addEventListener permite registrar un evento, en este caso se usa un listener para el evento 'input' del formulario. El evento 'input' se dispara cada vez que el usuario modifica el valor de un campo de entrada del formlario, tal como escribir una entrada o escoger una opción del dropdown
        validateField(event.target); //la función se ejecuta cada vez que se dispara el evento 'input', en donde event.target es una propiedad del objeto 'event'.
        //la función definida 'validateField' se encarga de validar el campo. Esta función recibe el elemento que ha generado el evento 'event.target' como argumento 
    });

     // Validaciones completas al enviar formulario
    form.addEventListener('submit', function(event) { //cada vez que se intente enviar el formulario, se ejecutara la siguiente función
        event.preventDefault(); //se usa para cancelar la acción, evitando que el formulario se envie (lo cual normalmente recargaria la pagina o te llevaria a otra pagina)
        var isFormValid = true; //variable que se usa para verificar si todos os campos del formulario son validos


        // Se validan todos los campos
        var inputs = form.querySelectorAll('input, select'); //'querySelectorAll selecciona todos los elementos 'input' y 'select' dentro del formulario, incluyendo todos los campos de entrada que deben ser validados
        inputs.forEach(function(input) {  //Se recorren todos los elementos seleccionados, para cada elemento se ejecuta la función
            if (!validateField(input)) {  ////validateField(input) es una función que valida el campo de entrada.
                isFormValid = false;  //Si la función devuelve false, se establece 'isFormValid' en 'false., indicando que al menos un campo del formulario no es valido
            }
        });



        // Si el formulario es válido
        if (isFormValid) {   //si isFormValid es 'true' significa que todos los campos son válidos
            var modal = new bootstrap.Modal(document.getElementById('successModal')); //mostrando un modal de exito o notificacion que el formulario se envio correctamente
            modal.show();
            form.reset(); //restablece el formulario a sus valores iniciales, limpiando los campos de entrada
        }
    });

    function validateField(input) { //Se encarga de validar el contenido de un campo del formulario
        var value = input.value.trim(); //aqui se obtiene el valor actual del campo y .trim elimina los espacios en blanco al principio y al final
        var isValid = true; //Se establece isValid en 'true' inicialmente. Si algo falla cambiara a 'false'

        switch (input.id) {
            case 'name':
            case 'apellido':
                isValid = /^[A-Za-z]+$/.test(value); //'name' y 'apellido' deben tener solo letras /^[A-Za-z]+$/
                break;
            case 'email':
                isValid = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value); //email debe tener el formato de correo electronico
                break;
            case 'password':
                isValid = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/.test(value); //password debe tener entre 6 y 18 caracteres y almenos 1 letra mayuscula y 1 digito
                break;
            case 'confirmPassword':
                isValid = value === document.getElementById('password').value; //confirmar contraseña, debe calzar con la contraseña anterior
                break;
            case 'dob':
                var age = calculateAge(value);
                isValid = age >= 18;  //la edad debe ser mayor o igual a 18
                break;
            case 'region':
                isValid = value !== ''; //Quise especificar que la region es necesaria ya que usualmente en un registro este dato es necesario, sé que el ejercicio no lo pedia explicitamente
                break;
            case 'comuna':
                isValid = value !== ''; //Quise especificar que la comuna es necesaria ya que usualmente en un registro este dato es necesario, sé que el ejercicio no lo pedia explicitamente
                break;
            
        }

        if (!isValid) {
            input.classList.add('is-invalid');  //Si 'isValid' es false, entonces se añade la clase 'is-invalid' al campo de modo que se vea reflejado en .html
        } else {
            input.classList.remove('is-invalid'); //Caso contrario, se elimina el 'is-invalid'
        }

        return isValid;
    }

    function calculateAge(dob) {  //esta función calcula la edad a partir de la fecha de nacimiento 'dob'
        var dobDate = new Date(dob); //Se crea un objeto de fecha con la fecha de nacimiento
        var diff = Date.now() - dobDate.getTime(); //se calcula la diferencia entre la fecha actual y la de nacimiento
        var ageDate = new Date(diff);  //crea una nueva fecha con la diferencia y calcula el año actual
        return Math.abs(ageDate.getUTCFullYear() - 1970); //calcula la edad a partir del año de la fecha calculada. Se usa 1970 ya que es el año base de 'Date' de JavaScript para obtener la edad en años
    }
});