<h1 style="text-align: center">Proyecto Universitario Trayecto 3</h1>

<div 
style="background: #333;border-radius: 10px;padding:10px;display: flex;flex-direction: column;align-items: center">
<h2>Comandos para ejecutar el proyecto</h2>

<ol>
    <li>Para poder crear entornos virtuales puedes instalar virtualenv con el comando <code> pip install virtualenv</code> o ejecutar el comando <code>py -m venv (nombre_de_entorno)</code></li>
    <li>
        Si elegiste virtualenv ejecutar<code>virtualenv (nombre_de_entorno)</code>para crear un entorno virtual
    </li>
    <li>
        para activar dicho entorno debes ejecutar en la terminal lo siguiente <code>.\nombre_de_entorno\Scripts\activate</code>
    </li>
    <li>Despues ejecutar el siguiente comando <code>pip install -r requirements.txt</code> esto instalara todas las dependencias del proyecto</li>
    <li>Despues entrar a la carpeta donde esta nuestra aplicación <code>cd app</code></li>
    <li>Ejecutar el siguiente comando para correr las migraciones y tener todas las tablas del proyecto <code>py manage.py migrate</code></li>
    <li>y por ultimo ejecutar <code>py manage.py runserver</code> para correr el servidor</li>
</ol>
</div>

## Documentación

Para añadir nueva documentacion ejecuta el siguiente el comando

<code>py manage.py spectacular --color --file schema.yml</code>
