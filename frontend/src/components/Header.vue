<template>
  <nav class="navbar navbar-expand-lg navbar-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Webchat</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="fas fa-user-friends"></i> Amigos
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Carlos</a></li>
            <li><a class="dropdown-item" href="#">Ricardo</a></li>
            <li><a class="dropdown-item" href="#">João</a></li>
            <li><a class="dropdown-item" href="#">Paulo</a></li>
            <li><a class="dropdown-item" href="#">Juliana</a></li>
            <li><a class="dropdown-item" href="#">Maria</a></li>
            <li><a class="dropdown-item" href="#">Fábio</a></li>
            <li><a class="dropdown-item" href="#">Joana</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Ver todos</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="fas fa-users"></i> Grupos
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Grupo 1</a></li>
            <li><a class="dropdown-item" href="#">Grupo 2</a></li>
            <li><a class="dropdown-item" href="#">Groupo 3</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Ver todos</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="fas fa-cogs"></i> Configurações
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Idioma</a></li>
            <li><a class="dropdown-item" href="#">Tema</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Conta</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex">
        <button class="btn btn-outline-success" type="submit">Entrar</button>
      </form>
      </div>
  </div>
  </nav>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
:root{
  --semi-light: #949494;
}

nav{
  background: #FFF;
  margin-bottom: 1em;
}

i{
  color: var(--semi-light);
}

</style>