
# Proyecto Curso Python PIP

Sistema para la administración del inventario de venta de
discos de vinilo, este sistema cuenta con lo siguiente.

1. Inicio de sesión
        
        Correo electrónico y contraseña
        
2. Recuperación de contraseña.
        
        Comprobación de correo electrónico válido y existente.
        Envío de un enlace al correo electrónico del usuario, para que se pueda
        restablecer dicha contraseña.

3. Registro. 
    
        Se debe permitir el registro de nuevos usuarios, este registro debe solicitar:
        ■ Nombre completo
        ■ Nombre Usuario
        ■ Correo electrónico
        ■ Contraseña
        ■ Scopes (permisos)

        Una vez realizado el registro se debe enviar un correo electrónico al usuario 
        informando que se realizó un registro en el portal y que es necesario activar
        su cuenta dando click en el enlace adjunto al correo, de lo contrario su cuenta
        permanecerá inactiva. (Se debe mandar un enlace en el correo para activar la cuenta).

4. Una vez dentro del sistema, cuenta con los siguientes módulos:

    4.1 CRUD de usuarios. 
        
        Se deben poder crear, tanto administradores como usuarios, la diferencia 
        entre ambos es que los administradores pueden editar usuarios.

    4.2 CRUD de discos
        
        Creación de discos
        
        ● Nombre
        ● Álbum
        ● Artista
        ● Género
        ● Año
        ● Foto de portada
    4.3 Listado de discos
        
        ● Búsqueda por: 
           ■ Nombre
           ■ Album 
           ■ Artista
        ● Edición de cada disco
        ● Eliminación de cada disco

    4.4 Compra de un disco

        ● Nombre del disco
        ● Usuario que lo compro
        ● Precio
        ● Fecha de compra
    
    4.4 Carga masiva de discos por Excel

        ● Definición de layout
            ■ ARTISTA	
            ■ ALBUM	
            ■ GENERO	
            ■ AÑO	
            ■ PRECIO

    4.5 Descarga de inventario de discos por Excel

        ● Definición de cabeceras
            ■ ID	
            ■ ARTISTA	
            ■ ALBUM	
            ■ GENERO	
            ■ AÑO	
            ■ PRECIO

    4.6 Generación de reporte de ventas por Excel

        ● Definición de cabeceras
            ■ ID	
            ■ ALBUM	
            ■ ARTISTA	
            ■ GENERO	
            ■ AÑO	
            ■ PRECIO	
            ■ CLIENTE	
            ■ CORREO	
            ■ FECHA DE COMPRA

    4.7 Generación de reporte de ventas por PDF

        ● Definición de cabeceras
            ■ ID	
            ■ FECHA DE COMPRA
            ■ CLIENTE	
            ■ ALBUM	
            ■ ARTISTA	
            ■ PRECIO	
            ■ TOTAL

    4.8 Conexión con API de Spotify.

        Consulta para buscar discos y guardarlos en la base de datos.
         
## Acknowledgements

 - [Python](https://www.python.org/downloads/)
 - [FastAPI](https://fastapi.tiangolo.com/)
 


## Layout

Layout para carga masiva de Discos
- [Layout](https://sorianoarizacom-my.sharepoint.com/:x:/g/personal/r_salazard_soriano-ariza_com/EV3D1FcM9FxGkqKP3gamUzoBwCRIhoFFwT1mN3p8GjAnUA?e=egkAsP)


## Authors

- [@rodsalazard](https://bitbucket.org/rodsalazard)


## Badges

[![MIT License](https://img.shields.io/pypi/pyversions/fastapi?color=green&logo=python)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi/)
## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Contributing

Las contribuciones siempre son bienvenidas! 😄



## Run Locally

Clone the project

Go to the project directory

```bash
    cd py-project
```

Go to the game directory
```bash
    cd game
```

Run Locally
```bash
    python3 main.py
```


## Run Locally APP

Clone the project

Go to the project directory

```bash
    cd py-project
```

Go to the game directory
```bash
    cd app
```

Activate the Environment
```bash
    source env/bin/activate
```

Install Requirements
```bash
    pip3 install -r requirements.txt
```

Run Locally
```bash
    python3 main.py
```




## Documentation

 - [Python](https://www.python.org/downloads/)
 - [Matplolib](https://pypi.org/project/matplotlib/)
 - [Pandas](https://pandas.pydata.org/)



## Feedback

If you have any feedback, please reach out to us at r.salazard@soriano-ariza.com


## 🚀 About Me
I'm software developer 🦊

