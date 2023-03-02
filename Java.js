
var identificacion= 2810047543
var Nombre= "Martin Valle";
var Direccion= "cra 15 # 2-34";
var Telefono= 3153794216
var Edad= 70
var Estado_Civil= "casado";
var Numero_hijos= 2
var Estatura= 168
var Fecha_contratacion= "02/07/2021";
var Sueldo_Basico= 800000
var Dias_laborados= 26

var datos= document.getElementById("info");

datos.innerHTML = `
<h3>Estos son los datos personales de una persona</h3>
<h2>Identificacion: ${identificacion}</h2>
<h2>Nombre: ${Nombre}</h2>
<h2>Direccion: ${Direccion}</h2>
<h2>Telefono: ${Telefono}</h2>
<h2>Edad: ${Edad}</h2>
<h2>Estado Civil: ${Estado_Civil}</h2>
<h2>Numero de hijos: ${Numero_hijos}</h2>
<h2>Estatura: ${Estatura}</h2>
<h2>Fecha de contratacion: ${Fecha_contratacion}</h2>
<h2>Sueldo Basico: ${Sueldo_Basico}</h2>
<h2>Dias Laborados: ${Dias_laborados}</h2>
`;

